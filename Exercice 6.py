import turtle as tt

def drawCurve(tt, l, x) :
    if x == 0 :
        return
    tt.forward(l/4**x)
    tt.left(45)
    tt.forward(l/4**x)
    tt.right(90)
    tt.forward(l/4**x)
    tt.left(45)
    tt.forward(l/4**x)
    return drawCurve(tt, l, x)

tt.setup(800, 400)
drawCurve(tt, 300, 2)
tt.exitonclick()
