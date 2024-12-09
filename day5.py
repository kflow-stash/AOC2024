from functools import cmp_to_key

rules, lines = open("data/day5.txt","r").read().split("\n\n")

rules = [tuple(map(int,z.split("|"))) for z in rules.split("\n")]

lines = [list(map(int,line.split(","))) for line in lines.split("\n")]

valid_lines =[]
invalid_lines = [] 
for line in lines:
    invalid = False
    for ix, elem in enumerate(line):
        prior_rules = set([x for x,y in rules if y == elem])
        post_rules = set([y for x,y in rules if x == elem])
        
        prior_invalid = any([prior in post_rules for prior in line[:ix]])
        post_invalid = any([post in prior_rules for post in line[ix+1:]])
        if prior_invalid or post_invalid:
            invalid = True
            break
    if invalid:
        invalid_lines.append(line)
    else:
        valid_lines.append(line)
            
middles = [x[len(x)//2] for x in valid_lines]       
print("pt1",sum(middles))


def compare_(elem1,elem2):
    prior_rules = set([x for x,y in rules if y == elem1])
    return 1 if elem2 not in prior_rules else -1

sorted_invalid = []
for line in invalid_lines:
    sorted_line = sorted(line,key=cmp_to_key(lambda x,y: compare_(x,y)))
    sorted_invalid.append(sorted_line)
    
middles = [x[len(x)//2] for x in sorted_invalid]     
print("pt2",sum(middles))

                