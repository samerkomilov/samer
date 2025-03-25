#bismillah
#muallif: Samer Komilov
#Dars: while tsikli ustida ishlash
#sana:21.03.2025

#kitob = ("Iltimos, yoqtirgan kitoblaringizni kiriting? ")
#kitob += "(barcha kitoblarni kiritib bo'lgach 'exit' deb yozing): "
#f_chi = ""
#while True:
 #   if f_chi == 'exit':
 #       break
  #  else:
  #      f_chi = input(kitob)
#print('rahmat')        
    
#savol = "iltimos, yoshingizni kiriting!"
#savol += " \nNarhni olgandan so'ng 'exit' yoki 'quit' deb yozing \n>>>"

#while True:
 #   f_chi = input(savol)  
  #  if f_chi == 'exit'or f_chi =='quit':
    #    break
 #   f_ch = int(f_chi) 
    
  #  if f_ch<7:
  #      narh = 2000
  #  elif 7<=f_ch<18:
 #       narh = 3000
 #   elif 18<=f_ch<65:
 #       narh = 10000
 #   else: narh = 0
    
 #   if narh==0:
  #      print("Sizga chipta bepul")
 #   else:
   #     print(f"Chipta {narh} so'm")
      
#print("rahmat")


#savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
#savol += "Musbat son kiriting "
#savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

#while True:
 #   qiymat = input(savol).lower()
 #   if float(qiymat)<0:
  #      continue
  #  elif str(qiymat)=='exit':
  #      break
  #  else:
   #     ildiz = float(qiymat)**(0.5)
   #     print(f"{qiymat} ning ildizi {ildiz} ga teng")
savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if qiymat=='exit':
        break
    elif float(qiymat)<0:
        continue## agar foydalanuvchi manfiy son kiritsa tsiklni takrorlaymiz
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")
print("Rahmat, dastur tugadi!")



print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
savol = "Istalgan son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
ishora = True
while ishora:
    qiymat = input(savol)
    if qiymat == 'exit':
        ishora = False
    else:
        print(float(qiymat)**2)

sonlar = list(range(1,11))
for son in sonlar: 
    if son == 5: # son 5 ga teng bo'lsa kod to'xtaydi
        break
    print(f"{son} ning kvadrati {son**2} ga teng")


sonlar = list(range(1,11))
for son in sonlar:
    if son == 5: # son 5 ga teng bo'lsa tiskl boshiga qaytadi
        continue
    print(f"{son} ning kvadrati {son**2} ga teng")


























