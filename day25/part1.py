def snafu(n):
    s = []
    while n > 0:
        rem = n % 5
        n = n // 5
        s.insert(0, str(rem))

    for i in range(len(s)-1, -1, -1):
        if s[i] == '3':
            s[i] = '='
            s[i-1] = chr(ord(s[i-1]) + 1)
        elif s[i] == '4':
            s[i] = '-'
            s[i-1] = chr(ord(s[i-1]) + 1)
        elif s[i] == '5':
            s[i] = '0'
            s[i-1] = chr(ord(s[i-1]) + 1)
    return ''.join(s)

def solve(s):
    n = 0
    lines = s.splitlines()
    for line in lines:
        line = line.strip()
        for i, c in enumerate(line):
            power = len(line) - i - 1
            val = {'0': 0, '1': 1, '2': 2, '-': -1, '=': -2}[c]
            x = val * 5**power
            n += x
    return snafu(n)

def main():
    with open('input.txt') as f:
        print(solve(f.read()))

if __name__ == '__main__':
    main()
