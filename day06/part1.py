def solve(s):
    chars = []
    n = 4
    for i, c in enumerate(s):
        if len(chars) != n - 1:
            chars.append(c)
        else:
            chars.append(c)
            if len(set(chars)) == n:
                return i + 1

            if len(chars) == n:
                chars.pop(0)

def main():
    with open('input.txt') as f:
        print(solve(f.read()))

if __name__ == '__main__':
    main()
