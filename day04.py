from itertools import product
from collections import defaultdict, Counter

grid_ = open("data/day4.txt", "r").read().split("\n")

neighbors = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]  # (r,c) where positive is down and right

target = "XMAS"

candidates = {
    (r, c): neighbors for r, c in product(range(len(grid_)), range(len(grid_[0]))) if grid_[r][c] == target[0]
}  # (r,c): direction where no set direction is None


def search_(target_char, candidates):

    new_candidates = defaultdict(list)
    for coord, directions_ in candidates.items():

        for neighbor in directions_:  # find all adjacent values and check if they are equal to the current target
            new_coord = (coord[0] + neighbor[0], coord[1] + neighbor[1])
            try:
                assert new_coord[0] >= 0
                assert new_coord[1] >= 0
                if grid_[new_coord[0]][new_coord[1]] == target_char:
                    new_candidates[new_coord].append(neighbor)

            except:
                pass

    return new_candidates


for target_char in target[1:]:
    candidates = search_(target_char, candidates)


print("pt1", sum([len(dirs) for dirs in candidates.values()]))


neighbors = [(1, 1), (1, -1), (-1, -1), (-1, 1)]  # (r,c) where positive is down and right

candidates = {
    (r, c): neighbors for r, c in product(range(len(grid_)), range(len(grid_[0]))) if grid_[r][c] == target[1]
}  # (r,c): direction where no set direction is None
for target_char in target[2:]:
    candidates = search_(target_char, candidates)

A_locs = Counter([(coord[0] - dir_[0], coord[1] - dir_[1]) for coord, dirs in candidates.items() for dir_ in dirs])

print("pt2", len(list(filter(lambda x: x == 2, A_locs.values()))))
