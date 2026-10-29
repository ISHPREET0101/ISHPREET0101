"""Render a contribution calendar with a small animated snake. Standard library only."""
import json
import os
import sys
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
query = '{ user(login: "ISHPREET0101") { contributionsCollection { contributionCalendar { weeks { contributionDays { date contributionCount color } } } } } }'
if os.environ.get('GH_TOKEN'):
    request = Request('https://api.github.com/graphql', data=json.dumps({'query': query}).encode(), headers={'Authorization': 'Bearer '+os.environ['GH_TOKEN'], 'Content-Type': 'application/json'})
    with urlopen(request, timeout=30) as response:
        payload = json.load(response)
else:
    if len(sys.argv) != 2:
        raise SystemExit('Set GH_TOKEN or pass a contribution-calendar JSON snapshot path.')
    payload = json.loads(Path(sys.argv[1]).read_text(encoding='utf-8-sig'))
if payload.get('errors'):
    raise RuntimeError('Contribution query failed; previous graphic preserved.')
weeks = payload['data']['user']['contributionsCollection']['contributionCalendar']['weeks']
width = len(weeks)*18+24
parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="164" viewBox="0 0 {width} 164" role="img" aria-labelledby="title desc"><title id="title">My contributions</title><desc id="desc">GitHub contribution calendar with a decorative snake animation.</desc><style>.empty{{fill:#ebedf0}}@media(prefers-color-scheme:dark){{.empty{{fill:#161b22}}}}@media(prefers-reduced-motion:reduce){{.snake{{display:none}}}}</style>']
points=[]
for x,week in enumerate(weeks):
    for y,day in enumerate(week['contributionDays']):
        color = day['color']
        cls = ' class="empty"' if not day['contributionCount'] else ''
        parts.append(f'<rect x="{12+x*18}" y="{10+y*18}" width="13" height="13" rx="3" fill="{color}"{cls}><title>{day["date"]}: {day["contributionCount"]} contributions</title></rect>')
    ys=range(len(week['contributionDays'])) if x%2==0 else reversed(range(len(week['contributionDays'])))
    points.extend((18.5+x*18,16.5+y*18) for y in ys)
path='M'+' L'.join(f'{x},{y}' for x,y in points)
for i in range(6):
    parts.append(f'<rect class="snake" x="-5" y="-5" width="10" height="10" rx="3" fill="{["#8957e5","#a371f7","#bc8cff","#c8a5ff","#d8b9ff","#e8d5ff"][i]}"><animateMotion dur="45s" begin="-{i*0.12}s" repeatCount="indefinite" path="{path}"/></rect>')
parts.append('</svg>')
(ROOT/'assets').mkdir(exist_ok=True)
(ROOT/'assets/contributions.svg').write_text(''.join(parts),encoding='utf-8')
print('Contribution graphic updated.')
