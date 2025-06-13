def nLetterTriangle(n: int):
    for i in range(n,0,-1):
        asc=65
        for j in range(i):
            print(chr(asc+j),end=(" "))
        print("")
