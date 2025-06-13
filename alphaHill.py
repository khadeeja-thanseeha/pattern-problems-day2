def alphaHill(n: int):
    for i in range(1,n+1,1):
        print("  "*(n-i),end=(""))
        asc=65
        for j in range(1,i+1,1):
            print(chr(asc+j-1),end=(" "))
        for j in range(i-1,0,-1):
            print(chr(asc+j-1),end=(" "))
        print("")
