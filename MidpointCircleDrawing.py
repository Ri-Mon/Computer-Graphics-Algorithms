def Pixel(a, b, x, y):
    print(f"({x+a}, {y+b})")
    print(f"({-x+a}, {y+b})")
    print(f"({x+a}, {-y+b})")
    print(f"({-x+a}, {-y+b})")
    print("*********************")

    print(f"({y+a}, {x+b})")
    print(f"({-y+a}, {x+b})")
    print(f"({y+a}, {-x+b})")
    print(f"({-y+a}, {-x+b})")
    print("*********************")


def Mcircle(a, b, r):
    x = 0
    y = r
    d = 1 - r

    while y >= x:
        Pixel(a, b, x, y)
        x += 1
        if d > 0:
            y -= 1
            d = d + 2* (x-y) + 5
        else:
            d = d + 2*x + 3

Mcircle(0, 0, 2)
