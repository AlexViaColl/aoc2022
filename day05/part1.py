def solve(s):
    n = ''
    stacks = {}
    parse_crates = True
    stacks_count = 0
    for l in s.splitlines():
        if parse_crates:
            for i,c in enumerate(l):
                if not '[' in l:
                    parse_crates = False
                    numbers = l.split()
                    stacks_count = int(numbers[-1])
                    break

                if i % 4 == 1 and c != ' ':
                    idx = i // 4
                    #print(idx, c)
                    if idx in stacks:
                        stacks[idx].insert(0, c)
                    else:
                        stacks[idx] = [c]

        else:
            if l.startswith('move'):
                _, count, _, src, _, dst = l.split(' ')
                count = int(count)
                src = int(src) - 1
                dst = int(dst) - 1
                for i in range(count):
                    s = stacks[src].pop()
                    stacks[dst].append(s)

    for i in range(stacks_count):
        if len(stacks[i]) > 0:
            n += stacks[i].pop()
    return n

def main():
    with open('input.txt') as f:
        print(solve(f.read()))

if __name__ == '__main__':
    main()
