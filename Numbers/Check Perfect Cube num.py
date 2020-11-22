n = float(input("Enter a number:"))


def cube(n):
    cube_root = n**(1./3.)
    if round(cube_root) ** 3 == n:
        print(True, "its a perfect cube number")
    else:
        print(False, "its not a perfect cube number")


cube(n)
