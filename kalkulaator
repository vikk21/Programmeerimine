class Calculator: #kalkulaator klass
    def liida(self, a, b): #loob klassi
        return a+b #lõpus toob välja arvutuse
    
    def lahuta(self, a, b):
        return a-b
        
    def korruta(self, a, b):
        return a*b

    def jaga(self, a, b):
        return a/b
    
    def ruutjuur(self, a, b):                 
        return a ** b
    
    def jääk(self, a, b):                     
        return a % b

#loob kalkulaatori
my_cl = Calculator()

while True: #jääb kordama while tsüklit

    print("1: Liitmine")
    print("2: Lahutamine")
    print("3: Korrutamine")
    print("4: Jagamine")
    print("5: Ruutjuur")
    print("6: Jääk")
    print("7: Välju")
    
    ch = int(input("Vali ülesanne: ")) #Küsib sisestust
    
    #Märgib sisestatavad valikud
    if ch in (1, 2, 3, 4, 5, 6, 7):
        
        if(ch == 7): #katkestab while loopi kui kasutaja sisestab "7"
            break
              
        a = int(input("Lisa esimene number: ")) #küsib numbri sisestust.
        b = int(input("Lisa teine number: "))
        
        if(ch == 1):
            print(a, "+", b, "=", my_cl.liida(a, b)) #prindib vastuse
        elif(ch == 2):
            print(a, "-", b, "=", my_cl.lahuta(a, b))
        elif(ch == 3):
            print(a, "*", b, "=", my_cl.korruta(a, b))
        elif(ch == 4):
            print(a, "/", b, "=", my_cl.jaga(a, b))
        elif(ch == 5):
            print(a, "**", b, "=", my_cl.ruutjuur(a, b))
        elif(ch == 6):
            print(a, "%", b, "=", my_cl.jääk(a, b))
    
    else:
        print("Vigane sisestus") #kui ükski eelnevatest ei töödanud siis tuleb veateade.
