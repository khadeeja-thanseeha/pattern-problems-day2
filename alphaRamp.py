def alphaRamp(n: int) -> None:
    asc=65
    for i in range(n):
        ch=(chr(asc)+" ")*(i+1)
        print(ch)
        asc+=1
        print("")
