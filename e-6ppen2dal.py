a = 1 #"a" väärtus on 1
b = "a\n" #"b" väärtus on "a" koos reavahetusega
while a < 3: # Tsükkel kestab seni kuni "a" väärtus on väiksem kui 3
    print(b) # Prindib "b" väärtuse
    a +=1 #Suurendab "a" väärtust iga korraga
    
b = "'Tere!'" 
c = '"Head aega!"'
print(b) #prindib b väärtuse
print("\n") #prindib vahe
print(c) #prindib c väärtuse

a = "Tere" 
b = "Tore"
lause = a * 3 + "\\" + b #suurendab a väärtust 3 korda ja lisab b väärtuse
print(lause) #prindib muutujua lause

nimi = "loomariik"
print(nimi[0] + nimi[-1]) #Prindib muutuja esimese ja viimase tähe

nimi1 = "Paide"
nimi2 = "Türi"
print("Tere,"[0],nimi1[-5],nimi2,"!") #Valib tähti valitud sõndaest

a = "A" 
b = 1
while b < 3: # Tsükkel kestab seni kuni muutuja "b" väärtus on väiksem kui 3
    print(a,end=" ") # Prindib muutuja "a" väärtus koos tühikuga ja ei lõpeta rea vahetust
    b += 1 #lisab ühe b väärtusele
    
a = 10
b = 2
print(a > b) #Prindib True kuna a on suurem kui b

a = 10
b = 2
print(a != b and b > 10) # Vaatab kas a ei võrdu b-ga ja kas b on suurem kui 10
print(b == a or a >=0) # Vaatab kas b võrdub a-ga või kas a on suurem või võrdne 

from tkinter import * #impordib tkinteri
raam = Tk() #loob raami
raam.title("Tühi tahvel") #Raami nimeks saab Tühi Tahvel.
tahvel = Canvas(raam, width=600) #Laiuseks määratakse 600

tahvel.create_rectangle(59,70,100,100, width=2, outline="blue") # Loob ristküliku 
tahvel.create_text(50,50, text="Tere!") #Tere kordinaadid on 50, 50

tahvel.create_polygon(100,100,150,150,200,100, fill="red", outline="black") #Loob polugoni kordniaatidega ja punase ning musta värviga

tahvel.pack() #paigaldab tahvli
raam.mainloop() #käivitab akna loopi, et asi töötakse
