import functools

def is_list(x):
    return x.startswith('[')

def get_list_items(l):
    l = l[1:-1]
    items = []

    parsing_item = False
    cur_item = ''
    
    parsing_list = False
    cur_list = ''
    depth = 0
    for c in l:
        if c == ',':
            # Item separator
            if parsing_item:
                items.append(cur_item)
                cur_item = ''
                parsing_item = False
            elif parsing_list:
                cur_list += c
            else:
                pass
        elif c == '[':
            if parsing_item:
                assert False, 'Unreachable'
            elif parsing_list:
                cur_list += c
                depth += 1
            else:
                parsing_list = True
                cur_list += c
        elif c == ']':
            if parsing_item:
                assert False, 'Unreachable'
            elif parsing_list:
                if depth == 0:
                    cur_list += c
                    items.append(cur_list)
                    cur_list = ''
                    parsing_list = False
                else:
                    depth -= 1
                    cur_list += c
            else:
                assert False, f'Unreachable l={l}'
        else:
            # digit
            if parsing_item:
                cur_item += c
            elif parsing_list:
                cur_list += c
            else:
                parsing_item = True
                cur_item = c
    if cur_item != '':
        items.append(cur_item)
    if cur_list != '':
        items.append(cur_list)
    return items

def are_ordered(left, right):
    if is_list(left) and is_list(right):
        # Compare each value of each list
        l = get_list_items(left)
        r = get_list_items(right)
        min_len = min(len(l), len(r))
        for i in range(min_len):
            ordering = are_ordered(l[i], r[i])
            if ordering < 0:
                return -1
            elif ordering > 0:
                return 1
        if len(l) < len(r):
            return -1
        elif len(l) > len(r):
            return 1
        else:
            return 0
    elif not is_list(left) and not is_list(right):
        l = int(left)
        r = int(right)
        if l < r:
            return -1
        elif l > r:
            return 1
        else:
            return 0
    elif not is_list(left):
        # Convert left to list
        return are_ordered(f'[{left}]', right)
    elif not is_list(right):
        # Convert right to list
        return are_ordered(left, f'[{right}]')
    assert False, 'Unreachable'

def solve(s):
    packets = list(filter(lambda l: len(l.strip()) != 0, s.splitlines()))
    packets.append('[[2]]')
    packets.append('[[6]]')
    packets.sort(key=functools.cmp_to_key(are_ordered))
    n = 1
    for i, p in enumerate(packets):
        if p == '[[2]]' or p == '[[6]]':
            n *= i+1
    return n

def main():
    with open('input.txt') as f:
        print(solve(f.read()))

if __name__ == '__main__':
    main()
