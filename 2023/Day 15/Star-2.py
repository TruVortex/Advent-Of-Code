def hash_fun(s):
    value = 0
    for ch in s:
        value = ((value + ord(ch)) * 17) % 256
    return value


boxes = [[] for i in range(256)]
for operation in open('input', 'r').read().split(','):
    if '-' in operation:
        for box in boxes:
            for i in range(len(box)):
                if box[i][0] == operation[:-1]:
                    box.pop(i)
                    break
    else:
        replace = False
        for box in boxes:
            for i in range(len(box)):
                if box[i][0] == operation[:operation.find('=')]:
                    box[i] = operation.split('=')
                    replace = True
                    break
        if not replace:
            boxes[hash_fun(operation[:operation.find('=')])].append(operation.split('='))
summate = 0
for i, box in enumerate(boxes):
    for j, lens in enumerate(box):
        print(i + 1, j + 1, lens)
        summate += (i + 1) * (j + 1) * int(lens[1])
print(summate)
