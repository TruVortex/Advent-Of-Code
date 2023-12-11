medicine = open('input', 'r').read().split('\n\n')[1]
print(sum(ch.isupper() for ch in medicine) - medicine.count('Rn') - medicine.count('Ar') - 2 * medicine.count('Y') - 1)
