import turtle as t
t.speed(50)
length=10
color="red"
if length <= 50:
    color = "blue"
    
    
    
for i in range(500):
    t.color(color)
    t.forward(length)
    t.right(170)
    t.width=(20)
    t.circle(2)
    length=length + 2
    if length <= 50:
        color = "blue"
    if length >= 100:
        color = "green"
    if length >= 150:
        color = "red"
    if length >= 200:
        color = "purple"
    if length >= 250:
        color = "yellow"
    if length >= 300:
        color = "cyan"
    if length >= 350:
        color = "blue"
    if length >= 400:
        color = "green"
    if length >= 450:
        color ="red"
    if length >=500:
        t.speed(1000)
        t.penup()
# makes a rainbow spiral, dont ask why 

