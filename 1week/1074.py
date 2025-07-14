x = 0
y = 0
step = 0
n,r,c = map(int,input().split())
    
while(1):
    if x==r and y==c:
        print(step)
        break
    if step%4==0:
        y += 1
        step += 1
    elif step%4==1:
        x += 1
        y -= 1
        step += 1
    elif step%4==2:
        y += 1
        step += 1
    else :
        x -= 1
        y += 1
        step += 1