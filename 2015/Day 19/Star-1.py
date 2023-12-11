conversions, medicine = open('input', 'r').read().split('\n\n')
distinct, medicine = set(), medicine.strip() + 'Q'
for conversion in conversions.split('\n'):
    before, after = conversion.strip().split(' => ')
    for i in range(len(before), len(medicine)):
        if medicine[i - len(before):i] == before:
            distinct.add(medicine[:i - len(before)] + after + medicine[i:])
print(len(distinct))
