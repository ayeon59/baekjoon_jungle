
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