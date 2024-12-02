#!/usr/bin/env python
import sys

left = []
right = []
with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        temp = line.split()
        left.append(int(temp[0]))
        right.append(int(temp[-1]))

left.sort()
right.sort()

total = 0
part2_total = 0

for i in range(len(left)):
    total += abs(left[i] - right[i])
    part2_total += left[i] * right.count(left[i])
               #print(total)
print(f"Part 1: {total}")
print(f"Part 2: {part2_total}")

