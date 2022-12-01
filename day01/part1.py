def solve(s):
    max_calories = 0
    calories = 0
    for l in s.splitlines():
        l = l.strip()
        if l == '':
            if calories >= max_calories:
                max_calories = calories
            calories = 0
        else:
            calories += int(l.strip())

    return max_calories

def main():
    with open('input.txt') as f:
        print(solve(f.read()))

if __name__ == '__main__':
    main()
