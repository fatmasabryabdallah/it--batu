import pathlib
import re
import urllib.parse
import urllib.request
import urllib.error

root = pathlib.Path(r'D:\vertual 11')
assets = set()
for html in root.glob('*.html'):
    text = html.read_text(encoding='utf-8', errors='ignore')
    for m in re.findall(r'src=["\']([^"\']+)["\']', text):
        if 'images/' in m or 'pdfs/' in m or m.endswith('.png') or m.endswith('.pdf'):
            assets.add(m)
    for m in re.findall(r'href=["\']([^"\']+)["\']', text):
        if 'images/' in m or 'pdfs/' in m or m.endswith('.png') or m.endswith('.pdf'):
            assets.add(m)
    for m in re.findall(r'"(images/[^"]+)"|\'(images/[^\']+)\'', text):
        for path in m:
            if path and ('images/' in path or 'pdfs/' in path):
                assets.add(path)

for a in sorted(assets):
    if a.startswith('http'):
        continue
    url = 'https://it-batu.vercel.app/' + urllib.parse.quote(a.replace('\\', '/'), safe=':/')
    local_path = root / a.replace('/', '\\')
    if local_path.exists():
        print('SKIP', a)
        continue
    local_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        resp = urllib.request.urlopen(url, timeout=30)
        local_path.write_bytes(resp.read())
        print('OK', a)
    except Exception as e:
        print('ERR', a, e)
