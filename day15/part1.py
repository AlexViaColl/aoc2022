def check_row(row, sensors, beacons):
    cells = {}
    for (sensor, beacon) in zip(sensors, beacons):
        mht = abs(beacon[0] - sensor[0]) + abs(beacon[1] - sensor[1])
        if row >= sensor[1] - mht and row <= sensor[1] + mht:
            # compute occupied cells at row
            if sensor[1] == row:
                d = 0
            elif sensor[1] < row:
                d = row - sensor[1]
            elif sensor[1] > row:
                d = sensor[1] - row
            for x in range(sensor[0]-mht+d, sensor[0]+mht-d+1):
                cells[x] = True
    return len(cells) - 1


def solve(s):
    lines = s.splitlines()
    sensors = []
    beacons = []
    for l in lines:
        _, _, sx, sy, _, _, _, _, bx, by = l.split()
        sx = int(sx.replace('x=','').replace(',',''))
        sy = int(sy.replace('y=','').replace(':',''))
        bx = int(bx.replace('x=','').replace(',',''))
        by = int(by.replace('y=','').replace(':',''))
        sensors.append((sx, sy))
        beacons.append((bx, by))

    return check_row(2000000, sensors, beacons)

def main():
    with open('input.txt') as f:
        print(solve(f.read()))

if __name__ == '__main__':
    main()
