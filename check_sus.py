import glob

files_to_fix = glob.glob('components/**/*.py', recursive=True) + glob.glob('pages/*.py')
suspicious = ['\x8d', '\x8f', '\x9d', '\x90', '¢', 'ï', 'â', '¸', 'Ã', 'Å', 'Â']

for fpath in files_to_fix:
    with open(fpath, 'r', encoding='utf-8') as f:
        text = f.read()
    
    for c in suspicious:
        if c in text:
            print(f"File {fpath} contains suspicious char: {repr(c)}")
