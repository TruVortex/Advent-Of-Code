from math import dist, prod


def find(x):
    global parent
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    global parent, sizes
    x, y = find(x), find(y)
    if x != y:
        if sizes[x] < sizes[y]:
            x, y = y, x
        sizes[x] += sizes[y]
        parent[y], sizes[y] = x, 0


boxes, distances = [tuple(map(int, line.split(','))) for line in open('input', 'r')], []
parent, sizes = [i for i in range(len(boxes))], [1] * len(boxes)
for i, box1 in enumerate(boxes):
    for j in range(i + 1, len(boxes)):
        distances.append((dist(box1, boxes[j]), i, j))
for distance in sorted(distances)[:1000]:
    union(distance[1], distance[2])
print(prod(sorted(sizes)[-3:]))
