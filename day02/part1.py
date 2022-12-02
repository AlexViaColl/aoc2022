OPPONENT_MAP = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors'}
PLAYER_MAP = {'X': 'Rock', 'Y': 'Paper', 'Z': 'Scissors'}

def solve(s):
    n = 0
    for l in s.splitlines():
        opponent, player = l.split()
        opponent = OPPONENT_MAP[opponent]
        player = PLAYER_MAP[player]
        if opponent == 'Rock':
            if player == 'Rock':
                n += 3
            elif player == 'Paper':
                n += 6
            elif player == 'Scissors':
                n += 0
        elif opponent == 'Paper':
            if player == 'Rock':
                n += 0
            elif player == 'Paper':
                n += 3
            elif player == 'Scissors':
                n += 6
        elif opponent == 'Scissors':
            if player == 'Rock':
                n += 6
            elif player == 'Paper':
                n += 0
            elif player == 'Scissors':
                n += 3

        if player == 'Rock':
            n += 1
        elif player == 'Paper':
            n += 2
        elif player == 'Scissors':
            n += 3

    return n

def main():
    with open('input.txt') as f:
        print(solve(f.read()))

if __name__ == '__main__':
    main()
