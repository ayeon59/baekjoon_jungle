import sys
sys.setrecursionlimit(10**8)

n,m = map(int,input().split())
tree = list(map(int,input().split()))


#특정 길이로 잘랐을 때 몇개의 조각이 나오는지
def cut_tree(height):
    sum = 0 
    for x in tree :
        sum += (0 if x -height <= 0 else x-height)
    return sum

max_cut = 0

def find_height(start,end):
    global max_cut
    if start >= end :
        return
    mid = (start+end)//2
    if cut_tree(mid) >= m : 
        max_cut = max(max_cut,mid)
        find_height(mid+1,end)
    else : 
        find_height(start,mid)
        

tree.sort()
find_height(0,tree[-1]+1)
print(max_cut)