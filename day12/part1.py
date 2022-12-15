import heapq

def get_possibles(grid, node):
    nrows = len(grid)
    ncols = len(grid[0])
    cost, pos = node
    y, x = pos
    current_value = grid[y][x]
    possibles = []
    if x > 0:
        next_value = grid[y][x-1]
        if next_value <= current_value + 1:
            possibles.append((cost + 1, (y, x-1)))
    if x < ncols - 1:
        next_value = grid[y][x+1]
        if next_value <= current_value + 1:
            possibles.append((cost + 1, (y, x+1)))
    if y > 0:
        next_value = grid[y-1][x]
        if next_value <= current_value + 1:
            possibles.append((cost + 1, (y-1, x)))
    if y < nrows - 1:
        next_value = grid[y+1][x]
        if next_value <= current_value + 1:
            possibles.append((cost + 1, (y+1, x)))
    return possibles


def solve(s):
    lines = s.splitlines()
    grid = []
    for y, line in enumerate(lines):
        grid_line = []
        for x, c in enumerate(line):
            if c == 'S':
                start = (y, x)
                grid_line.append(0)
            elif c == 'E':
                goal = (y, x)
                grid_line.append(25)
            else:
                grid_line.append(ord(c)-ord('a'))
        grid.append(grid_line)

    pq = []
    visited = [start]
    heapq.heappush(pq, (0, start))
    
    node = heapq.heappop(pq)
    while node != None:
        if node[1] == goal:
            break

        for possible in get_possibles(grid, node):
            if possible[1] not in visited:
                heapq.heappush(pq, possible)
                visited.append(possible[1])
        
        if len(pq) > 0:
            node = heapq.heappop(pq)
        else:
            break

    return node[0]

def main():
    with open('input.txt') as f:
        print(solve(f.read()))

if __name__ == '__main__':
    main()
