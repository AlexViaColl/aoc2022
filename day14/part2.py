SOURCE = (500,0)

def solve(s):
    lines = s.splitlines()
    blocks = {}
    max_y = 0
    for l in lines:
        parts = l.split(' -> ')
        prev_part = None
        for p in parts:
            x,y = p.split(',')
            x = int(x)
            y = int(y)
            if y > max_y:
                max_y = y
            if prev_part == None:
                prev_part = (x, y)
                continue
            if prev_part[0] == x:
                start = min(prev_part[1], y)
                end = max(prev_part[1], y)
                for row in range(start, end+1):
                    blocks[(x, row)] = True
            elif prev_part[1] == y:
                start = min(prev_part[0], x)
                end = max(prev_part[0], x)
                for col in range(start, end+1):
                    blocks[(col, y)] = True
            else:
                assert False, f'Unreachable prev_part: {prev_part}, x: {x}, y: {y}'
            prev_part = (x, y)
    ground = max_y + 2

    n = 0
    done = False
    while not done:
        sand = SOURCE
        if SOURCE in blocks:
            break
        while True:
            assert sand not in blocks, f'sand: {sand}'
            if sand[1] == ground - 1:
                n += 1
                blocks[sand] = True # comes to rest
                break

            if (sand[0], sand[1]+1) not in blocks:
                sand = (sand[0], sand[1]+1)
            elif (sand[0]-1, sand[1]+1) not in blocks:
                sand = (sand[0]-1, sand[1]+1)
            elif (sand[0]+1, sand[1]+1) not in blocks:
                sand = (sand[0]+1, sand[1]+1)
            else:
                n += 1
                blocks[sand] = True # comes to rest
                break
    return n

def main():
    with open('input.txt') as f:
        print(solve(f.read()))

if __name__ == '__main__':
    main()
