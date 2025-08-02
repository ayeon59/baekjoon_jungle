import sys
input = sys.stdin.readline

n = int(input())
card_sang = list(map(int, input().split()))
m = int(input())
card = list(map(int, input().split()))

card_sang.sort()

# target의 첫 등장 위치 (lower bound)
def lower_bound(arr, target):
    start, end = 0, len(arr)
    #어쨌든 이 반복은 start==end 거나 start>end 여서 끝남
    while start < end:
        mid = (start + end) // 2
        #해당 값이 여전히 타겟이랑 같으면 계속 왼쪽
        if arr[mid] >= target:
            end = mid
        #타겟이랑 처음 달라지는 지점에서 끝
        else:
            start = mid + 1
    return start


def upper_bound(arr, target):
    start, end = 0, len(arr)-1
    while start < end:
        mid = (start + end) // 2
        
        if arr[mid] > target:
            end = mid
        #다른값이 나올때까지 start를 오른쪽으로 옮기고
        #
        else:
            start = mid + 1
    return start

# 개수 구하기: upper - lower
for x in card:
    low = lower_bound(card_sang, x)
    high = upper_bound(card_sang, x)
    print(high, end=' ')
    print(low, end=' ')
    print()
