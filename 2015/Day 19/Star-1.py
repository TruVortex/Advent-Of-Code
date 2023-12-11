conversions, medicine = open('input', 'r').read().split('\n\n')
distinct, medicine = set(), medicine.strip() + 'Q'
for conversion in conversions.split('\n'):
    before, after = conversion.strip().split(' => ')
    if before[0].isupper():
        for i in range(len(before), len(medicine)):
            if medicine[i - len(before):i] == before and medicine[i].isupper():
                distinct.add(medicine[:i - len(before)] + after + medicine[i:])
print(len(distinct))
