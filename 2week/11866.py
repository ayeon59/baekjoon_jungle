import sys
from collections import deque
input = sys.stdin.readline


n, k = map(int,input().split())
queue = deque(range(1, n + 1))
answer = []

count = 1
while len(queue) > 1 :
    if count % k == 0 :
        answer.append(queue.popleft())
    else :
        queue.append(queue.popleft())
    count += 1
answer.append(queue.popleft())
print("<" + ", ".join(map(str, answer)) + ">")