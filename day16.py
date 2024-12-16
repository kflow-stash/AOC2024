
import heapq
from sys import maxsize
from copy import copy
from collections import defaultdict
grid_ = open("data/day16.txt", "r").read().splitlines()

vecs = [(0,1),(0,-1),(1,0),(-1,0)]

walls = set()
for iy, row in enumerate(grid_):
    for ix, elem in enumerate(row):
        if elem == "S":
            loc_ = (iy, ix)
        elif elem == "#":
            walls.add((iy,ix))
            
        elif elem == "E":
            dest = (iy,ix)
            
vec = (0,1)

visited = {}
visited_paths = defaultdict(lambda: set)
queue = []
path = set()

path_elements = set()

heapq.heappush(queue,(0,(loc_,vec, path)))
lowest_cost = maxsize

while queue:
    cost, (loc_, vec, path) = heapq.heappop(queue)
    
    if loc_ == dest and cost <= lowest_cost:
        lowest_cost = cost
        path_elements = path_elements.union(set(path))
    elif loc_ == dest:
        break
    
    for v in vecs:
        new_loc = (loc_[0] + v[0], loc_[1] + v[1])
        new_cost = cost + 1 + (0 if v == vec else 1000)
        if new_loc not in walls and new_cost <= lowest_cost:
            if visited.get((new_loc,v),maxsize) >= new_cost:
                new_path = copy(path)
                new_path.add(new_loc)
                visited[(new_loc,v)] = new_cost
                visited_paths[(new_loc,v)] = visited_paths[(new_loc,v)].union(new_path)
                heapq.heappush(queue,(new_cost,(new_loc, v, new_path)))
 
print("pt1",lowest_cost,"pt2",len(path_elements)+1)           

            