#时间显示
from turtle import*
def seven(i):
    pensize(5)
    color("red")
    hideturtle()
    if  i=='0':
        forward(60)
        right(90)
        forward(90)
        right(90)
        forward(60)
        right(90)
        forward(90)
        right(90)
    elif i=='1':
        penup()
        forward(60)
        pendown()
        right(90)
        forward(90)
        backward(90)
        left(90)
    elif i=='2':
        forward(60)
        right(90)
        forward(45)
        right(90)
        forward(60)
        left(90)
        forward(45)
        left(90)
        forward(60)
        backward(60)
        penup()
        left(90)
        forward(90)
        right(90)
        pendown()
    elif i=='3':
        forward(60)
        right(90)
        forward(45)
        right(90)
        forward(60)
        penup()
        backward(60)
        pendown()
        left(90)
        forward(45)
        right(90)
        forward(60)
        penup()
        right(90)
        forward(90)
        right(90)
        pendown()
    elif i=='4':
        right(90)
        forward(45)
        left(90)
        forward(60)
        left(90)
        forward(45)
        backward(90)
        penup()
        forward(90)
        right(90)
        backward(60)
        pendown()
    elif i=='5':
        forward(60)
        backward(60)
        right(90)
        forward(45)
        left(90)
        forward(60)
        right(90)
        forward(45)
        right(90)
        forward(60)
        penup()
        right(90)
        forward(90)
        right(90)
        pendown()
    elif i=='6':
        forward(60)
        backward(60)
        right(90)
        forward(90)
        left(90)
        forward(60)
        left(90)
        forward(45)
        left(90)
        forward(60)
        penup()
        right(90)
        forward(45)
        right(90)
        pendown()
    elif i=='7':
        forward(60)
        right(90)
        forward(90)
        penup()
        backward(90)
        left(90)
        backward(60)
        pendown()
    elif i=='8':
        forward(60)
        right(90)
        forward(90)
        right(90)
        forward(60)
        right(90)
        forward(90)
        backward(45)
        right(90)
        forward(60)
        penup()
        backward(60)
        left(90)
        forward(45)
        right(90)
        pendown()
    else:
        forward(60)
        right(90)
        forward(90)
        backward(45)
        right(90)
        forward(60)
        right(90)
        forward(45)
        penup()
        right(90)
        pendown()
def main():
    num=input("please input the time:YYYY/MM/DD")
    i=0
    penup()
    backward(400)
    pendown()
    for i in range(0,8):
        seven(num[i])
        i=i+1
        penup()
        forward(80)
        pendown()
main()