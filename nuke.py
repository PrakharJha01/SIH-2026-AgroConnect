import re

def clean_file(fpath):
    with open(fpath, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Remove specific corrupted remnants by explicitly stripping them out
    # These characters are literal corrupted latin-1 bytes masquerading as unicode.
    text = re.sub(r'[\x8d\x8f\x9d\x90¢ïâ¸ÃÅÂ]+', '', text)
    
    # Also strip zero width joiner if left alone
    text = re.sub(r'‍', '', text)

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(text)

files_to_fix = [
    'components/common/cards.py',
    'pages/02_Market_Prices.py'
]

for fpath in files_to_fix:
    clean_file(fpath)

print('Cleaned totally.')
