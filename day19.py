from copy import copy
from collections import Counter , defaultdict

input_ = open("data/day19.txt", "r").read().split("\n\n")

towels = input_[0].split(", ")
patterns = set(input_[1].split("\n"))

def get_matches(initial_pattern):
    ways = 0
    matches = defaultdict(lambda:0)
    matches[initial_pattern] = 1
    while matches:
        sorted_matches= list(sorted(matches.items(),key= lambda x: len(x[0]), reverse=True))
        pattern, ct = sorted_matches[0]
        del matches[pattern]
        if len(pattern)==0:
            ways += ct
        else:
            matches_counts = Counter([pattern[len(x):] for x in towels if x == pattern[:len(x)]])
            for match, ct2 in matches_counts.items():
                matches[match] += ct*ct2
        
    return ways

        
    
ct = 0
for ix, pattern in enumerate(patterns):
    print(ix)
    n_ways = get_matches(pattern)

    ct += n_ways
        
print("pt2",ct)    
