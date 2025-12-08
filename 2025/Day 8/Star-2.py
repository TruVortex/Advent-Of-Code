from math import dist


def find(x):
    global parent
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    global boxes, parent, sizes, ans
    nx, ny = find(x), find(y)
    if nx != ny:
        if sizes[nx] < sizes[ny]:
            nx, ny = ny, nx
        sizes[nx] += sizes[ny]
        parent[ny] = nx
        ans = boxes[x][0] * boxes[y][0]


boxes, distances = [tuple(map(int, line.split(','))) for line in open('input', 'r')], []
parent, sizes, ans = [i for i in range(len(boxes))], [1] * len(boxes), -1
for i, box1 in enumerate(boxes):
    for j in range(i + 1, len(boxes)):
        distances.append((dist(box1, boxes[j]), i, j))
for distance in sorted(distances):
    union(distance[1], distance[2])
print(ans)
