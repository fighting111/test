# coding=utf-8
import turtle
turtle.color("red", "yellow")
 
turtle.begin_fill()
for _ in range(50):#缩进 尖尖数量
    turtle.forward(200)
    turtle.left(170)#角度
turtle.end_fill()
 
turtle.mainloop()
