a = 1
b = "a\n"
while a < 3:
    print(b)
    a +=1
    
b = "'Tere!'"
c = '"Head aega!"'
print(b)
print("\n")
print(c)

a = "Tere"
b = "Tore"
lause = a * 3 + "\\" + b
print(lause)

nimi = "loomariik"
print(nimi[0] + nimi[-1])

nimi1 = "Paide"
nimi2 = "Türi"
print("Tere,"[0],nimi1[-5],nimi2,"!")

a = "A"
b = 1
while b < 3:
    print(a,end=" ")
    b += 1
    
a = 10
b = 2
print(a > b)

a = 10
b = 2
print(a != b and b > 10)
print(b == a or a >=0)

from tkinter import *
raam = Tk()
raam.title("Tühi tahvel")
tahvel = Canvas(raam, width=600)

tahvel.create_rectangle(59,70,100,100, width=2, outline="blue")
tahvel.create_text(50,50, text="Tere!")

tahvel.create_polygon(100,100,150,150,200,100, fill="red", outline="black")

tahvel.pack()
raam.mainloop()
