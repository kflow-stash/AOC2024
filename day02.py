import math

input_ = open("data/day2.txt", "r").read().split("\n")

rows = [list(map(int, x.split())) for x in input_]


def is_safe(row):
    diffs = [x - y for x, y in zip(row[1:], row[:-1])]

    if min([abs(x) for x in diffs]) < 1 or max([abs(x) for x in diffs]) > 3:
        return 0
    elif (not all([x > 0 for x in diffs])) and (not all([x < 0 for x in diffs])):
        return 0

    return 1


safe_count = 0
for row in rows:
    safe_count += is_safe(row)

print("pt1", safe_count)

safe_count = 0
for row in rows:
    safe_list = []
    safe_list.append(is_safe(row))
    for ix in range(len(row)):
        row_copy = row.copy()
        row_copy.pop(ix)
        safe_list.append(is_safe(row_copy))

    safe_count += max(safe_list)

print("pt2", safe_count)
stop_here = 1
