from collections import defaultdict
import time
input_ = open("data/day9.txt","r").read()


file_dict = defaultdict(lambda: 0)
group_dict = {}
empties = []
empty_dict = {}
file_id = 0
start_ix = 0
for ix, x in enumerate(input_):
    if ix % 2 == 0:
        file_dict.update({iz:file_id for iz in range(start_ix, int(x)+start_ix)})
        group_dict[file_id] = {"start_ix": start_ix, "len": int(x)}
        file_id += 1
    else:
        empties.extend(list(range(start_ix, int(x)+start_ix)))
        empty_dict[start_ix] = int(x)

    start_ix += int(x)

time0 = time.time()
insertions = {}
empty_space=empties.pop(0)
pt1_dict = file_dict.copy()
while empties and empty_space < max(pt1_dict.keys()):
    _, val = pt1_dict.popitem()
    insertions[empty_space] = val
    empty_space = empties.pop(0)


pt1_dict.update(insertions)   
print("pt1", sum([x*y for x,y in pt1_dict.items()]), "time:", round(time.time() - time0,1))   

time0 = time.time()
insertions = {}
empty_space=empties.pop(0)
for file_id, group in reversed(group_dict.items()):
    for start_ix, empty_size in sorted(empty_dict.items()):
        if empty_size >= group["len"] and start_ix < group["start_ix"]:
            insertions.update({iz:file_id for iz in range(start_ix, start_ix + group["len"]) })
            [file_dict.pop(iz) for iz in range(group["start_ix"], group["start_ix"] + group["len"])]
            empty_dict.pop(start_ix)
            if empty_size > group["len"]:
                empty_dict[start_ix+group["len"]] = empty_size - group["len"]

            break
   
file_dict.update(insertions)             
print("pt2", sum([x*y for x,y in file_dict.items()]), "time:", round(time.time() - time0,1))  

