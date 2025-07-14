n = int(input())
a = []
for i in range(n):
    a.append(int(input()))


# #파이썬 내장함수 정렬
# n = int(input())
# a = []
# for _ in range(n):
#     a.append(int(input()))
# a.sort()
# for x in a :
#     print(x)

# #버블 정렬
# n = int(input())
# a = []
# for i in range(n):
#     a.append(int(input()))

# for i in range(n):
#     for j in range(0, n - i - 1):
#         if a[j] > a[j+1]:
#             a[j], a[j+1] = a[j+1], a[j]

# for x in a :
#     print(x)

#선택정렬
# for i in range(n):
#     min = i
#     for j in range(i+1,n):
#         if a[j] < a[min]:
#             min = j
#         a[i],a[min] = a[min],a[i]

#삽입정렬
# for i in range(1,n):
#     j = i
#     key = a[i]
#     while j > 0 and a[j-1] > key:
#         a[j] = a[j-1]
#         j -= 1
#     a[j] = key


#퀵정렬
# def quick_sort(a,left,right):
#     pl = left
#     pr = right
#     pv = (left+right)//2

#     while pl >= pr :
#         while a[pv] > a[pl] : pl += 1
#         while a[pv] < a[pr] : pr -= 1
#         if pl <= pr :
#             a[pl],a[pr] = a[pr],a[pl]
#             pl += 1
#             pr -= 1
        
#         if left < pr :
#             return quick_sort(1,left,pr)
#         if right > pl :
#             return quick_sort(1,pl,right)
        

# def merge_sort(a,left,right):
#     if left<right:
#         center = (left+right) //2
#         merge_sort(a,left,center)
#         merge_sort(a,center+1,right)
#         p = j = 0
#         i = k = left

#         while i <= center:
#             buff[p] = a[i]
#             p += 1
#             i += 1

#         while i <= right and j < p:
#             if buff[j] <= a[i]:
#                 a[k] = buff[j]
#                 j += 1
            
#             else :
#                 a[k] = a[i]
#                 i += 1
#             k += 1
#         while j < p:
#             a[k] = buff[j]
#             k += 1
#             j += 1

# buff = [None]*n
# merge_sort(a,0,n-1)


# def heap_sort(a):
#     def down_heap(a,left,right):
#         temp = a[left] 
#         parent = left

#         while parent < (right+1)//2:
#             cl = parent * 2 + 1
#             cr = cl + 1
#             child = cr if cr <= right and a[cr] > a[cl] else cl
#             if temp >= a[child] :
#                 break
#             a[parent] = a[child]
#             parent = child
#         a[parent] = temp

#     n = len(a)

#     for i in range((n-1)//2,-1,-1):
#         down_heap(a,i,n-1)
#     for i in range(n-1,0,-1):
#         a[0], a[i] = a[i],a[0]
#         down_heap(a,0,i-1)


# def heap_sort(a):
#     def down_heap(a,left,right):
#         temp = a[left]
#         parent = left 

#         while parent < (right + 1) // 2 :
#             cl = parent * 2 + 1
#             cr = cl + 1
#             child = cr if cr <=right and a[cl] < a[cr] else cl 
#             if temp >= a[child] :
#                 break
            
#             a[parent] = a[child]
#             parent = child
#         a[parent] = temp
    
#     for i in range((n-1)//2,-1,-1):
#         down_heap(a,i,n-1)
    
#     for i in range((n-1)//2,-1,-1):
#         a[0],a[i] = a[i],a[0]
#         down_heap(a,0,i-1)

def fsort(a,max) :
    n = len(a)

    f = [0]*(max+1)
    b = [0]*n

    for i in range(n) : f[a[i]] += 1
    for i in range(1,max+1): f[i] += f[i-1]
    for i in range(n-1,-1,-1): b[f[a[i]]-1] = a[i]
    for i in range(n): a[i] = b[i]

fsort(a,max(a))
print(a)
