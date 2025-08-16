def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

T = int(input())
for _ in range(T):
    num = int(input())
    for i in range(num // 2, 1, -1): 
        if is_prime(i) and is_prime(num - i):
            print(i, num - i)
            break
