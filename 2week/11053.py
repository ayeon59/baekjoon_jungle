n = int(input())
a = list(map(int,input().split()))
cnt = n
for i in range(n-1) :
    if a[i] > a[i+1]:
        cnt -= 1
print(cnt)
    