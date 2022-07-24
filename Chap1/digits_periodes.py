import decimal
from decimal import Decimal

n = 300
decimal.getcontext().prec = n

from turtle import *
wn=Screen()
wn.bgcolor("gray")
#wn.setworldcoordinates(-100, -100, 200, 200)
t1 = Turtle()
#t1.color('red')
t1.pensize(3)
t1.speed("fast")

t2 = Turtle()
#t2.color('green')
t2.pensize(3)
t2.speed("fast")

t3 = Turtle()
#t3.color('white')
t3.pensize(3)
t3.speed("fast")

t4 = Turtle()
#t4.color('yellow')
t4.pensize(3)
t4.speed("fast")

r1 = str(Decimal('55') / 89)
r2 = str(Decimal('89') / 153)
r3 = str(Decimal('131') / 1001)
r4 = str(Decimal('2').sqrt())
R1 = [int(x) for x in r1[2 : n + 1]]
R2 = [int(x) for x in r2[2 : n + 1]]
R3 = [int(x) for x in r3[2 : n + 1]]
R4 = [int(x) for x in r4[2 : n + 1]]

t1.up()
t1.setposition(-200,-160)
t1.down()
t1.write('55/89', font=("Verdana",15, "normal"))
t1.color('red')

t2.up()
t2.setposition(50,50)
t2.down()
t2.write('89/153', font=("Verdana",15, "normal"))
t2.color('green')

t3.up()
t3.setposition(-150,150)
t3.down()
t3.write('131/1001', font=("Verdana",15, "normal"))
t3.color('white')

t4.up()
t4.setposition(250,-200)
t4.down()
t4.write('sqrt(2)', font=("Verdana",15, "normal"))
t4.up()
t4.setposition(250,-150)
t4.down()
t4.color('blue')

for (d1, d2, d3, d4) in zip(R1, R2, R3, R4):
    t1.lt(d1 * 36)
    t1.fd(15)
    t2.lt(d2 * 36)
    t2.fd(20)
    t3.lt(d3 * 36)
    t3.fd(30)
    t3.lt(d3 * 36)
    t3.fd(30)
    t4.lt(d4 * 36)
    t4.fd(10)
done()