import sys
input = sys.stdin.readline

def get_extent(gap):
    max_part_extent = 0
    for i in range(n+1-gap):
        temp = square[i:i+gap]
        max_part_extent = max(min(temp)*gap,max_part_extent)
    return max_part_extent

while True :
    data = list(map(int, input().split()))
    n = data[0]
    if n == 0 : break        
    square = data[1:]      


    max_extant = 0
    for i in range(1,n+1):
        max_extant=max(get_extent(i),max_extant)

    print(max_extant)

