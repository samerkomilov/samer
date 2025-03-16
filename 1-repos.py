#bismillah
#sana: 15.03.2025 #yangilandi...
#Muallif:Samer-Komilov
#6-dars Amaliyot
#Foydalanuvchi kiritgan tug'ilgan yildan kelib chiqib yoshini aniqlovchi dasturdir!

import sys

while True:
    
  ism = input("Assalomu Alaykum" "\nIsmingiz nima?" "\n>>>").strip()
  
  if ism.replace(" ","").isalpha():
      
      break
  
  else:
      
      print("Iltimos, faqat harflardan iborat bo'lgan ism kiriting!" "\n")
    
users = ['alisher1983','aziza','yasina','umar','samer',]

login = input(f"{ism} yangi login tanlang:""\n").lower()

if login in users:
    
    print('Login band, yangi login tanlang!' '\n')

else:
    print("Xush kelibsiz!",ism.title()) 
print(" ")    
print(f"{ism} bu login, '{login}' siz yana qachondir dasturga kirishingizni osonlashtiradi.")
print(" ")
print(ism.title() + " bu ism sizga juda mos keladi va chiroyli ism ekan!")
print(" ")
print(ism.title(),"keling siz bilan ozroq suxbat qilaylik!")
print(" ")
while True:

     foy_chi = input("Agar rozi bo'lsangiz 'ha' deb yozing!" " Agar xohlamasangiz 'yo'q' deb yozing"  "\n>>>" "\n").lower()
     
     if foy_chi == 'ha':
         
         break
 
     elif foy_chi in ['yoq', 'yuq', "yo'q", "yo‘q"]:
         
         print("Rahmat, xayr siz bilan tanishganimdan xursand man!")
         
         sys.exit()

     else:
         
        print("Noto‘g‘ri javob, iltimos faqat 'ha' yoki 'yo‘q' deb yozing!")
print(" ")
print("Mening ismim Samer \nMen ongli mavjudod emas man")
print(" ")
print("Men <Sun'iy Intellikt> man, ingilizchada qisqartirib <AI> deb ham aytishadi")
print(" ")
from datetime import datetime
hozirgi_yil = datetime.now().year

while True:
    try: 
        t_yil = int(input(ism.title() + " tug'ilgan yilingizni kiriting!" "\n>>>"))
        
        if len(str(t_yil)) != 4:
            
           print("Iltimos, 4 xonali yilingizni kiriting! Masalan, 2003")
    
        elif t_yil>hozirgi_yil:
            
            print("Siz kelajakda tug‘ilgansizmi? Iltimos, hozirgi yildan keyin bo‘lmagan yilingizni kiriting!")
       
        else:
        
            break
             
    except ValueError:
         
         print("Iltimos, faqat tug'ulgan yilingizni raqam bilan kiriting!") 

yosh = hozirgi_yil-t_yil

print(ism.title() + " Sizning yoshingiz",yosh,"da")

input("To'g'rimi?" "\n>>>")

print("Mening yoshim 20 da" "\n")

yashash = input(ism.title() + " aytingchi siz qayerda istiqomat qilasiz hozirda?" "\n>>>" "\n")

t_joy = input(ism.title() + " qayerda tug'ilgansiz?" "\n>>>" "\n"
              )

print("U joylar juda ham chiroyli va tozza!" "\n")

sura = [ ] 

print(f"{ism} yoqtirgan beshta 'SURANGIZNI' kiriting!" "\n")

for k in range(5):
    
    sura.append(input(f"{k+1}-Sura " "\n"))
    
print(sura)

print(" ")

input(f"{ism} siz hayvonot bog'iga kirishni xohlaysizmi?" "\n")

print("Men sizga onlayn chipta olib beraman!" "\n")

yosh = int(input("Yoshingiz nechida?" "\n"))

if yosh<=4:
    narh = 0
    
elif yosh <= 12:
    narh = 5000
    
elif yosh <= 18:
    narh = 10000
    
elif yosh >= 60:
    narh = 8000
    
else:
    narh = 15000
    
print(f"Chipta {narh} so'm")

print("")

print(f"Siz menga shu {narh}ni tashlab berishingiz kerak! " "\n")

def harf1():#bu yerga harf1 ni orniga har qanday funksiya nomini yozishimiz mumkin 
#va funksiya  nomidan keyin () bolishi shart 
#def Python'da funksiya yaratish uchun ishlatiladi.
#Bu yerda harf_turi nomli funksiya e'lon qilinmoqda.
#Funksiya bir dona argument (harf) qabul qiladi.
# bu yerda harf1 tagfidagi kodlarga teng
    unli_harflar = "aeio'uo"
    
    if harf.lower() in unli_harflar:
#harf ga kirgizilgan malumotni unli harflar ichida bor yoki yoqligini tekshiradi
#agar bolsa unli deb chiqaradi yani return ishga tushadi
#aks holda else ishga tushadi 
#foydalanuvchi kiritgan harfni kichik qiladi 
#va fofdalanuvchi harf kiritgan yoki yoqligini tekshiradi 
        return "Unli harf"
    else:
        return "Undosh harf"
#return funksiyaning natijasini qaytaradi.

#Agar harf unli harflardan bo'lsa, "Unli harf" qaytariladi,
 #aks holda "Undosh harf" qaytariladi.

