from copy import  deepcopy

grid_, instructs = open("data/day15.txt", "r").read().split("\n\n")
grid_ = grid_.split("\n")

vec_map={"v":(1,0),"<":(0,-1),">":(0,1),"^":(-1,0)}

walls=set()
blocks=set()
for iy, row in enumerate(grid_):
    ix = 0
    for elem in row:
        if elem == "#":
            walls.add((iy,ix))
            walls.add((iy,ix+1))
        elif elem == "O":
            blocks.add(frozenset([(iy,ix),(iy,ix+1)]))
        elif elem == "@":
            loc_ = (iy,ix)
            
        ix += 2
    
blocks_all = set(x for block in blocks for x in block)
            
def push(start_block, vec):
    global blocks, blocks_all
    block_mass = deepcopy(start_block) # should start with a set of length 2 ((y1,x1),(y2,x2))
    while True:
        moved_block_mass = set((x[0]+vec[0], x[1]+vec[1]) for x in block_mass)
        if any([x in walls for x in moved_block_mass]):
            #a part of the block mass hit a wall on the last step
            return False
        
        else:
            pushed_mass = blocks_all.intersection(moved_block_mass)
            pushed_mass = set(loc_ for x in blocks for loc_ in x if x.intersection(pushed_mass)).union(block_mass)
            
            if pushed_mass != block_mass:
                #found some new blocks to push - get the full set of found occupied block locations
                block_mass = deepcopy(pushed_mass)
            else:
                #successfully pushed the mass
                
                old_block_locs = list(sorted(list(block_mass)))
                old_blocks = set(frozenset([old_block_locs[ix],old_block_locs[ix+1]]) for ix in range(0,len(old_block_locs),2))
                
                new_block_locs = list(sorted(list(moved_block_mass)))
                new_blocks = set(frozenset([new_block_locs[ix],new_block_locs[ix+1]]) for ix in range(0,len(new_block_locs),2))
                blocks = blocks.difference(old_blocks)
                blocks = blocks.union(new_blocks)
                
                blocks_all = set(x for block in blocks for x in block)
                
                return True
                

for instruct in [x for x in instructs if x != "\n"]:
    vec = vec_map[instruct]
    step = (loc_[0] + vec[0], loc_[1] + vec[1])
    if step in walls:
        continue
    elif step in blocks_all:
        block = next(x for x in blocks if step in x)
        pushed = push(block, vec)
        if pushed:
            loc_ = step
    else:
        loc_ = step

sorted_blocks = list(sorted(list(blocks_all)))

left_blocks = [sorted_blocks[ix] for ix in range(0,len(sorted_blocks),2)]
        
score = sum([100*y + x for y,x in left_blocks])

print("pt2",score)