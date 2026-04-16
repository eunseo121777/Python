import turtle as t
import random

x=0
y=0
r=0
g=0
b=0

t.penup()
t.shape("turtle")

screen=t.Screen()
screen.title("거북이 글자쓰기(모듈버전)")
screen.colormode(255)

text=t.textinput("문자열 입력","거북이 쓸 문자열을 입력")
text_len=len(text)

if text:
    for i in range (text_len):
        x=random.randint(-300,300)
        y=random.randint(-300,300)

        r=random.randint(0, 255)
        g=random.randint(0, 255)
        b=random.randint(0, 255)

        t.goto(x, y)
        t.color(r, g, b)

        t.write(text[i], font=("Arial", random.randint(20,50), "bold"))

screen.exitonclick()