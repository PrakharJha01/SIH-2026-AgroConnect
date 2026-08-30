
with open('app.py', 'rb') as f:
    text = f.read().decode('utf-8', errors='ignore')

# Fix known mojibake manually
text = text.replace('ðŸ  ', '??')
text = text.replace('ðŸ  ', '??')
text = text.replace('ðŸ¤ ', '??')

with open('app.py', 'w', encoding='utf-8') as f:
    f.write(text)

