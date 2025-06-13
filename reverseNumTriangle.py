def nNumberTriangle(n: int) -> None:
    for i in range(n,0,-1):
        for j in range(i):
            k=j+1
            print(k,end=(" "))
        print("")
