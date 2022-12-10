def crt_to_str(crt):
    lines = crt.splitlines()
    s = ''
    hash_to_char = {
        190: 'F',
        300: 'U',
        330: 'R',
        340: 'E',
        360: 'G',
        # ... hashes for other characters ...
    }
    for i in range(8):
        char_hash = 0
        for line_idx, line in enumerate(lines):
            l = line[i*5:i*5+5]
            char_hash += l.count('#') * line_idx * 10
        s += hash_to_char[char_hash]
    return s

def solve(s):
    X = 1
    lines = s.splitlines()
    in_progress = None
    pending = []
    i = 0
    crt = ''
    while i < len(lines) or len(pending) != 0:
        col = i % 40
        if col >= X - 1 and col <= X + 1:
            crt += '#'
        else:
            crt += ' '

        if (i+1) % 40 == 0:
            crt += '\n'

        if i < len(lines) and len(pending) == 0:
            line = lines[i]
            if line == 'noop':
                if in_progress is None:
                    in_progress = line
                else:
                    pending.insert(0, line)
            else:
                if in_progress is None:
                    in_progress = f'{line} 2'
                else:
                    pending.insert(0, line)
        elif in_progress is None and len(pending) != 0:
            if i < len(lines):
                pending.insert(0, lines[i])
            line = pending.pop()
            if line == 'noop':
                if in_progress is None:
                    in_progress = line
                else:
                    pending.insert(0, line)
            else:
                if in_progress is None:
                    in_progress = f'{line} 2'
                else:
                    pending.insert(0, line)
        elif in_progress != None and i < len(lines):
            line = lines[i]
            pending.insert(0, line)

        # End of Cycle
        if in_progress == 'noop':
            in_progress = None
        elif in_progress != None and 'addx' in in_progress:
            _, amount, cycles = in_progress.split()
            amount = int(amount)
            cycles = int(cycles)
            if cycles == 1:
                X += amount
                in_progress = None
            else:
                in_progress = f'addx {amount} {cycles - 1}'
        else:
            in_progress = pending.pop()

        i += 1

    print(crt)
    return crt_to_str(crt)

def main():
    with open('input.txt') as f:
        print(solve(f.read()))

if __name__ == '__main__':
    main()
