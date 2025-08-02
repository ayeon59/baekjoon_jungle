


def fib(num):
    if num == 0 :
        return 0
    elif num == 1:
        return 1
    return fib(num-1)+fib(num-2)

arr = [0, 1]
def fib_top_down(num):
    if num < len(arr):
        return arr[num] 
    val = fib_top_down(num - 1) + fib_top_down(num - 2)
    arr.append(val)
    return val

def fib_bottom_up(n):
    if n == 0:
        return 0
    fib = [0, 1]  
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[n]

print(fib(7))
print(fib_bottom_up(7)) 
print(fib_top_down(7)) 






