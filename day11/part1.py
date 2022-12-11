def solve(s):
    monkeys = s.split('\n\n')
    monkeys_data = []
    inspection_times = [0]*len(monkeys)
    for i, monkey in enumerate(monkeys):
        lines = monkey.splitlines()
        starting_items = list(map(int, lines[1].split(':')[1].strip().split(',')))
        operation = lines[2].split(':')[1].strip().split('=')[1].strip().split()
        test = int(lines[3].split()[-1])
        on_true = int(lines[4].split()[-1])
        on_false = int(lines[5].split()[-1])
        monkeys_data.append({
            'items': starting_items,
            'operation': operation,
            'test': test,
            'on_true': on_true,
            'on_false': on_false
        })

    for _ in range(20):
        for i, monkey in enumerate(monkeys_data):
            inspection_times[i] += len(monkey['items'])
            for item in monkey['items']:
                after_op = item
                operation = monkey['operation']
                operand = operation[2]
                if operation[2] == 'old':
                    operand = item
                else:
                    operand = int(operation[2])

                if operation[1] == '*':
                    after_op = item * operand
                elif operation[1] == '/':
                    after_op = item / operand
                elif operation[1] == '+':
                    after_op = item + operand
                after_relief = after_op // 3
                divisible = after_relief % monkey['test'] == 0
                yes_no = "" if divisible else " not"
                monkey_throw = monkey['on_true'] if divisible else monkey['on_false']
                monkeys_data[i]['items'] = []
                monkeys_data[monkey_throw]['items'].append(after_relief)

    inspection_times.sort(reverse=True)
    return inspection_times[0] * inspection_times[1]

def main():
    with open('input.txt') as f:
        print(solve(f.read()))

if __name__ == '__main__':
    main()
