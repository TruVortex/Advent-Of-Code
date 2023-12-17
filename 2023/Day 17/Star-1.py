import heapq

grid, vis, pq = [list(map(int, line.strip())) for line in open('input', 'r')], set(), [(0, 0, 0, 0, 0, 0)]
while pq:
    loss, y, x, dy, dx, consecutive = heapq.heappop(pq)
    if y == len(grid) - 1 and x == len(grid[0]) - 1:
        print(loss)
        break
    if (y, x, dy, dx, consecutive) in vis:
        continue
    vis.add((y, x, dy, dx, consecutive))
    if (y, x) != (0, 0) and consecutive < 3 and 0 <= y + dy < len(grid) and 0 <= x + dx < len(grid[0]):
        heapq.heappush(pq, (loss + grid[y + dy][x + dx], y + dy, x + dx, dy, dx, consecutive + 1))
    for ddy, ddx in ((0, -1), (0, 1), (-1, 0), (1, 0)):
        if (ddy, ddx) != (dy, dx) and (ddy, ddx) != (-dy, -dx) and 0 <= y + ddy < len(grid) and 0 <= x + ddx < len(grid[0]):
            heapq.heappush(pq, (loss + grid[y + ddy][x + ddx], y + ddy, x + ddx, ddy, ddx, 1))
