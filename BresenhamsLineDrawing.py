def BLcalc(x1, y1, x2, y2):

    Dx = x2 - x1
    Dy = y2 - y1
    p = 2*Dy - Dx
    x = x1
    y = y1

    while x <= x2:
        print(f"({x},{y})\n")

        x += 1
        if p < 0:
            p = p + 2*Dy
        else:
            p = p + 2*Dy - 2*Dx
            y += 1

BLcalc(1, 1, 8, 5)
