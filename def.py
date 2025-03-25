#bismillah
#muallif: Samer Komilov
#Dars: Lug'atlar ustida ishlash
#sana: 24.03.2025

#from datetime import datetime
#hozirgi_yil = datetime.now().year
#def yosh_hisobla(t_yil, hozirgi_yil):
 #   """ Foydalanuvchidan tug'ilgan yilini olib,
 #  uning yoshini hisoblovchi dastur """
  #  t_yil = int(input("Iltimos, tug'ilgan yilingizni kiriting! \n>"))
   # print(f"Sizning yoshingiz {hozirgi_yil-t_yil}-da")
    
#yosh_hisobla('t_yil', hozirgi_yil)    
    

#def kvadrat_va_kub_hisobla():
 #   """ Foydalanuvchi kiritgan sonni olib uning kvadrati va kubini,
  #  hisoblab beruvchi dastur. """
  #  son = int(input("Iltimos, biron bir son kiriting! \n>>>"))
  #  print(f"{son}-ning kvadrati {son**2}-ga teng, "
 #         f"\n{son}-ning kubi {son**3}-ga teng. ")

#kvadrat_va_kub_hisobla()

#def juft_toq_sonlar():
 #   """ Foydalanuvchi kiritgan sonni olib uni juft son yoki 
 #  toq son ekanligini aniqlab beruvchi funksiya """
  #  juft = int(input("Biron bir son kiriting:"))
  #  if juft % 2 == 0 :
   #     print(f"{juft}-soni juft son")
  #  else:
    #    print(f"{juft}-soni toq son")

#juft_toq_sonlar()

#def katta_kichik_ayt():
 #   """ Foydalanuvchi kiritgan ikkita sonni olib,
  #  ularni solishtiruvchi funksiya """
  #  print("Biron bir ikkita son kiriting:")
   # a = int(input(f"{1}-sonni kiriting:"))
  #  b = int(input(f"{2}-sonni kiriting:"))
 #   if a > b :
   #     print(f"{a}-soni katta {b}-sonidan!")
   # elif b > a :
 #       print(f"{b}-soni katta {a}-sonidan!")
   # else:
   #     print(f"{a}-soni va {b}-soni teng")

#katta_kichik_ayt()

#def x_y_sonini_chiqar():
 #   """ Foydalanuvchidan x va y sonlarini olib sonlarni,
  #  konsolga chiqaruvchi funksiya """
  #  print("Iltimos, x va y sonlarini kiriting:\n")
 #   x = int(input("x sonini kiriting:"))
   # y = int(input("y sonini kiriting:"))
  #  print(f"Siz kiritgan sonlar bular {x} va {y} sonlari!")

#x_y_sonini_chiqar()


# Foydalanuvchidan x va y sonlarini olib, x^y ni konsolga chiqaruvchi funksiya yozing.
# Yuqoridagi funksiyada y uchun 2 standart qiymatini bering.
#def daraja(x,y=2):
  #  print(f"{x} ning {y}-darajasi {x**y} ga teng")

#daraja(5,2)
#daraja(3,3)
#daraja(94,4)
#daraja(6)


def qoldiqsiz_bolinish():
    """ Foydalanuvchidan son qabul qilib, 
    sonni 2 dan 10 gacha bo'lgan sonlarga qoldiqsiz bo'linishini,
    tekshiruvchi funksiya """
    son = int(input("Biron bir son kiriting:"))
    for i in range(1,11):
        if son % i == 0 :
           print(f"{son} {i} ga qoldiqsiz bo'linadi")   
            
qoldiqsiz_bolinish()
















