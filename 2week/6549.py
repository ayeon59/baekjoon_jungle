# import sys
# input = sys.stdin.readline

# def get_extent(gap):
#     max_part_extent = 0
#     for i in range(n+1-gap):
#         temp = square[i:i+gap]
#         max_part_extent = max(min(temp)*gap,max_part_extent)
#     return max_part_extent

# while True :
#     data = list(map(int, input().split()))
#     n = data[0]
#     if n == 0 : break        
#     square = data[1:]      


#     max_extant = 0
#     for i in range(1,n+1):
#         max_extant=max(get_extent(i),max_extant)

#     print(max_extant)

import sys
input = sys.stdin.readline

def get_max_area(hist):
    stack = []
    max_area = 0
    idx = 0

    while idx < len(hist):
        if not stack or hist[stack[-1]] <= hist[idx]:
            stack.append(idx)
            idx += 1
        else:
            top = stack.pop()
            width = idx if not stack else idx - stack[-1] - 1
            area = hist[top] * width
            max_area = max(max_area, area)

    while stack:
        top = stack.pop()
        width = idx if not stack else idx - stack[-1] - 1
        area = hist[top] * width
        max_area = max(max_area, area)

    return max_area

while True:
    line = list(map(int, input().split()))
    if line[0] == 0:
        break
    n = line[0]
    hist = line[1:]
    print(get_max_area(hist))
