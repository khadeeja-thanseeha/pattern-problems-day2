def nStarDiamond(n: int) -> None:
    for i in range(1,n+1,1):
        spaces=" "*(n-i)
        stars="*"*(2*i-1)
        print(spaces+stars)
    for i in range(n,0,-1):
        spaces=" "*(n-i)
        stars="*"*(2*i-1)
        print(spaces+stars)
    
