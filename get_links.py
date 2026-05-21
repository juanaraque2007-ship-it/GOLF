import urllib.request, re
try:
    html = urllib.request.urlopen('https://www.fedgolfclm.com/informacion-fgclm-ley-de-transparencia/').read().decode('utf-8')
    matches = re.findall(r'<a.*?href=[\'\"]([^\'\"]+\.pdf)[\'\"][^>]*>(.*?)</a>', html, flags=re.IGNORECASE|re.DOTALL)
    for m in matches:
        text = re.sub(r'<[^>]+>', '', m[1]).strip()
        print(f'{text} -> {m[0]}')
except Exception as e:
    print(e)
