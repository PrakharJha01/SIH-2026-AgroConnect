def deep_fix(line):
    current = line
    for _ in range(3):
        try:
            if 'Ã°' in current or 'ð' in current:
                current = current.encode('cp1252').decode('utf-8')
            else:
                break
        except Exception:
            break
    return current

import glob
for fpath in glob.glob('pages/*.py') + glob.glob('components/common/*.py'):
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    lines = content.split('\n')
    new_lines = []
    changed = False
    for line in lines:
        fixed = deep_fix(line)
        if fixed != line:
            changed = True
        new_lines.append(fixed)
    
    if changed:
        print(f"Fixed {fpath}")
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write('\n'.join(new_lines))
