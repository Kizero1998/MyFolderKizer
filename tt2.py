from turtle import*
shape("turtle")
speed(200)
angle=100
for n in range(100,2,-1):##start, stop, step
    color("#761ca7","#ffe4e1")
    begin_fill()

    for i in range(n):
        forward(10)
        right(360/n)
    end_fill()
