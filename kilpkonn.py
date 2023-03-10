import turtle
import random

# Avab kilpkonn.txt fail lugemiseks
with open('kilpkonn.txt', 'r') as f:
    # Loe faili read listi
    lines = f.readlines()

# Loob turtle objekt
t = turtle.Turtle()

# Määrab turtle'i algne positsioon
t.penup()
t.goto(0, 0)
t.pendown()

# Liigub läbi faili read
for line in lines:
    # Määra turtle'i pliiatsi värv juhuslikuks
    r = random.random()
    g = random.random()
    b = random.random()
    t.pencolor(r, g, b)

    # Tükelda rida sõnadeks
    words = line.strip().split()

    # Võta esimene sõna
    command = words[0]

    # Võta teine sõna (kui see olemas on)
    if len(words) > 1:
        value = int(words[1])

    # Tee käsklus
    if command == 'forward':
        t.forward(value)
    elif command == 'back':
        t.back(value)
    elif command == 'left':
        t.left(value)
    elif command == 'right':
        t.right(value)

# Küsib kasutajalt, mitu kuju ta soovib joonistada.
num_shapes = int(input("Mitu ruutu sooviksid joonistada?: "))

# Joonista soovitud arv kujusid.
for i in range(num_shapes):
    # Liigu turtle'iga juhuslikule positsioonile ekraanil
    t.penup()
    x = random.randint(-400, 400)
    y = random.randint(-400, 400)
    t.goto(x, y)
    t.pendown()

    # Määrab turtle'i pliiatsi värv juhuslikuks.
    r = random.random()
    g = random.random()
    b = random.random()
    t.pencolor(r, g, b)

    # Ruudu joonistamise valem.
    for j in range(4):
        t.forward(50)
        t.right(90)

# Sulgeb akna
turtle.done()

**********************
kilpkonn.txt file:
    
forward 100
right 72
forward 100
right 144
forward 100
right 72
forward 100
right 144
forward 100
right 72
forward 100
right 144
forward 100
right 72
forward 100
right 144
forward 100
right 72
forward 100
right 144
forward 100
right 72
forward 100
right 144
