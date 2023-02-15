sammude_list=[]
f = open('sammud.txt')#Teeb .txt faili lahti
for rida in f:
    sammude_list.append(rida.strip())#Loob iga failis olevale reale listis indeksi koha
f.close()#Sulgeb faili
print(sammude_list) #Prindib sammude listi
#Int listi failitüübiks tegemine
with open('sammud.txt') as f:
    sammude_list = [ int(i) for i in f ]
sammud_kokku = sum(sammude_list) #Liidab sammude listi
print("Sammude arv kokku:" , sammud_kokku) #Sammud kokku
print("Keskmine sammude kogus:" , sum(sammude_list)/len(sammude_list))#Keskmine arvutamine
print("Väikseim sammude kogus:" , min(sammude_list)) #Vähima arvutamine
print("Suurim sammude kogus:" , max(sammude_list)) #Suurima arvutamine
