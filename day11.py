from collections import Counter, defaultdict

stones = open("data/day11.txt", "r").read().split()

stone_dict = defaultdict(lambda: 0)
for stone in stones:
    stone_dict[int(stone)] += 1


for blink in range(75):

    new_stones = defaultdict(lambda: 0)
    while stone_dict:
        stone, stone_count = stone_dict.popitem()
        stone_length = len(str(stone))
        if stone == 0:
            new_stones[1] += stone_count
        elif stone_length % 2 == 0:
            s1, s2 = int(str(stone)[: stone_length // 2]), int(str(stone)[stone_length // 2 :])
            new_stones[s1] += stone_count
            new_stones[s2] += stone_count

        else:
            new_stones[stone * 2024] += stone_count

    stone_dict = new_stones.copy()
    print(blink)

    stop_here = 1

print("pt1")
print(sum(stone_dict.values()))

stop_here = 1
