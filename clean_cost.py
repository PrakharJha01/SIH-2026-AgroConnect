import re

with open('pages/23_Buyer_Matches.py', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('ðŸ’°', '💰')
text = text.replace('â‚¹', '₹')

with open('pages/23_Buyer_Matches.py', 'w', encoding='utf-8') as f:
    f.write(text)
