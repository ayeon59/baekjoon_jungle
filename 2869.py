import sys

a, b, v = map(int, sys.stdin.readline().split())
v = v-a
print(int(v/(a-b))+1)

#round 함수도 x

# step = 0
# day = 0
# while(1):
#     day += 1
#     step += a
#     if(step>=v):
#         break
#     step -= b
# print(day)