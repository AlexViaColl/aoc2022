import math

def update_tail(head, tail, direction):
    d = (tail[0] - head[0], tail[1] - head[1])
    dist = math.sqrt(d[0]*d[0] + d[1]*d[1])
    if dist == 2:
        return (math.floor(tail[0]*0.5 + head[0]*0.5), math.floor(tail[1]*0.5 + head[1]*0.5))
    elif dist > math.sqrt(2):
        if head[0] > tail[0] and head[1] > tail[1]:
            return (tail[0]+1, tail[1]+1)
        elif head[0] > tail[0] and head[1] < tail[1]:
            return (tail[0]+1, tail[1]-1)
        elif head[0] < tail[0] and head[1] > tail[1]:
            return (tail[0]-1, tail[1]+1)
        elif head[0] < tail[0] and head[1] < tail[1]:
            return (tail[0]-1, tail[1]-1)
        else:
            raise
    else:
        return tail

def update_rope(rope, direction):
    for i in range(9):
        rope[i + 1] = update_tail(rope[i], rope[i + 1], direction)
    return rope

def solve(s):
    rope = []
    for i in range(10):
        rope.append((0, 0))
    visited = {}
    for l in s.splitlines():
        direction, steps = l.split()
        steps = int(steps)
        for _ in range(steps):
            head = rope[0]
            if direction == 'R':
                rope[0] = (head[0] + 1, head[1])
            elif direction == 'L':
                rope[0] = (head[0] - 1, head[1])
            elif direction == 'U':
                rope[0] = (head[0], head[1] + 1)
            elif direction == 'D':
                rope[0] = (head[0], head[1] - 1)
            rope = update_rope(rope, direction)
            visited[rope[-1]] = 1
    return len(visited)

def main():
    with open('input.txt') as f:
        print(solve(f.read()))

if __name__ == '__main__':
    main()
