n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

for i in range(n):
    for j in range(0, n - i - 1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]

for x in a :
    print(x)
        