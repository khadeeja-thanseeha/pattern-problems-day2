def getNumberPattern(n: int) -> None:
    size=2*n-1
    for i in range(size):
        for j in range(size):
                value = n - min(i, j, size - 1 - i, size - 1 - j)
                print(value, end="")


        print("")
