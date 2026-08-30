with open('pages/14_Opportunities.py', 'r', encoding='utf-8') as f:
    lines = f.read().split('\n')

new_lines = []
skip = False
for line in lines:
    if 'with st.spinner(' in line and 'Finding matching buyers' in line:
        skip = True
        continue
    if skip and ('matches = find_buyers_for_lot' in line):
        skip = False
        continue
    if '# Update the best-offer metric' in line:
        skip = True
        continue
    if skip and 'best_buyer_name =' in line:
        skip = False
        continue
        
    if not skip:
        new_lines.append(line)

with open('pages/14_Opportunities.py', 'w', encoding='utf-8') as f:
    f.write('\n'.join(new_lines))
