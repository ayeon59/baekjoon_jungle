n = int(input())
solution = list(map(int,input().split()))

min_solution = 0


def find_zero_solution(start,end):
    global min_solution
    if start >= end :
        return
    if solution[start] + solution[end] > 0 :
        print()


solution.sort()
#산성만 있는 경우
if solution[0] >= 0 : print(solution[0], solution[1])
elif solution[-1] <= 0 : print(solution[-2], solution[-1])
else : 
    find_zero_solution(0,n-1)