import sys
input = sys.stdin.readline

stick = []
n = int(input())

for i in range(n):
    if i == 0 : 
        stick.append(int(input()))
        continue
    num = int(input())
    while(stick and stick[-1]<=num):
        stick.pop()
    stick.append(num)
        
    

print(len(stick))
