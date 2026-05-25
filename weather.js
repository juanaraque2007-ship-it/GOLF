const provinces = [
  { name: 'Guadalajara', short: 'GUA', lat: 40.6333, lon: -3.1667 },
  { name: 'Toledo', short: 'TOL', lat: 39.8581, lon: -4.0226 },
  { name: 'Ciudad Real', short: 'CR', lat: 38.9863, lon: -3.9291 },
  { name: 'Cuenca', short: 'CUE', lat: 40.0704, lon: -2.1374 },
  { name: 'Albacete', short: 'ALB', lat: 38.9942, lon: -1.8564 }
];

function getWeatherIcon(code) {
  if (code === 0) return `<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line></svg>`; // Sol
  
  if (code <= 3) return `<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M17.5 19H9a7 7 0 1 1 6.71-9h1.79a4.5 4.5 0 1 1 0 9Z"></path></svg>`; // Nube
  
  if ((code >= 51 && code <= 65) || (code >= 80 && code <= 82)) return `<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M20 16.58A5 5 0 0 0 18 7h-1.26A8 8 0 1 0 4 15.25"></path><line x1="16" y1="16" x2="16" y2="22"></line><line x1="8" y1="16" x2="8" y2="22"></line><line x1="12" y1="18" x2="12" y2="24"></line></svg>`; // Lluvia
  
  if (code >= 71 && code <= 77) return `<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><line x1="2" y1="12" x2="22" y2="12"></line><line x1="12" y1="2" x2="12" y2="22"></line><path d="m20 16-4-4 4-4"></path><path d="m4 8 4 4-4 4"></path><path d="m16 4-4 4-4-4"></path><path d="m8 20 4-4 4 4"></path></svg>`; // Nieve
  
  if (code >= 95) return `<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M19 16.9A5 5 0 0 0 18 7h-1.26a8 8 0 1 0-11.62 9"></path><polyline points="13 11 9 17 15 17 11 23"></polyline></svg>`; // Tormenta
  
  return `<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M17.5 19H9a7 7 0 1 1 6.71-9h1.79a4.5 4.5 0 1 1 0 9Z"></path></svg>`;
}

async function initWeatherWidget() {
  const container = document.getElementById('weather-widget');
  if (!container) return;

  try {
    const promises = provinces.map(async p => {
      const res = await fetch(`https://api.open-meteo.com/v1/forecast?latitude=${p.lat}&longitude=${p.lon}&current_weather=true`);
      const data = await res.json();
      return {
        name: p.name,
        short: p.short,
        temp: Math.round(data.current_weather.temperature),
        wind: Math.round(data.current_weather.windspeed),
        code: data.current_weather.weathercode
      };
    });

    const weatherData = await Promise.all(promises);
    renderStaticWidget(container, weatherData);
  } catch (e) {
    console.error("Error cargando el tiempo de CLM:", e);
    container.style.display = 'none';
  }
}

function renderStaticWidget(container, data) {
  let html = `<div class="weather-body">`;
  
  data.forEach(p => {
    html += `
      <div class="weather-item" title="${p.name}">
        <div class="weather-province">${p.short}</div>
        <div class="weather-icon">${getWeatherIcon(p.code)}</div>
        <div class="weather-temp">${p.temp}°</div>
        <div class="weather-wind">${p.wind} km/h</div>
      </div>
    `;
  });
  
  html += `</div>`;
  container.innerHTML = html;
}

document.addEventListener('DOMContentLoaded', initWeatherWidget);
