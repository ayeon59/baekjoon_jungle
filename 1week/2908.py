a, b = map(str,input().split())
a = a[::-1]
b = b[::-1]

print(a if a>b else b)