import sys
input = sys.stdin.readline

n = int(input())
request_budget=list(map(int,input().split()))
budget=int(input())

def calculate_budget(limit_money):
    total = 0
    for x in request_budget:
        total += x if limit_money>=x else limit_money
    return total

max_money = 0

def what_is_max(left,right):
    global max_money
    if(left>right) : 
        return 
    mid = (left+right)//2
    money = calculate_budget(mid)
    # 아직 예산이 널널하다면
    if money <= budget :
        max_money=max(mid,max_money)
        what_is_max(mid+1,right)
    else :
        what_is_max(left,mid-1)

biggest = max(request_budget)
if sum(request_budget) <= budget :
    print(biggest)

else :
    what_is_max(0,biggest)
    print(max_money)
        
