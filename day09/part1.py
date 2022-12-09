import math

def update_tail(head, tail, direction):
    d = (tail[0] - head[0], tail[1] - head[1])
    dist = math.sqrt(d[0]*d[0] + d[1]*d[1])
    if dist > math.sqrt(2):
        if direction == 'R':
            return (head[0] - 1, head[1])
        elif direction == 'L':
            return (head[0] + 1, head[1])
        elif direction == 'U':
            return (head[0], head[1] - 1)
        elif direction == 'D':
            return (head[0], head[1] + 1)
    else:
        return tail

def solve(s):
    head = (0, 0)
    tail = (0, 0)
    visited = {}
    for l in s.splitlines():
        direction, steps = l.split()
        steps = int(steps)
        for _ in range(steps):
            if direction == 'R':
                head = (head[0] + 1, head[1])
            elif direction == 'L':
                head = (head[0] - 1, head[1])
            elif direction == 'U':
                head = (head[0], head[1] + 1)
            elif direction == 'D':
                head = (head[0], head[1] - 1)
            tail = update_tail(head, tail, direction)
            visited[tail] = 1
    return len(visited)

def main():
    with open('input.txt') as f:
        print(solve(f.read()))

if __name__ == '__main__':
    main()
