Ülesanne 1:
linnad = ["Tallinn", "Tartu", "Pärnu", "Viljandi", "Haapsalu", "Narva", "Türi"] #Defineerib järjendid
for i in range (0, 6): #Teeb range vahemiku
    linnad.sort() #sorteerib linnad tähestiku järjekorras
    print(linnad[i]) #prindib linnad kindla vahemikuga
print("Järjendis on", (len(linnad)), "linna.") #Koostab lause nummerdatud järjekorraga

Ülesanne 2:
a = [2, 3, 1, 5] #a väärtus
b = [6, 4] #b väärtus
c = (a+b) #liidab a ja b väärtuse ja teeb selle c-ks
c.sort() #sorteerib c 
print (c) #prindib c

#Ülesanne 3:
linnad = ["Tallinn", "Tartu", "Pärnu", "Viljandi", "Haapsalu", "Narva", "Türi"] #Defineerib järjendid 
for i in range (0, 6): #Teeb range vahemiku
    linnad.sort() #Sorteerib "linna" järjendi
i = 1 #defineerib i väärtuse
while i < len(linnad): #nummerdab järjekorra
    print(str(i) + ". Linn" + " on "  + "" + linnad[i]) #liidab kogu lause kokku tehete ja väärtustega
    i += 1 #lisab i-le juurde ühe

#Ülesanne 4:
from turtle import* #Impordib kilpkonna

for i in range(4): #defineerib i väärtuse
    forward(100) #Liigub edasi kasutaja poolt sisestatud koguse.
    left(90) # Liigub vasakule 90 jagu

#Ülesanne 5:
list = [1, 2, 3, 4, 5] #teeb listi numbritega
total = 0 #koguväärtus on 0
for number in list: #liidab numbri listiga
    total += number #lisab total väärtusele juurde numbri väärtuse
print(total) #prindib kogu vastuse
