from collections import defaultdict
from itertools import combinations
lines = open("data/day8.txt","r").read().split("\n")

nodes = defaultdict(set)
all_nodes = set()
for iy, row in enumerate(lines):
    for ix, elem in enumerate(row):
        if elem != ".":
            nodes[elem].add((iy,ix))
            all_nodes.add((iy,ix))
      
def in_bounds(iy,ix):
    if iy <0 or iy >= len(lines):
        return False
    elif ix < 0 or ix >= len(lines[0]):
        return False
    return True      
      
antis = set()
for node_name, locs in nodes.items():
    combos = list(combinations(locs,2) )
    for combo in combos:
        dy, dx = combo[0][0] - combo[1][0], combo[0][1] - combo[1][1]
        
        in_bounds_ = True
        ix=1
        while in_bounds_:
            pot1 = (combo[0][0] + ix*dy, combo[0][1] + ix*dx)
            in_bounds_ = in_bounds(*pot1)
            if in_bounds_:
                antis.add(pot1)
            ix+=1
                
        in_bounds_ = True
        ix=1
        while in_bounds_:
            pot2 = (combo[1][0] - ix*dy, combo[1][1] - ix*dx)
            in_bounds_ = in_bounds(*pot2)
            if in_bounds_:
                antis.add(pot2)
            ix+=1
                
    
       
print("pt2",len(antis.union(all_nodes))) 


    