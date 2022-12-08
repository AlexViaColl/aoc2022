def get_score(lines, row, col):
    w = len(lines[0])
    h = len(lines)
    height = lines[row][col]
    left_count = 0
    c = col - 1
    while c >= 0:
        if lines[row][c] < height:
            left_count += 1
        else:
            left_count += 1
            break
        c -= 1
    right_count = 0
    c = col + 1
    while c < w:
        if lines[row][c] < height:
            right_count += 1
        else:
            right_count += 1
            break
        c += 1
    up_count = 0
    r = row - 1
    while r >= 0:
        if lines[r][col] < height:
            up_count += 1
        else:
            up_count += 1
            break
        r -= 1
    down_count = 0
    r = row + 1
    while r < h:
        if lines[r][col] < height:
            down_count += 1
        else:
            down_count += 1
            break
        r += 1
    return left_count*right_count*up_count*down_count


def solve(s):
    lines = s.splitlines()
    w = len(lines[0])
    h = len(lines)
    n = 0
    for row in range(1, h-1):
        for col in range(1, w-1):
            score = get_score(lines, row, col)
            if score > n:
                n = score
    return n

def main():
    with open('input.txt') as f:
        print(solve(f.read()))

if __name__ == '__main__':
    main()
