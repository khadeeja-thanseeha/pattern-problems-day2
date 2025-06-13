def symmetry(n: int):
    asc=65
    for i in range(1,n+1,1):
        stars="* "*i
        spaces="  "*((n-i)*2)
        print(stars+spaces+stars)
    for i in range(n-1,-1,-1):
        stars="* "*i
        spaces="  "*((n-i)*2)
        print(stars+spaces+stars)
