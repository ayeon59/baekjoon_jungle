#입력으로 받는 선로에 최대한 많은 인원이 포함되어야 한다.
#결과값의 기준은 집과 사무실의 위치가 전부 포함되어야 한다.
#즉, 집과 사무실의 위치가 길이를 넘어서는 사람들은 애초에 제외
#집과 사무실의 위치가 선로를 넘지 않는 사람들이 가장 많이 중복된 곳에 설치
#컴퓨터야 어디에 사람이 가장 많은지 알려줄래 내가 철로 길이랑 사람들 위치 알려줄게
#우선순위큐의 장점 : 최대 또는 최소값을 기가막히게 알려줌

import heapq
import sys
input = sys.stdin.readline

n = int(input())
people = []

for _ in range(n):
    a, b = map(int, input().split())
    start, end = min(a, b), max(a, b)
    people.append((start, end))

trail = int(input())

# 끝점 기준 정렬
people.sort(key=lambda x: x[1])

heap = []
max_count = 0

for start, end in people:
    if end - start > trail:
        continue
    #힙의 최소 요소 = 현재 선로의 시작점
    heapq.heappush(heap, start)
    #선로의 시작점을 벗어나기 시작하면 다음 기준 세우기
    while heap and heap[0] < end - trail:
        heapq.heappop(heap)
    max_count = max(max_count, len(heap))

print(max_count)
