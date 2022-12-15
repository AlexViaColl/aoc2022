MAX_COORD = 4000000

def merge_intervals(intervals):
    intervals.sort()
    start = max(0, intervals[0][0])
    end = min(intervals[0][1], MAX_COORD)
    for interval in intervals:
        istart, iend = interval
        if istart < start  and iend >= start:
            start = max(0, istart)
        if iend > end and istart <= end:
            end = min(iend, MAX_COORD)
    return end-start+1

def check_row(row, sensors, beacons, get_cells=False):
    cells = {}
    intervals = []
    for (sensor, beacon) in zip(sensors, beacons):
        mht = abs(beacon[0] - sensor[0]) + abs(beacon[1] - sensor[1])
        if row >= sensor[1] - mht and row <= sensor[1] + mht:
            if sensor[1] == row:
                d = 0
            elif sensor[1] < row:
                d = row - sensor[1]
            elif sensor[1] > row:
                d = sensor[1] - row
            start = sensor[0]-mht+d
            end = sensor[0]+mht-d
            intervals.append((start, end))

    return merge_intervals(intervals)

def parse(s):
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
    return sensors, beacons

def solve(s):
    sensors, beacons = parse(s)
    for y in range(MAX_COORD+1):
        x = check_row(y, sensors, beacons)
        if x == MAX_COORD + 1:
            continue

        return x * MAX_COORD + y

def main():
    print("This might take a while...")
    with open('input.txt') as f:
        print(solve(f.read()))

if __name__ == '__main__':
    main()
