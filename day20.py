import heapq
from sys import maxsize
from copy import copy, deepcopy
from collections import defaultdict
grid_ = open("data/day20.txt", "r").read().splitlines()

vecs = [(0,1),(0,-1),(1,0),(-1,0)]

walls = set()
for ix in range(len(grid_[0])+2):
    walls.add((0,ix))
    walls.add((len(grid_)+1,ix))
for iy, row in enumerate(grid_):
    walls.add((iy+1,0))
    walls.add((iy+1,len(row)+1))
    for ix, elem in enumerate(row):
        if elem == "S":
            start = (iy+1, ix+1)
        elif elem == "#":
            walls.add((iy+1,ix+1))
            
        elif elem == "E":
            dest = (iy+1,ix+1)

def draw_map():
    map_ = [["." for _ in range(len(grid_[0])+2)] for _ in range(len(grid_)+2)]
    for wall in walls:
        map_[wall[0]][wall[1]] = "#"
        
    print("\n".join(["".join(row) for row in map_]))
 
 
          


def no_cheat():
    path_heap = []
    initial_visited = [start]

    heapq.heappush(path_heap,(0,(start,initial_visited.copy()))) #cost, location, cheated flag, cheat_locations, visited 
    
    while path_heap:
        cost, (loc, visited) = heapq.heappop(path_heap)
            
        if loc == dest:   
            return cost,visited
        
        for vec in vecs:
            new_loc = (loc[0]+vec[0], loc[1] + vec[1])
            new_cost = cost+1
            if new_loc in visited or new_loc in walls:
                continue
            else:
                new_visited = visited.copy()
                new_visited.append(new_loc)
                heapq.heappush(path_heap,(new_cost, (new_loc, new_visited)))
                
no_cheat_cost, no_cheat_path = no_cheat()

distances = {x:ix for ix, x in enumerate(reversed(no_cheat_path))}
    
def find_cost(no_cheat_cost):
    global distances
    path_heap = []
    
    cheat_costs = {}

    initial_visited = set()
    initial_visited.add(start)

    heapq.heappush(path_heap,(0,(start,False,None,deepcopy(initial_visited)))) #cost, location, cheated flag, cheat_locations, visited 
    while path_heap:
        
        cost, (loc, cheated, cheat_loc, visited) = heapq.heappop(path_heap)
            
        if cheated and loc in distances:
            total_cost = cost + distances[loc] 
            
            cheat_costs[cheat_loc] = total_cost
            continue
        
        for vec in vecs:
            new_cheat = cheated
            new_loc = (loc[0]+vec[0], loc[1] + vec[1])
            new_cost = cost+1
            if new_cost >= no_cheat_cost:
                break
            if new_loc in visited:
                continue
            elif new_loc in walls:
                if cheated:
                    continue
                else:
                    new_loc2 = (new_loc[0]+vec[0],new_loc[1]+vec[1])
                    if new_loc2 in walls:
                        continue
                    new_cost +=1
                    new_cheat = True
                    cheat_loc = (new_loc,new_loc2)
                    new_loc = new_loc2
            new_visited = visited.copy()
            new_visited.add(new_loc)
            heapq.heappush(path_heap,(new_cost, (new_loc, new_cheat, cheat_loc, new_visited)))
            
    return cheat_costs

costs = find_cost(no_cheat_cost=no_cheat_cost)
print("pt1",len([x for x in costs.values() if no_cheat_cost - x >= 100]))
    