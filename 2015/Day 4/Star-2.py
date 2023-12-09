from hashlib import md5

key = 'iwrupvqb'
for i in range(100000000):
    if md5(f'{key}{i}'.encode('utf-8')).hexdigest()[:6] == '000000':
        print(i)
        break
