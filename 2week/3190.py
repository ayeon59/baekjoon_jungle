n = int(input())
ground = list([0] * n for _ in range(n))
snake = list([False] * n for _ in range(n))
snake[0][0] = True
move = []
apple = int(input())
for i in range(apple):
    a, b = map(int,input().split())
    ground[a-1][b-1] = 1
move_count = int(input())
for i in range(move_count):
    a, b = input().split()
    a = int(a)
    move.append((a,b))
now = 0
while True : 
    now += 1
    if any(time == now for time, _ in move):
        

print(ground)
print(move)

