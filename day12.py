from copy import deepcopy

grid = open("data/day12.txt", "r").read().split("\n")

neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def in_bounds(y, x):
    if y < 0 or y >= len(grid) or x < 0 or x >= len(grid[0]):
        return False
    return True


def get_edges(y, x):
    top_dir = (y, x, "-", "^")
    right_dir = (y, x + 1, "|", ">")
    down_dir = (y + 1, x, "-", "v")
    left_dir = (y, x, "|", "<")

    return set([top_dir, right_dir, down_dir, left_dir])


visited = set()


def search(loc, elem):
    global visited, group_members, group_edges
    for neighbor in neighbors:
        new_loc = (loc[0] + neighbor[0], loc[1] + neighbor[1])
        if in_bounds(*new_loc) and grid[new_loc[0]][new_loc[1]] == elem and new_loc not in visited:
            group_members.add(new_loc)
            visited.add(new_loc)
            edges = get_edges(*new_loc)
            edges_nodir = [(x[0], x[1], x[2]) for x in edges]

            for edge, edge_nodir in zip(edges, edges_nodir):
                if edge_nodir in ((x[0], x[1], x[2]) for x in group_edges):
                    remove_edge = (x for x in group_edges if (x[0], x[1], x[2]) == edge_nodir)
                    group_edges.remove(next(remove_edge))
                else:
                    group_edges.add(edge)
            search(new_loc, elem)

    return


groups = []

for iy, row in enumerate(grid):
    for ix, elem in enumerate(row):
        if (iy, ix) not in visited:
            group_members = set([(iy, ix)])
            group_edges = set(get_edges(iy, ix))
            visited.add((iy, ix))
            search((iy, ix), elem)
            groups.append({"elem": elem, "members": deepcopy(group_members), "edges": deepcopy(group_edges)})

print("pt1", sum([len(x["edges"]) * len(x["members"]) for x in groups]))


def search_edges(edge, members):
    global accounted
    if edge not in accounted:
        accounted.add(edge)
        (y, x, orient_, side_) = edge
        if orient_ == "|":  # search above and below
            if (y - 1, x, orient_, side_) in edges:
                search_edges((y - 1, x, orient_, side_), members)
            if (y + 1, x, orient_, side_) in edges:
                search_edges((y + 1, x, orient_, side_), members)
        elif orient_ == "-":
            if (y, x - 1, orient_, side_) in edges:
                search_edges((y, x - 1, orient_, side_), members)
            if (y, x + 1, orient_, side_) in edges:
                search_edges((y, x + 1, orient_, side_), members)


pt2_groups = []
for group in groups:
    edges = group["edges"]
    members = group["members"]
    accounted = set()
    sides = 0
    for edge in edges:
        if edge not in accounted:
            sides += 1
            search_edges(edge, members)

    group["sides"] = sides
    pt2_groups.append(deepcopy(group))

print("pt2", sum([x["sides"] * len(x["members"]) for x in pt2_groups]))

# 830198 too low
stop_here = 1
