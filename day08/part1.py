def visible(lines, row, col):
    w = len(lines[0])
    h = len(lines)
    height = lines[row][col]
    visible_left = True
    visible_right = True
    visible_up = True
    visible_down = True
    for i in range(0, col):
        if lines[row][i] >= height:
            visible_left = False
            break
    for i in range(col+1, w):
        if lines[row][i] >= height:
            visible_right = False
            break
    for i in range(0, row):
        if lines[i][col] >= height:
            visible_up = False
            break
    for i in range(row+1, h):
        if lines[i][col] >= height:
            visible_down = False
            break
    return visible_left or visible_right or visible_up or visible_down

def solve(s):
    lines = s.splitlines()
    w = len(lines[0])
    h = len(lines)
    n = w*2 + h*2 - 4
    for row in range(1, h - 1):
        for col in range(1, w - 1):
            if visible(lines, row, col):
                n += 1
    return n

def main():
    with open('input.txt') as f:
        print(solve(f.read()))

if __name__ == '__main__':
    main()
