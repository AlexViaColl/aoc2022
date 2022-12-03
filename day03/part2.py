def solve(s):
    n = 0
    lines = s.splitlines()
    for i in range(0, len(lines), 3):
        found = False
        first = lines[i]
        second = lines[i+1]
        third = lines[i+2]
        for x in second:
            if x in first:
                for y in third:
                    if x == y:
                        if x >= 'a' and x <= 'z':
                            n += ord(x) - ord('a') + 1
                        else:
                            n += ord(x) - ord('A') + 27
                        found = True
                        break
            if found:
                break
    return n

def main():
    with open('input.txt') as f:
        print(solve(f.read()))

if __name__ == '__main__':
    main()
