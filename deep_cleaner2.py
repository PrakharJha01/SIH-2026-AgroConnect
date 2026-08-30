import glob

replacer = {
    'ðŸ“ ': '📍',
    'ðŸ ¢ ': '🏢',
    'ðŸ ¢': '🏢'
}

files_to_fix = [
    'components/common/cards.py',
    'pages/02_Market_Prices.py',
    'pages/10_Farmer_Dashboard.py',
    'pages/20_Buyer_Dashboard.py',
    'services/matching_service.py'
]

for fpath in files_to_fix:
    try:
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        for k, v in replacer.items():
            content = content.replace(k, v)
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed {fpath}")
    except Exception as e:
        print(f"Error skipping {fpath}")

