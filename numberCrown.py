def numberCrown(n):
    for i in range(1,n+1,1):
        for j in range(1,i+1,1):
            if(j<=i):
                print(j,end=" ")
        spaces="  "*((j-1)*2)
        print(spaces,end="")
        for j in range(i,0,-1):
            if(j>0):
                print(j,end=" ")
        print("")
