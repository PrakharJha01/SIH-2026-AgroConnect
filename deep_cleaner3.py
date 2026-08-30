import glob
import re

files_to_fix = glob.glob('components/**/*.py', recursive=True) + glob.glob('pages/*.py')

for fpath in files_to_fix:
    try:
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Just destroy anything between 0xC0 and 0xFF that looks like corruption
        # But wait, python strings are decoded unicode.
        # Let's match the exact string shown in powershell.
        content = re.sub(r'ðŸ“ ', '📍', content)
        content = re.sub(r'ðŸ ¢', '🏢', content)
        content = re.sub(r'â„¹', 'ℹ️', content)
        content = re.sub(r'â€', '', content)
        content = re.sub(r'âš', '⚠️', content)
        content = re.sub(r'ðŸ‘¨', '👨', content)
        content = re.sub(r'ðŸŒ¾', '🌾', content)
        
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Cleaned {fpath}")
    except Exception as e:
        print(f"Error {fpath}: {e}")

