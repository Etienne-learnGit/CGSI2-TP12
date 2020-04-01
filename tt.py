import turtle as tt

def drawCurve(tt, l, x) :
    if x == 0 :
        tt.forward(l)

    else :
        tt.forward(l/4*x)
        tt.left(45)
        tt.forward(l/4*x)
        tt.right(90)
        tt.forward(l/4*x)
        tt.left(45)
        tt.forward(l/4*x)

    return drawCurve(tt, l/4, x-1)

tt.setup(800, 400)
drawCurve(tt, 300, 2)
tt.exitonclick()
