from copy import deepcopy
from collections import defaultdict
import time



input_ = open("data/day14.txt","r").read().split("\n")

mx = 101
my = 103

dot_grid = [["." for _ in range(mx)] for _ in range(my)]


robots = []
for line in input_:
    ps = tuple(map(int,line.split(" ")[0].split("=")[1].split(",")))
    vs = tuple(map(int,line.split(" ")[1].split("=")[1].split(",")))
    
    robots.append({"p":ps,"v": vs})
 
def draw_grid(ps):
    grid = deepcopy(dot_grid)
    for p in ps:
        grid[p[1]][p[0]] = "x"
        

    print("\n".join(["".join(x) for x in grid]))
        
            
       
for it in range(1000000):
    new_robots = []
    row_counts = defaultdict(set)
    for robot in robots:
        new_pos = ((robot["p"][0] + robot["v"][0]) % mx, (robot["p"][1] + robot["v"][1]) % my)
        new_robots.append({"p":new_pos,"v": robot["v"]})
        
        row_counts[new_pos[1]].add(new_pos[0])
        
        
    if it == 100:
        q1 = [x for x in robots if x["p"][0] < mx // 2 and x["p"][1] < my //2]
        q2 = [x for x in robots if x["p"][0] > mx // 2 and x["p"][1] < my //2]
        q3 = [x for x in robots if x["p"][0] > mx // 2 and x["p"][1] > my //2]
        q4 = [x for x in robots if x["p"][0] < mx // 2 and x["p"][1] > my //2]
                
        print("pt1" , len(q1) * len(q2) * len(q3) * len(q4))
        
        
    row1 = [x for x in new_robots if x["p"][1] == 0]
    row1_xs = set([x["p"][0] for x in row1])
    
    row_counts = [len(x) for x in row_counts.values()]
    
    if max(row_counts) > 15:
        print("ITERATION",it)
        draw_grid([x["p"] for x in new_robots])
        time.sleep(1)
        
    robots = new_robots.copy()
       
       
    