with open('pages/23_Buyer_Matches.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.search(r'def _render_logistics_map', text)
if matches:
    print("Found map")
else:
    print("No map")
