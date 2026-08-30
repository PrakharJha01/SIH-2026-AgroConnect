import glob

files_to_fix = glob.glob('components/**/*.py', recursive=True) + glob.glob('pages/*.py')

replacements = {
    'ðŸ“\x8d': '📍',
    'ðŸ\x8f¢': '🏢',
    'Â·': '·',
    'â„¹ï¸\x8f': 'ℹ️',
    'â„¹': 'ℹ️',
    'âš\xa0ï¸\x8f': '⚠️',
    'âš\xa0': '⚠️',
    'â†\x90': '←',
    'âœ“': '✓',
    'âœ—': '✗',
    'â‚¹': '₹',
    'ðŸ‘¨' : '👨',
    'ðŸŒ¾' : '🌾',
    'â€‍': '',
    'ð': '',
    'Ÿ': ''
}

for fpath in files_to_fix:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False
    for k, v in replacements.items():
        if k in content:
            content = content.replace(k, v)
            modified = True
            
    if modified:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Cleaned {fpath}")

