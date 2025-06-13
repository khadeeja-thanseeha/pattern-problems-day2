def nLetterTriangle(n: int) -> None:
    for i in range (1,n+1,1):
        asc=65
        for j in range(1,i+1,1):
            print(chr(asc),end=(" "))
            asc+=1
        print("")

