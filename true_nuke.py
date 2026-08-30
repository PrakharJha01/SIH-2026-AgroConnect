import glob
import re

files_to_fix = glob.glob('components/**/*.py', recursive=True) + glob.glob('pages/*.py')

for fpath in files_to_fix:
    with open(fpath, 'r', encoding='utf-8') as f:
        text = f.read()

    # Kill pure mojibake
    text = re.sub(r'[\x8d\x8f\x9d\x90¢ïâ¸ÃÅÂðŸ]+', '', text)
    text = re.sub(r'‍', '', text)
    
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(text)
