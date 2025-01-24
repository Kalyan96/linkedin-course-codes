import turtle as t


if __name__ == '__main__':
    tur = t.Turtle()
    scr = t.Screen()
    tur.speed(100000)
    for i in range(3,60):
        for j in range(i):
            tur.forward(20)
            tur.right(360 / i)
    scr.exitonclick()

