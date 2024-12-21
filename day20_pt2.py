import heapq

grid_ = open("data/day20.txt", "r").read().splitlines()

vecs = [(0,1),(0,-1),(1,0),(-1,0)]

walls = set()
locs = set()

for iy, row in enumerate(grid_):
    for ix, elem in enumerate(row):
        if elem == "S":
            start = (iy,ix)
            locs.add((iy,ix))
        elif elem == "#":
            walls.add((iy,ix))
            
        elif elem == "E":
            dest = (iy,ix)
            locs.add((iy,ix))
            
        else:
            locs.add((iy,ix))

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

all_vecs = set()
for y in range(-20,20+1):
    xm = 20 - abs(y)
    for x in range(-xm,xm+1):
        all_vecs.add((y,x))

 
def possible_cheats(loc):
    all_possible = set((loc[0]+y,loc[1]+x) for y,x in all_vecs).intersection(locs)
    all_possible = set(((y,x), (abs(y-loc[0])+abs(x-loc[1]))) for y,x in all_possible)
    
    return all_possible

cheats = set()
for ix, loc in enumerate(locs):
    if ix % 1000 ==0:
        print(ix)
    possibles = possible_cheats(loc)
    initial_dist = no_cheat_cost - distances[loc] # distance to this location with no cheating
    for loc2, cheat_len in possibles:
        dist = initial_dist + cheat_len + distances[loc2]
        if dist <= no_cheat_cost - 100:
            cheats.add((loc,loc2))

print(len(cheats))        
  