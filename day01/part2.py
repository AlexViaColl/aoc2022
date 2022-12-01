def solve(s):
    calories = 0
    calories_list = []
    for l in s.splitlines():
        l = l.strip()
        if l == '':
            calories_list.append(calories)
            calories = 0
        else:
            calories += int(l.strip())

    calories_list.sort(reverse=True)
    return sum(calories_list[:3])

def main():
    with open('input.txt') as f:
        print(solve(f.read()))

if __name__ == '__main__':
    main()
