import json
import re

data = [
  {
    "year": 2026,
    "docs": [
      {"name": "Presupuesto 2026", "url": "https://www.fedgolfclm.com/wp-content/uploads/2026/04/PRESUPUESTO-2026.pdf", "icon": "presupuesto"}
    ]
  },
  {
    "year": 2025,
    "docs": [
      {"name": "Presupuesto 2025", "url": "https://www.fedgolfclm.com/wp-content/uploads/2025/03/PRESUPUESTO-fgclm-2025.pdf", "icon": "presupuesto"},
      {"name": "Censo de Jugadores 2025", "url": "https://www.fedgolfclm.com/wp-content/uploads/2026/02/CENSO-JUGADORES-TORNEOS-FGCLM-2025.pdf", "icon": "censo"},
      {"name": "Balance de Pérdidas y Ganancias 2025", "url": "https://www.fedgolfclm.com/wp-content/uploads/2026/04/Cuenta-Perdidas-y-Ganancias-2025.pdf", "icon": "balance"},
      {"name": "Balance de Situación 2025", "url": "https://www.fedgolfclm.com/wp-content/uploads/2026/04/Balance-Situacion-2025.pdf", "icon": "balance"},
      {"name": "Ejecución de Presupuesto 2025", "url": "https://www.fedgolfclm.com/wp-content/uploads/2026/04/EJECUCION-INGRESOS-GASTOS-2025.pdf", "icon": "ejecucion"}
    ]
  },
  {
    "year": 2024,
    "docs": [
      {"name": "Presupuesto 2024", "url": "https://www.fedgolfclm.com/wp-content/uploads/2024/02/Presupuesto-FGCLM-2024.pdf", "icon": "presupuesto"},
      {"name": "Censo de Jugadores 2024", "url": "https://www.fedgolfclm.com/wp-content/uploads/2025/02/CENSO-ELECTORES-FGCLM-2024.pdf", "icon": "censo"},
      {"name": "Balance de Pérdidas y Ganancias 2024", "url": "https://www.fedgolfclm.com/wp-content/uploads/2025/03/CUENTA-DE-PERDIDAS-Y-GANANCIAS-fgclm-2024.pdf", "icon": "balance"},
      {"name": "Balance de Situación 2024", "url": "https://www.fedgolfclm.com/wp-content/uploads/2025/03/BALANCE-fgclm-2024.pdf", "icon": "balance"},
      {"name": "Ejecución de Presupuesto 2024", "url": "https://www.fedgolfclm.com/wp-content/uploads/2025/03/Ejecucion-presupuestaria-fgclm-2024.pdf", "icon": "ejecucion"}
    ]
  },
  {
    "year": 2023,
    "docs": [
      {"name": "Presupuesto 2023", "url": "https://www.fedgolfclm.com/wp-content/uploads/2023/04/Presupuesto-2023.pdf", "icon": "presupuesto"},
      {"name": "Balance de Pérdidas y Ganancias 2023", "url": "https://www.fedgolfclm.com/wp-content/uploads/2024/02/BALANCE-PERDIDAS-Y-GANANCIAS-FGCLM-2023.pdf", "icon": "balance"},
      {"name": "Balance de Situación 2023", "url": "https://www.fedgolfclm.com/wp-content/uploads/2024/02/BALANCES-DE-SITUACION-FGCLM-2023.pdf", "icon": "balance"},
      {"name": "Ejecución de Presupuesto 2023", "url": "https://www.fedgolfclm.com/wp-content/uploads/2024/02/Ejecucion-presupuesto-FGCLM-2023.pdf", "icon": "ejecucion"}
    ]
  },
  {
    "year": 2022,
    "docs": [
      {"name": "Presupuesto 2022", "url": "https://www.fedgolfclm.com/wp-content/uploads/2022/04/Presupuesto-fgclm-Asamblea-2022.pdf", "icon": "presupuesto"},
      {"name": "Balance de Pérdidas y Ganancias 2022", "url": "https://www.fedgolfclm.com/wp-content/uploads/2023/04/Balance-de-P-Y-G-2022.pdf", "icon": "balance"},
      {"name": "Balance de Situación 2022", "url": "https://www.fedgolfclm.com/wp-content/uploads/2023/04/BALANCE-SITUACION-2022.pdf", "icon": "balance"},
      {"name": "Ejecución de Presupuesto 2022", "url": "https://www.fedgolfclm.com/wp-content/uploads/2023/04/Ejecucion-presupuestaria-2022.pdf", "icon": "ejecucion"}
    ]
  },
  {
    "year": 2021,
    "docs": [
      {"name": "Presupuesto 2021", "url": "https://www.fedgolfclm.com/wp-content/uploads/2021/11/Presupuesto-fgclm-2021.pdf", "icon": "presupuesto"},
      {"name": "Cuenta de Pérdidas y Ganancias 2021", "url": "https://www.fedgolfclm.com/wp-content/uploads/2022/04/PERDIDAS-Y-GANANCIAS-fgclm-2021.pdf", "icon": "balance"},
      {"name": "Balance de Situación 2021", "url": "https://www.fedgolfclm.com/wp-content/uploads/2022/04/BALANCE-SITUACION-fgclm-2021.pdf", "icon": "balance"},
      {"name": "Ejecución de Presupuesto 2021", "url": "https://www.fedgolfclm.com/wp-content/uploads/2022/04/Ejecucion-del-presupuesto-fgclm-2021.pdf", "icon": "ejecucion"}
    ]
  },
  {
    "year": 2020,
    "docs": [
      {"name": "Cuenta de Pérdidas y Ganancias 2020", "url": "https://www.fedgolfclm.com/wp-content/uploads/2021/11/BALANCE-PERDIDAS-Y-GANANCIAS-fgclm-2020.pdf", "icon": "balance"},
      {"name": "Balance de Situación 2020", "url": "https://www.fedgolfclm.com/wp-content/uploads/2021/11/BALANCE-DE-SITUACION-fgclm-2020.pdf", "icon": "balance"}
    ]
  }
]

