from hashlib import md5

key = None
for i in range(100000000):
    if md5(f'{key}{i}'.encode('utf-8')).hexdigest()[:5] == '00000':
        print(i)
        break
