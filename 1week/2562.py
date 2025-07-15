a = list()
for _ in range(9):
    a.append(int(input()))
print(max(a))
print(a.index(max(a))+1)




import sys
input = sys.stdin.readline

n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))

count = [0]*max(a)

for i in range(n):
    count[int(input())] += 1


for i in range(len(count)):
    for j in range(count[i]):
        print(i)