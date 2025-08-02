#단순 배열을 이용한 숫자 조작 문제 같지만
#결국 매번 숫자를 노드로, get_next를 간선으로 노드를 이동하고 있고
#current로 사이클을 탐색하고 있다.
a, power = map(int, input().split())

path = []

visited = {}

def get_next(node):
    result = 0
    while node > 0:
        result += pow(node % 10, power)
        node //= 10
    return result


current = a
while True:
    if current in visited:
        break  
    visited[current] = True
    path.append(current)
    current = get_next(current)  # 간선 따라 다음 노드로 이동

# 사이클 시작 전까지의 길이 = 처음 current가 나온 위치
cycle_start_index = path.index(current)
print(cycle_start_index)
