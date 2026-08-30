with open('pages/23_Buyer_Matches.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re
match = re.search(r'def _render_logistics\(.*?(?=\ndef _|\n# )', text, re.DOTALL)
if match:
    print(match.group(0))