harf = input(f"{ism} iltimos, biron bir harf kiriting: " "\n" "\nMen bu harf unli yoki undosh ekanligini aniqlab beraman!" "\n>>>" "\n")
if len(harf) == 1 and harf.isalpha():
#len(harf) == 1 — foydalanuvchi faqat bitta harf kiritganini tekshiradi.
#harf.isalpha() — foydalanuvchi faqat harf kiritganini tekshiradi 
#tepa----(raqam yoki boshqa belgilar kiritilmaganligini tekshiradi).
#Agar harf kiritilsa, funksiya chaqiriladi (print(harf_turi(harf))).
#Aks holda, xato xabar chiqariladi: "Iltimos, faqat bitta harf kiriting!".

    print(harf1())
else:
    print("Iltimos, faqat bitta harf kiriting!" "\n")
    
yil = int(input(f"{ism} biron bir yil kiriting" "\n" "\nMen bu yil kabisa yili yoki kabisa yili emasligini aniqlab beraman!" "\n>>>" "\n"))

if yil % 400 == 0:
    print("bu kabisa yili" "\n")
    
elif yil % 100 == 0 :
    print("bu kabisa yili emas" "\n")
    
elif yil % 4 == 0 :
    print("bu kabisa yili" "\n")
    
else:
    print("bu kabisa yili emas" "\n")    
    

while True:
    
    try:
           raqam = int(input(" Biron bir raqam yozing men uning kvadrati va kubini hisoblab aytaman sizga" "\n>>>" "\n"))
           
           if raqam < 0:
               
              print("Iltimos, musbat son kiriting" "\n")
              
              continue 
       
           break
       
    except ValueError:# aksincha
    
        print("Xatolik, Iltimos son kiriting" "\n ")
    
javob = raqam**2

javob_1 = raqam**3

print(raqam,"ning kvadrati",javob,"ga teng" "\n")

print(raqam,"ning kubi",javob_1,"ga teng" "\n")

son = input("Yana ikkita raqam yoza olasizmi?" "\nAgar tayyor bo'lsangiz 'ha' yoki 'yoq' deb yozing" "\n>>>" "\n")

if son == 'ha' :
    
    son_1 = int(input("Birinchi sonni kiriting:" "\n"))

    son_2 = int(input("Ikkinchi sonni kiriting:" "\n"))
    
    print(son_1,"*",son_2,"=",son_1*son_2)
    print(son_1,"/",son_2,"=",son_1/son_2)
    print(son_1,"-",son_2,"=",son_1-son_2)
    print(son_1,"+",son_2,"=",son_1+son_2)

if son_1 > 0:
    
    print(f"musbat son {son_1}""\n")
    
else:
    
     print(f"manfiy son {son}""\n")
     
if son_2 > 0:
    print(f"sonning ildiizi {son_2**(1/2)}ga teng!""\n")

if son == 'yoq''yuq'"yo'q":
    
   print("Rahmat, xayr ko'rishguncha!" "\n")
   sys.exit()
   
son_3 = float(input("Juft son kiriting: "))

if son_3%2==1:
    
    print("Bu son juft emas.""\n")
    
else:
    
    print("Rahmat!""\n")
   
print("Suhbatta davom etamiz""\n")

while True:
    try: 
        
        odamlar = int(input("Bugun qancha odam bilan gaplashdiz?""\n>>>""\n")) #sonli javob soraydi yani raqam
        
        break

    except ValueError:
        
      print("\nFaqat SON kiriting!""\n")
      
ism_1 = []

for od in range(odamlar):
    
    ism_1.append(input(f"{od+1}-odam kim edi ""\n"))
    
print("\nSiz gaplashgan odamlar""\n")

print(ism_1)

while True:
    try:
        
        n = int(input("Iltimos, yana biron bir son kiriting: " " \nMen sizga, siz kiritgan sonlargacha bo'lgan juft sonlar yig'indisini- \nhisoblab aytaman >>>" "\n"))
        
        if n < 0:
            
            print("Iltimos, musbat son kiriting!""\n")
            
            continue
        
        break  # To'g'ri son kiritilgan bo‘lsa, sikldan chiqamiz
        
    except ValueError:
        
        print("Xatolik! Iltimos, faqat son kiriting.""\n")

yigindi = 0  # Yig‘indini saqlash uchun o‘zgaruvchi

for i in range(0,n + 1, 2):  # 2 dan boshlab n gacha 2 qadam bilan o'tamiz

    yigindi += i  # Yig‘indiga qo‘shamiz

print(f"Juft sonlar yig‘indisi teng: {yigindi}""\n")

num = int(input(f"{ism} yana ikki yoki uch yoki undan ham kattaroq xonalik son kirita olasizmi" "\nMen uning raqamlar yig'indisini hisoblab aytaman" "\n"))#har qanday son raqam kiritilsa uning indexlar yig'indisini hisoblab beradi

summa = (num // 100) + ((num // 10) % 10) + (num % 10)  

print(summa)

print(ism.title() + " Siz bilan tanishganimdan juda ham xursand man!""\n")

print(ism.title() + " Kuninggiz xayrli va barokatli o'tsin! \nVaqtingiz uchun rozi bo'ling!""\n")





