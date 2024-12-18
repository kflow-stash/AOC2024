import heapq
from sys import maxsize

input_ = open("data/day18.txt", "r").read().splitlines()

mx = 70
my = 70
vecs = {(0,1),(0,-1),(1,0),(-1,0)}
target = (70,70)

def in_bounds(x,y):
    if x < 0 or x > mx or y < 0 or y > my:
        return False
    return True

blocks = set()
for line_ in input_[:1024]:
    x,y = map(int, line_.split(","))
    blocks.add((x,y))
    


def search():
    distances = []
    heapq.heappush(distances, (0,(0,0)))
    visited = {(0,0):0}
    found = False
    while distances:
        dist, loc = heapq.heappop(distances)
        
        if loc == target:
            found = True
            break
        
        for vec in vecs:
            new_loc = (loc[0]+vec[0],loc[1]+vec[1])
            if (in_bounds(*new_loc) 
                and new_loc not in blocks 
                and visited.get(new_loc,maxsize)>dist+1):
                heapq.heappush(distances, (dist+1,new_loc))
                visited[new_loc] = dist+1
                
    if found:
        return dist
    else:
        return -1
            
print("pt1",search())

for line_ in input_[1024:]:
    x,y = map(int, line_.split(","))
    blocks.add((x,y))
    
    if search() == -1:
        print("pt2",f"{x},{y}")
        break


            