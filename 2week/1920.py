n = int(input())
a = list(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))

def quick_sort(left,right,a):
    pl = left
    pr = right
    pv = (left+right)//2

    while pl <= pr :
        while a[pv] > a[pl] : pl += 1
        while a[pv] < a[pr] : pr -= 1
        if pl <= pr :
            a[pl],a[pr] = a[pr],a[pl]
            pl += 1
            pr -= 1
        
    if left < pr :
        quick_sort(left,pr,a)
    if right > pl :
        quick_sort(pl,right,a)


def isIn(target,start,end):
    if start > end :
        return 
    mid = ( start + end ) // 2
    if a[mid] == target :
        return True
    elif a[mid] > target :
        return isIn(target,start,mid)
    else :
        return isIn(target,mid+1,end)

    

quick_sort(0,n-1,a)

for x in b :
    if isIn(x,0,len(a)-1) : print(1)
    else : print(0)

