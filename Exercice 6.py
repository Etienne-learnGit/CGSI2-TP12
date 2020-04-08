import turtle as tt

def drawCurve(tt, l, order):
    if order == 0 :
        tt.forward(l)
        return
    else :
        l /= 3
        drawCurve(tt, l, order-1)
        tt.left(60)
        drawCurve(tt, l, order-1)
        tt.right(120)
        drawCurve(tt, l, order-1)
        tt.left(60)
        drawCurve(tt, l, order-1)

if __name__ == "__main__" :
    tt.setup(800, 400)
    for i in range(0,3) :
        drawCurve(tt, 300, 3)
        tt.right(120)
    tt.exitonclick()
