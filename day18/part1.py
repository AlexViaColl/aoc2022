def solve(s):
    n = 0
    cubes = {}
    lines = s.splitlines()
    for l in lines:
        x,y,z = l.split(',')
        x = int(x)
        y = int(y)
        z = int(z)
        cubes[(x,y,z)] = True

    for x,y,z in cubes:
        sides = 6
        if (x-1,y,z) in cubes:
            sides -= 1
        if (x+1,y,z) in cubes:
            sides -= 1
        if (x,y-1,z) in cubes:
            sides -= 1
        if (x,y+1,z) in cubes:
            sides -= 1
        if (x,y,z-1) in cubes:
            sides -= 1
        if (x,y,z+1) in cubes:
            sides -= 1
        cubes[(x,y,z)] = True
        n += sides
    return n

def main():
    with open('input.txt') as f:
        print(solve(f.read()))

if __name__ == '__main__':
    main()
