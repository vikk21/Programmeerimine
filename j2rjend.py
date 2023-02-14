Ülesanne 1:
linnad = ["Tallinn", "Tartu", "Pärnu", "Viljandi", "Haapsalu", "Narva", "Türi"] 
for i in range (0, 6):
    linnad.sort()
    print(linnad[i])
print("Järjendis on", (len(linnad)), "linna.")

Ülesanne 2:
a = [2, 3, 1, 5]
b = [6, 4]
c = (a+b)
c.sort()
print (c)

#Ülesanne 3:
linnad = ["Tallinn", "Tartu", "Pärnu", "Viljandi", "Haapsalu", "Narva", "Türi"]
for i in range (0, 6):
    linnad.sort()
i = 1
while i < len(linnad):
    print(str(i) + ". Linn" + " on "  + "" + linnad[i])
    i += 1

#Ülesanne 4:
from turtle import* #Impordib kilpkonna

for i in range(4): 
    forward(100) #Liigub edasi kasutaja poolt sisestatud koguse.
    left(90) # Liigub vasakule 90 jagu

#Ülesanne 5:
list = [1, 2, 3, 4, 5]
total = 0
for number in list:
    total += number
print(total)
