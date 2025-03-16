#bismillah
#Sana:05.03.2025
#Muallif: Samer komilov
#08-dasr<list>Ro'yxatlar ustida ishlash

#davlatlar = ['Misr','Uzbekiston','Dubai','Russia','Tailand',]
#print(davlatlar)
#print("Element soni:",len(davlatlar))
#print("Qaytargan ro'yxat:",sorted(davlatlar))
#print("Asl ro'yxat o'zgarmas qoldi:",davlatlar)
#print(sorted(davlatlar))
#print(sorted(davlatlar,reverse = True))
#print(davlatlar)
#davlatlar.reverse()
#print(davlatlar)
#davlatlar.sort()
#print(davlatlar)
#davlatlar.sort(reverse=True)
#print(davlatlar)

#sonlar = list(range(120,1200))
#print(sonlar)
#jami = sum(sonlar)
#print(jami)
#ayirma1 = min(sonlar)-max(sonlar)
#ayirma = max(sonlar)-min(sonlar)
#print(ayirma1)
#print(ayirma)
#print("Elementlar soni:",len(sonlar))
#my_sonlar = sonlar[20]
#my_sonlar_1 = sonlar[580:600]
#my_sonlar_2 = sonlar[-20]
#print(my_sonlar)
#print(my_sonlar_1)
#print(my_sonlar_2)

#taomlar = ['Osh','Palov','Manti','Somsa','Baliq']
#nonushta = taomlar[:]
#print(nonushta)
#nonushta.pop(0)
#nonushta.remove('Palov')
#nonushta.insert(0,'Quymoq')
#nonushta.append("Sut")
#print(nonushta)

#nonushta = ('Quymoq', 'Manti', 'Somsa', 'Baliq', 'Sut')
##nonushta = tuple(nonushta)
#nonushta[0] = "qaymoq non"

#ismlar = []
#for i in range(5):
       #ism = input(f"{i+1}-ismni kiriting:")
       #ismlar.append(ism)    
#print("\nIsmingizni kiriting!")
#for ism in ismlar:
       #print(ism)

sonlar = []
for s in range(5):
    while True:
        try:     
           son = int(input(f"{s+1}-Sonlarni kiriting:"))
           sonlar.append(son)
           break
        except ValueError:
           print("Iltimos faqat son kiriting")
           
           
print("\nSiz kiritgan sonlar to'plami")
for son in sonlar:
    print(son)
if sonlar:
        print("Siz kiritgan eng katta son bu:",max(sonlar))
        print("Siz kiritgan eng kichik son bu:",min(sonlar))
        print("Siz kiritgan sonlar yigindisi bu",sum(sonlar))
        print("Siz kiritgan sonlarning o'ratacha qiymati bu:",sum(sonlar) / len(sonlar))
else:
    print("Siz hech qanday son kiritmadingiz")







