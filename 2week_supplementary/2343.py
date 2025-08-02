n, m = map(int, input().split())
lecture = list(map(int, input().split()))

def check(capacity):
    count = 1
    total = 0
    for lec in lecture:
        if total + lec > capacity:
            count += 1
            total = lec
        else:
            total += lec
    return count <= m

start = max(lecture)
end = sum(lecture)
result = end

while start <= end:
    mid = (start + end) // 2
    if check(mid):
        result = mid
        end = mid - 1
    else:
        start = mid + 1

print(result)


def add_video(capacity,what_video,step):
    if step == m+1 :
        max_size = max(max_size,capacity)
        return
    count = 0
    sum_video = 0
    while True :
        if sum_video + lecture[count+what_video+1] > avg_size :
            add_video(sum_video+lecture[count+what_video+1],what_video+count+1,step+1)
            add_video(sum_video,what_video+count,step+1)
        else :
            sum_video += lecture[count+what_video]


# for _ in range(m):
#     sum_video = 0
#     while num != n :
#         if sum_video >= avg_size :
#             break
#         sum_video += lecture[num]
#         num += 1
#     print(sum_video)
#     max_size = max(max_size,sum_video)

print(max_size)
