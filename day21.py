import heapq
from sys import maxsize
from copy import deepcopy
from itertools import groupby
from collections import Counter, defaultdict
from functools import cache

inputs = open("data/day21.txt", "r").read().splitlines()

keypad = {"A":(3,2),"0":(3,1),"1":(2,0),"2": (2,1),"3":(2,2),"4":(1,0),"5":(1,1),"6":(1,2),"7":(0,0),"8":(0,1),"9":(0,2)}
arrows = {"A":(0,2),(-1,0):(0,1),(0,-1):(1,0),(1,0):(1,1),(0,1):(1,2)}

vecs = [(0,1),(0,-1),(1,0),(-1,0)]

key_locs = set(keypad.values())
arrow_locs = set(arrows.values())

def cost(vecs):
    cost_ = 0
    for ix in range(len(vecs)-1):
        vec1 = arrows[vecs[ix]]
        vec2 = arrows[vecs[ix+1]]
        
        cost_ += abs(vec1[0]-vec2[0]) + abs(vec1[1]-vec2[1])
        
    return cost_

def robot1(start, target):
    
    start_loc = keypad[start]
    target_loc = keypad[target]
    
    visited = [start_loc]
    path_heap = []
    heapq.heappush(path_heap,(0,start_loc,visited))
    
    shortest_paths = []
    
    min_moves = maxsize
    
    while path_heap:
        moves, loc,path = heapq.heappop(path_heap)
        
        if loc == target_loc and moves <= min_moves:
            min_moves = moves
            path_vecs = [(path[i+1][0] - path[i][0], path[i+1][1]-path[i][1]) for i in range(len(path)-1)]
            path_vecs.append("A")
            shortest_paths.append(path_vecs)
            
            
        elif moves > min_moves:
            continue
            
        else:
            
            for vec in vecs:
                new_loc = (loc[0]+vec[0], loc[1]+ vec[1])
                if new_loc in key_locs and new_loc not in path:
                    path_copy = path.copy()
                    path_copy.append(new_loc)
                    heapq.heappush(path_heap,(moves+1, new_loc, path_copy))
                    
    return shortest_paths
    
@cache
def robot2(start,target):
    start_loc = arrows[start]
    target_loc = arrows[target]
    
    visited = [start_loc]
    path_heap = []
    heapq.heappush(path_heap,(0,start_loc,visited))
    
    shortest_paths = set()
    
    min_moves = maxsize
    
    while path_heap:
        moves, loc,path = heapq.heappop(path_heap)
        
        if loc == target_loc and moves <= min_moves:
            min_moves = moves
            vec_path = [(path[i+1][0] - path[i][0], path[i+1][1]-path[i][1]) for i in range(len(path)-1)]
            vec_path.append("A")
            shortest_paths.add(tuple(vec_path))
            
        elif moves > min_moves:
            continue
            
        else:
            
            for vec in vecs:
                new_loc = (loc[0]+vec[0], loc[1]+ vec[1])
                if new_loc in arrow_locs and new_loc not in path:
                    path_copy = path.copy()
                    path_copy.append(new_loc)
                    heapq.heappush(path_heap,(moves+1, new_loc, path_copy))
                    
    return shortest_paths
     
def split_list(a):  
    result = []
    current = []
    for item in a:
        if item == "A":
            current.append(item)  # Include the delimiter in the current list
            result.append(tuple(current))
            current = []
        else:
            current.append(item)
    if current:  # Append the last segment if not empty
        result.append(current)
    return result

       
def shortest_route(input_, n_robots):             
    key_loc = "A"   
    robot_paths = []
    for key_target in input_:
        paths = robot1(key_loc,key_target)
        lowest_cost = sorted(paths,key=lambda x: cost(x))[0]
        robot_paths.extend(lowest_cost)
        key_loc = key_target
        
    robot_paths = Counter(split_list(robot_paths))
        
    robot_locs = ["A" for _ in range(n_robots)]
    
    for robot_ix, robot_loc in enumerate(robot_locs):
        
        print(robot_ix)
        new_path = defaultdict(lambda: 0)

        for vector_path, path_count in robot_paths.items():

            shortest_path = []
            for vector_target in vector_path:

                    
                paths = robot2(robot_loc, vector_target)
                paths = sorted(paths,key=lambda x: cost(x))[0]
                shortest_path.extend(list(paths))

                    
                robot_loc = vector_target
                
            
            shortest_segments = split_list(shortest_path)
            
            for seg in shortest_segments:
                new_path[seg] += path_count

                
        robot_paths = deepcopy(new_path)
                
        final_count = 0
        for path, path_count in robot_paths.items():
            final_count += len(path) * path_count
        
    return final_count
   
pt2 = 0             
for input_ in inputs:
    input_val = int(input_[:-1])
    route_cost = shortest_route(input_,25)
        
    print(input_,input_val, route_cost )
    
    pt2 += input_val * route_cost
    
print(pt2)
