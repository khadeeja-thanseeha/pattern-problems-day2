def symmetry(n: int):
    for i in range(n):
        stars="* "*(n-i)
        spaces="  "*(2*i)
        print(stars+spaces+stars)
    for i in range(n-1,-1,-1):
        stars="* "*(n-i)
        spaces="  "*(2*i)
        print(stars+spaces+stars)
