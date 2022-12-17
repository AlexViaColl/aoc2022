WIDTH = 7

def get_max_y(chamber):
    max_y = -1
    for rock in chamber:
        if rock[1] > max_y:
            max_y = rock[1]
    return max_y

def get_rock(chamber, i):
    max_y = get_max_y(chamber) + 1

    if i % 5 == 0:
        return [(2, max_y + 3), (3, max_y + 3), (4, max_y + 3), (5, max_y + 3)]
    elif i % 5 == 1:
        return [
            (3, max_y + 5),
            (2, max_y + 4), (3, max_y + 4), (4, max_y + 4),
            (3, max_y + 3),
        ]
    elif i % 5 == 2:
        return [
            (4, max_y + 5),
            (4, max_y + 4),
            (2, max_y + 3), (3, max_y + 3), (4, max_y + 3),
        ]
    elif i % 5 == 3:
        return [
            (2, max_y + 6),
            (2, max_y + 5),
            (2, max_y + 4),
            (2, max_y + 3),
        ]
    elif i % 5 == 4:
        return [
            (2, max_y + 4), (3, max_y + 4),
            (2, max_y + 3), (3, max_y + 3),
        ]

def push_rock(chamber, rock, jet):
    delta = 1 if jet == '>' else -1
    new_rock = []
    can_move = True
    for i, r in enumerate(rock):
        new_r = (r[0] + delta, r[1])
        if new_r[0] < 0 or new_r[0] >= WIDTH:
            can_move = False
            break
        elif new_r in chamber:
            can_move = False
            break
        new_rock.append(new_r)

    if not can_move:
        return (False, rock)
    return (True, new_rock)

def push_down_rock(chamber, rock):
    new_rock = []
    for i, r in enumerate(rock):
        new_r = (r[0], r[1] - 1)
        #print(new_r)
        if new_r[1] < 0:
            return (False, rock)
        elif new_r in chamber:
            return (False, rock)
        new_rock.append(new_r)
    return (True, new_rock)

def update_chamber(chamber, rock):
    for r in rock:
        chamber[r] = True

def solve(s):
    s = s.strip()
    chamber = {}
    rock_idx = 0
    jet_idx = 0
    while rock_idx != 2022:
        rock = get_rock(chamber, rock_idx)
        while True:
            has_moved = False
            jet = s[jet_idx]
            jet_idx = (jet_idx + 1) % len(s)
            can_move, new_rock = push_rock(chamber, rock, jet)
            if not can_move:
                pass
            else:
                has_moved = True
                rock = new_rock

            can_move, new_rock = push_down_rock(chamber, rock)
            if not can_move:
                update_chamber(chamber, rock)
                break
            else:
                has_moved = True
                rock = new_rock

        rock_idx += 1

    return get_max_y(chamber) + 1

def main():
    with open('input.txt') as f:
        print(solve(f.read()))

if __name__ == '__main__':
    main()