html = ''
for y in data:
    html += f'  <div class="block-title" style="margin-top: 48px; font-size: 20px;">Documentación {y["year"]}</div>\n'
    html += '  <div class="doc-list" style="margin-bottom: 24px;">\n'
    for doc in y['docs']:
        if doc['icon'] == 'presupuesto':
            svg = '<svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" style="display:inline-block; vertical-align:middle; color:var(--gold);"><path d="M12 1v22M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path></svg>'
        elif doc['icon'] == 'balance':
            svg = '<svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" style="display:inline-block; vertical-align:middle; color:var(--gold);"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>'
        elif doc['icon'] == 'censo':
            svg = '<svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" style="display:inline-block; vertical-align:middle; color:var(--gold);"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>'
        else:
            svg = '<svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" style="display:inline-block; vertical-align:middle; color:var(--gold);"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline></svg>'
            
        html += f'    <a href="{doc["url"]}" target="_blank" class="doc-item">\n'
        html += f'      <div class="doc-icon">\n        {svg}\n      </div>\n'
        html += f'      <div class="doc-info">\n'
        html += f'        <div class="doc-nombre">{doc["name"]}</div>\n'
        html += f'        <div class="doc-tipo">PDF Document</div>\n'
        html += f'      </div>\n'
        html += f'      <div class="doc-anyo">{y["year"]}</div>\n'
        html += f'    </a>\n'
    html += '  </div>\n'

with open('transparencia.html', 'r', encoding='utf-8') as f:
    orig = f.read()

new_html = re.sub(
    r'(?s)<div class="block-title">Documentos Institucionales</div>.*?(?=<div class="block-title">Solicitud de Información</div>)',
    html,
    orig
)

with open('transparencia.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

