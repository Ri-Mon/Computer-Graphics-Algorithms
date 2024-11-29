# Digital Differential Analyzer
def Dcalc(x1, y1, x2, y2):

    Dx = x2 - x1
    Dy = y2 - y1
    steps = 0

    if(abs(Dx) > abs(Dy)):
        steps = abs(Dx)
    else:
        steps = abs(Dy)
    
    xInc = Dx / steps
    yInc = Dy / steps

    x = x1
    y = y1
    for i in range(steps+1):
        print(f"({round(x)},{round(y)})\n")
        x += xInc
        y += yInc

Dcalc(1, 1, 8, 5)
