t = int(input())
for _ in range(t):
    cnt = 0
    n, m = map(int,input().split())
    for i in range(1,n): 
        for j in range(i+1,n):
            if (i**2+j**2+m)%(i*j) == 0:
                cnt += 1
    print(cnt)
