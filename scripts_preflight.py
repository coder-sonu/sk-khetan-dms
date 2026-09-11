import os, sys, zipfile
from pathlib import Path
root=Path(__file__).resolve().parent
required=['app.py','api/index.py','vercel.json','requirements.txt','templates/app.html','templates/login.html','static/app.js','vehicle_master_seed.xlsx']
missing=[p for p in required if not (root/p).exists()]
print('DMS V12 preflight')
print('Root:', root)
if missing:
    print('MISSING:', ', '.join(missing)); sys.exit(1)
print('Required files: OK')
print('DMS_SECRET_KEY:', 'SET' if os.getenv('DMS_SECRET_KEY') else 'NOT SET (expected locally)')
print('Preflight: PASS')
