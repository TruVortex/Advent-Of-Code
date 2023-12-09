import re

password = [ord(char) - ord('a') for char in None]
while True:
    values = password.copy()
    values[-1] += 1
    idx = len(values) - 1
    while idx >= 1 and values[idx] == 26:
        values[idx] = 0
        values[idx - 1] += 1
        idx -= 1
    password = values
    if any(password[i - 2] + 2 == password[i - 1] + 1 == password[i] for i in range(2, len(password))) and all(char not in password for char in [8, 11, 14]) and len(re.findall(r'(.)\1', ''.join(chr(char + ord('a')) for char in password))) >= 2:
        print(''.join(chr(char + ord('a')) for char in password))
        break
