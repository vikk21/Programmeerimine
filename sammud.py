sammude_list=[]
f = open('sammud.txt')#teeb .txt faili lahti
for rida in f:
    sammude_list.append(rida.strip())#loob iga failis olevale reale listis indeksi koha
f.close()#sulgeb faili
print(sammude_list) #prindib sammude listi
#listi int failitüübiks tegemine
with open('sammud.txt') as f:
    sammude_list = [ int(i) for i in f ]
sammud_kokku = sum(sammude_list) #liidab sammude listi
print("Sammude arv kokku:" , sammud_kokku)
print("Keskmine sammude kogus:" , sum(sammude_list)/len(sammude_list))#keskmine arvutamine
print("Väikseim sammude kogus:" , min(sammude_list)) #vähima arvutamine
print("Suurim sammude kogus:" , max(sammude_list)) #suurima arvutamine
