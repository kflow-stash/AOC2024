from itertools import cycle
from collections import defaultdict
from copy import copy, deepcopy
grid = open("data/day6.txt","r").read().split("\n")

blocks = set()

dir_map = {">":(0,1),"v":(1,0),"<":(0,-1),"^":(-1,0)}
dir_cycle = cycle(dir_map.values())

for iy, row in enumerate(grid):
    for ix, elem in enumerate(row):
        if elem in ( ">","<","^","v"):
            initial_guard = (iy,ix)
            initial_dir_ = dir_map[elem]
            while True:
                if next(dir_cycle) == initial_dir_:
                    break
                
        elif elem == "#":
            blocks.add((iy,ix))
      
 

def in_bounds(loc_):
    if loc_[0] < 0 or loc_[0] >= len(grid) or loc_[1] < 0 or loc_[1] >= len(grid[0]):
        return False
    return True
        

def walk(loc_: tuple, dir_: tuple, blocks_: set):
    global visited, dir_cycle
    while True:
        if dir_ in visited[loc_]: # check if this loc and dir has already been visited
            return 1
        visited[loc_].add(dir_) # start by logging the current location and direction
        prospect = (loc_[0]+dir_[0],loc_[1]+dir_[1])
        if prospect in blocks_:
            dir_ = next(dir_cycle)
        else:
            if in_bounds(prospect):
                loc_ = prospect # take a straight step

            else:
                return 0
                
            
visited = defaultdict(set)     
loop = walk(initial_guard, copy(initial_dir_), deepcopy(blocks))
        
        
print("pt1",len([x for x,y in visited.items() if len(y)>0]))

cand_blocks = [(iy,ix) for ix in range(len(grid[0])) for iy in range(len(grid)) if (iy,ix) not in blocks and (iy,ix) != initial_guard]

print(f"number of candidates: {len(cand_blocks)}")

loops = 0
for ix, cand_loc in enumerate(cand_blocks):
    visited = defaultdict(set)  
    while True:
        if next(dir_cycle) == initial_dir_:
            break
    if ix % 1000 == 0:
        print(ix, loops)
    new_blocks = deepcopy(blocks)
    new_blocks.add(cand_loc)
    loops += walk(initial_guard, copy(initial_dir_), new_blocks)
    

print("pt2",loops)

        