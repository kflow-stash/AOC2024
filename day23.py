from collections import defaultdict
from copy import deepcopy

sets = defaultdict(lambda: set())

input_ = open("data/day23.txt", "r").read().split("\n")

original = defaultdict(lambda: set())
for z in input_:
    x,y = z.split("-")
    sets[frozenset({x})].add(y)
    sets[frozenset({y})].add(x)
    
    original[x].add(y)
    original[y].add(x)
 
iz = 0
last_sets = deepcopy(sets)
while len(last_sets)>0:
    
    print(iz)
    
    inters = {}
    for elem, set_ in last_sets.items():
        for elem2 in set_:
            new_key = set(elem)
            new_key.add(elem2)
            new_key = frozenset(new_key)
            
            if new_key not in inters:
                new_cycle = last_sets[elem].intersection(original[elem2])
                if len(new_cycle)>0:
                    inters[new_key] = new_cycle
      
    if len(inters) == 0:
        break          
    last_sets = deepcopy(inters)
    
    iz += 1
    
biggest_set = sorted(last_sets.items(),key=lambda x: len(x[1]),reverse= True)[0]
  
biggest_set = set(biggest_set[0]).union(biggest_set[1])
lan_party = ",".join(list(sorted(biggest_set)))

print(lan_party)
  
"""threes = set()
for duo, set_ in inters.items():
    for elem in set_:
        t = set(duo)
        t.add(elem)
        threes.add(frozenset(t))
     
pt1 = 0   
for three in threes:
    if any([x[0] == "t" for x in three]):
        pt1+=1
print(pt1)"""
