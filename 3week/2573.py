#빙산이 매년 녹을때 한 요소가 다른 요소에 영향 안끼침
#빙산을 매년 녹이는 함수
#매년 덩어리가 몇개인지 계산하는 함수
import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6)

n, m = map(int,input().split())
ice = [list(map(int,input().split())) for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(x,y):
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m :
            if ice[nx][ny] > 0 and not visited[nx][ny] :
                dfs(nx,ny)

def melting(x,y,arr):
    count = 0 
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n :
            if arr[nx][ny] == 0 :
                count += 1
    return count
    

year = 0
while True :
    year += 1
    temp = [row[:] for row in ice]
    for i in range(n):
        for j in range(m):
            if ice[i][j] > 0 :
                ice[i][j] = max(ice[i][j] - melting(i, j, temp), 0)
                
    visited = [[False] * m for _ in range(n)]
    ice_num = 0
    for i in range(n):
        for j in range(m):
            if ice[i][j] > 0 and not visited[i][j]:
                dfs(i,j)
                ice_num += 1

    if ice_num >= 2 :
        print(year)
        break
    if sum(map(sum, ice)) == 0:
        print(0)
        break


