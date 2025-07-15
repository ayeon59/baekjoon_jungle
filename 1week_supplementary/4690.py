for a in range(1, 101):  
    a3 = a ** 3
    for b in range(1, a):        
        b3 = b ** 3
        for c in range(b, a):    
            c3 = c ** 3
            for d in range(c, a): 
                d3 = d ** 3
                if b3 + c3 + d3 == a3:
                    print(f"Cube = {a}, Triple = ({b},{c},{d})")
