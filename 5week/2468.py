#_2468:안전영역

"""
1. 내린 비의 양 "이하"의 모든 지점은 물에 잠긴다.
2. 물에 잠기지 않는 영역을 구한다 
3. 비가 얼마나 올 지 모른다.
-> 1&2번 조건 체크하면서 BFS()
-> BFS 한 사이클 돌면 영역 개수 +1
"""
#영역 크기 입력
import sys
from collections import deque

n = int(input())
rain = []
visited = [[False] * (n) for _ in range(n)]
for i in range(n):
    rain.append(list(map(int,input().split())))
queue = deque((0,0))


