with open('pages/23_Buyer_Matches.py', 'r', encoding='utf-8') as f:
    for line in f:
        if line.startswith('def '):
            print(line.strip())
