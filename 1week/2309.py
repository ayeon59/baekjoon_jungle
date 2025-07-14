from itertools import combinations
a = []
for _ in range(9):
    a.append(int(input()))

for comb in combinations(a, 7):
    if (sum(comb)==100):
        for x in comb:
            print(x)
        break