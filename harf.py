#bismillah 
#sana:13.03.2025
#harf_turi bu yerda o'zgaruvchi bo'lish kerak
#harf bu o'zgaruvchi ichidagi narsa ism yoki raqam

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

harf = input("Biron bir harf kiriting: ")
if len(harf) == 1 and harf.isalpha():
#len(harf) == 1 — foydalanuvchi faqat bitta harf kiritganini tekshiradi.
#harf.isalpha() — foydalanuvchi faqat harf kiritganini tekshiradi 
#tepa----(raqam yoki boshqa belgilar kiritilmaganligini tekshiradi).
#Agar harf kiritilsa, funksiya chaqiriladi (print(harf_turi(harf))).
#Aks holda, xato xabar chiqariladi: "Iltimos, faqat bitta harf kiriting!".

    print(harf1())
else:
    print("Iltimos, faqat bitta harf kiriting!")