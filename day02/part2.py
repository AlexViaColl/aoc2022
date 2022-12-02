OPPONENT_MAP = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors'}

def solve(s):
    n = 0
    for l in s.splitlines():
        opponent, player = l.split()
        opponent = OPPONENT_MAP[opponent]
        if opponent == 'Rock':
            if player == 'X':
                n += 0
                n += 3
            elif player == 'Y':
                n += 3
                n += 1
            elif player == 'Z':
                n += 6
                n += 2
        elif opponent == 'Paper':
            if player == 'X':
                n += 0
                n += 1
            elif player == 'Y':
                n += 3
                n += 2
            elif player == 'Z':
                n += 6
                n += 3
        elif opponent == 'Scissors':
            if player == 'X':
                n += 0
                n += 2
            elif player == 'Y':
                n += 3
                n += 3
            elif player == 'Z':
                n += 6
                n += 1

    return n

def main():
    with open('input.txt') as f:
        print(solve(f.read()))

if __name__ == '__main__':
    main()
