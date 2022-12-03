def solve(s):
    n = 0
    for l in s.splitlines():
        first = l[:len(l)//2]
        last = l[len(l)//2:]
        for a in last:
            if a in first:
                if a >= 'a' and a <= 'z':
                    n += ord(a) - ord('a') + 1
                else:
                    n += ord(a) - ord('A') + 27
                break
    return n

def main():
    with open('input.txt') as f:
        print(solve(f.read()))

if __name__ == '__main__':
    main()
