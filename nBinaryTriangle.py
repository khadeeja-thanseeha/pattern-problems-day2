def nBinaryTriangle(n: int) -> None:
    for i in range(1,n+1,1):
        b=1 if i%2!=0 else 0
        for j in range(i):
            if(b==1):
                print(b,end=" ")
                b=0
            else:
                print(b,end=" ")
                b=1
        print("")
