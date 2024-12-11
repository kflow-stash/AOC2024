
from copy import deepcopy
map_ = [list(map(int,row)) for row in open("data/day10.txt","r").read().split("\n")]

dirs = [(1,0),(0,-1),(-1,0),(0,1)]

trailheads = []
for iy, row in enumerate(map_):
    for ix, elem in enumerate(row):
        if map_[iy][ix] == 0:
            trailheads.append((iy,ix))
     
def in_bounds(iy,ix):
    if iy<0 or iy >= len(map_) or ix<0 or ix>=len(map_[0]):
        return False
    return True
     
def trace(loc, val, nines:set, path:set):

    path.add(loc)
    if val == 9:
        nines.add(frozenset(path))
        return nines
    for dir in dirs:
        new_loc = (loc[0]+dir[0],loc[1]+dir[1])
        if in_bounds(*new_loc) and map_[new_loc[0]][new_loc[1]] == val +1:
            res = trace(new_loc,val+1,nines,deepcopy(path))
            nines.union(res)
                
    return nines

scores = []      
for ix,th in enumerate(trailheads):
    if ix % 100 == 0:
        print("trailhead",ix)
    nines = set()
    path = set()
    nines = trace(th, 0, nines, path)
    
    scores.append(len(nines))
    
print("pt2",sum(scores))
