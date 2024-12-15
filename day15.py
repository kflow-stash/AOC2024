from copy import copy

grid_, instructs = open("data/day15.txt", "r").read().split("\n\n")
grid_ = grid_.split("\n")

vec_map={"v":(1,0),"<":(0,-1),">":(0,1),"^":(-1,0)}

walls=set()
blocks=set()
for iy, row in enumerate(grid_):
    for ix, elem in enumerate(row):
        if elem == "#":
            walls.add((iy,ix))
        elif elem == "O":
            blocks.add((iy,ix))
        elif elem == "@":
            loc_ = (iy,ix)
            
def push(loc_, vec):
    while True:
        new_loc = (loc_[0]+vec[0], loc_[1]+vec[1])
        if new_loc in walls:
            return False, None
        elif new_loc in blocks:
            loc_ = copy(new_loc)
        else:
            return True, new_loc
            
            
for instruct in [x for x in instructs if x != "\n"]:
    vec = vec_map[instruct]
    step = (loc_[0] + vec[0], loc_[1] + vec[1])
    if step in walls:
        continue
    elif step in blocks:
        pushed, new_block = push(step, vec)
        if pushed:
            blocks.remove(step)
            blocks.add(new_block)
            loc_ = step
    else:
        loc_ = step
        
score = sum([100*y + x for y,x in blocks])

print("pt1",score)