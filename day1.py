from collections import Counter

input_lines = open("data/day1_pt1.txt","r").read().split("\n")

left_list = [int(x.split()[0]) for x in input_lines]
right_list = [int(x.split()[1]) for x in input_lines]

left_sorted = sorted(left_list)
right_sorted= sorted(right_list)

pt1 = sum([abs(x-y) for x,y in zip(left_sorted,right_sorted)])

print(pt1)

right_counts = Counter(right_list)
pt2 = sum([x*right_counts.get(x,0) for x in left_list])

print(pt2)