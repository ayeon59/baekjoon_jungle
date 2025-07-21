import heapq , sys
input = sys.stdin.readline
pq = []
n = int(input())
for _ in range(n):
    num = int(input())
    if num > 0 :
        heapq.heappush(pq,-num)
    if num == 0 :
        if(len(pq)==0):
            print(0)
        else :
            print(-heapq.heappop(pq))

