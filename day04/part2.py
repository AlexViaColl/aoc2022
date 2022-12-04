def solve(s):
    n = 0
    for l in s.splitlines():
        p1, p2 = l.split(',')
        s1, e1 = map(int, p1.split('-'))
        s2, e2 = map(int, p2.split('-'))
        if (s2 >= s1 and s2 <= e1) or (s1 >= s2 and s1 <= e2):
            n += 1
    return n

def main():
    with open('input.txt') as f:
        print(solve(f.read()))

if __name__ == '__main__':
    main()
