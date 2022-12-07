import os

def solve(s):
    current_dir = ''
    sizes = {}
    for l in s.splitlines():
        if l.startswith('$'):
            if l.startswith('$ ls'):
                pass
            else:
                _, _, segment = l.split()
                current_dir = os.path.realpath(os.path.join(current_dir, segment))
        else:
            if l.startswith('dir'):
                pass
            else:
                size, _ = l.split()
                size = int(size)
                if not current_dir in sizes:
                    sizes[current_dir] = size
                else:
                    sizes[current_dir] += size

                if current_dir != '/':
                    sizes['/'] += size

                p = current_dir
                while p != '/' and p != '':
                    p = '/'.join(p.split('/')[:-1])
                    if p == '':
                        break
                    if not p in sizes:
                        sizes[p] = size
                    else:
                        sizes[p] += size

    unused = 70000000 - sizes['/']
    free_required = 30000000 - unused

    n = sizes['/']
    for k in sizes:
        if sizes[k] >= free_required and sizes[k] < n:
            n = sizes[k]

    return n

def main():
    with open('input.txt') as f:
        print(solve(f.read()))

if __name__ == '__main__':
    main()
