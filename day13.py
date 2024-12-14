from collections import defaultdict
from math import lcm

input_ = open("data/day13.txt","r").read().split("\n\n")

game_scores = {}
for game_id, game in enumerate(input_):
    [a, b, goal] = game.split("\n")
    [a_x, a_y] = [int(x[2:]) for x in a.split(": ")[1].split(", ")]
    [b_x,b_y] = [int(x[2:]) for x in b.split(": ")[1].split(", ")]
    [goal_x, goal_y] = [int(x[2:]) for x in goal.split(": ")[1].split(", ")]
    
    goal_x += 10000000000000
    goal_y += 10000000000000
    
    a_lcm = lcm(a_x,a_y)
    eq1_mult = a_lcm // a_x
    eq2_mult = a_lcm // a_y
    denom_ = (b_x * eq1_mult - b_y*eq2_mult)
    
    n_b = (goal_x * eq1_mult - goal_y*eq2_mult) / denom_
    if n_b == int(n_b):
        n_a = (goal_x - (int(n_b) * b_x)) / a_x
        if n_a == int(n_a):
            game_scores[game_id] = int(n_a * 3 + n_b)
            
print("pt2",sum(game_scores.values()))    
stop_here = 1