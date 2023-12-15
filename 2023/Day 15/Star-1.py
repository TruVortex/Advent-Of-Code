def hash_fun(s):
    value = 0
    for ch in s:
        value = ((value + ord(ch)) * 17) % 256
    return value


print(sum(hash_fun(step) for step in open('input', 'r').read().split(',')))
