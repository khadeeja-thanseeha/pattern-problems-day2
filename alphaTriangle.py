def alphaTriangle(n: int):
    asc=65
    for i in range(1,n+1,1):
        for j in range(1,i+1,1):
            print(chr(asc+n-j),end=(" "))
        print("")
