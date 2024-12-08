from collections import defaultdict

grid, antennas, nodes = [list(line.strip()) for line in open('input', 'r')], defaultdict(list), set()
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] != '.':
            antennas[grid[r][c]].append((r, c))
for antenna in antennas:
    for r1, c1 in antennas[antenna]:
        for r2, c2 in antennas[antenna]:
            if (r1 != r2 or c1 != c2) and 0 <= r1 - (r2 - r1) < len(grid) and 0 <= c1 - (c2 - c1) < len(grid[0]):
                nodes.add((r1 - (r2 - r1), c1 - (c2 - c1)))
print(len(nodes))
