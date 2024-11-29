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

def Bcircle(a, b, r):
    x = 0
    y = r
    d = 3 - 2*r

    while y >= x:
        Pixel(a, b, x, y)
        x += 1
        if d > 0:
            y -= 1
            d = d + 4*(x - y) + 10
        else:
            d = d + 4*x + 6

Bcircle(0, 0, 2)