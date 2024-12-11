from math import prod
from itertools import product
from functools import reduce
lines = open("data/day7.txt","r").read().split("\n")

samples = {}
for line in lines:
    samples[int(line.split(":")[0])]= list(map(int,line.split(":")[1].split()))
    
def mash(x):
    return int(str(x[0]) + str(x[1]))
    
ops = [prod,sum,mash] #just remove mash for pt1 answer


def reduce_(funcs, vals): #vals has one less than funcs
    if len(funcs)==0:
        return vals[0]
    else:
    
        rh = funcs[0]((vals[0],vals[1]))
    
        new_funcs = funcs[1:]
        new_vals = [rh] + vals[2:]
    
        return reduce_(new_funcs,new_vals)


valid_targets = []
for target,nums in samples.items():
    ops_perms = list(product(ops,repeat = len(nums)-1))
    for perm in ops_perms:  
        result = reduce_(perm,nums)
        
        if result == target:
            valid_targets.append(target)
            break
       
    
print("pt2",sum(valid_targets))


    
