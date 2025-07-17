n, r, c = map(int,input().split())

while n > 0 :
    size = 2 ** (n-1)
    square = size**2
    x = 0
    y = 0
    if 0+x < r < size and 0+y < c < size :
        pass
    if 0 < r < size and size+1 < c < 2*size:
        x += size