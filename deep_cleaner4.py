import glob

files_to_fix = glob.glob('components/**/*.py', recursive=True) + glob.glob('pages/*.py')
chars = set()

for fpath in files_to_fix:
    with open(fpath, 'r', encoding='utf-8') as f:
        text = f.read()
    
    for c in text:
        if ord(c) > 127:
            chars.add(c)

print(repr(''.join(list(chars))))
