import os
import glob

def fix_mojibake(text):
    try:
        # If the string was read as CP1252 and written back as UTF-8
        encoded = text.encode('cp1252')
        return encoded.decode('utf-8')
    except Exception:
        # Fallback if that's not exactly what happened
        return text

# Try to find all python files that might have been corrupted
for fpath in glob.glob('pages/*.py') + glob.glob('components/common/*.py'):
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'ð' in content or 'Ã°' in content:
        # There's corruption!
        print(f"Fixing {fpath}")
        lines = content.split('\n')
        new_lines = []
        for line in lines:
            if 'ð' in line or 'Ã°' in line:
                try:
                    fixed_line = line.encode('cp1252').decode('utf-8')
                    new_lines.append(fixed_line)
                except Exception as e:
                    new_lines.append(line)
            else:
                new_lines.append(line)
        
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write('\n'.join(new_lines))

print('Done')
