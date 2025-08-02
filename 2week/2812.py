import sys
input = sys.stdin.readline

n, k = map(int,input().split())
num = input().strip()
pop_num = 0
answer = []
#첫 원소 넣고 시작
answer.append(int(num[0]))
num = num[1:]

#팝 개수 도달하면 그만
while pop_num != k and num: 
    target = int(num[0])
    num = num[1:]
    top = answer[-1]
    
    if top < target :
        
        while answer and answer[-1] < target and pop_num < k:
            answer.pop()
            pop_num += 1    
        answer.append(target)    

    else : 
        answer.append(target)

for ch in num:
    if len(answer) == n - k:
        break
    answer.append(int(ch))

print(int(''.join(map(str, answer))))

    

