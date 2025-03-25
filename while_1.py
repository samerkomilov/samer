#bismillah
#muallif: Samer Komilov
#Dars: while tsikli ustida ishlash
#sana:21.03.2025

#buyurtma = []
#while True:
 #   kirish = "Buyurtmangizni kiriting!"
 #   kirish += "(buyurtmangizni yozgan bo'lsangiz 'exit' yoki 'quit' deb kiriting!) \n>>>"
 #   buyurtmalar = input(kirish)
 #   if buyurtmalar=='exit' or buyurtmalar=='quit':
 #       break
  #  buyurtma.append(buyurtmalar)
  #  print("Buyurtma qabul qilindi! \nRahmat")
#print("Rahmat, yana sizni kutib qolamiz!")   
    
#e_bozor = {}
#while True:
  #  kirish = "Mahsulot va uning narxini kiriting!"
  #  kirish += "(dastur yakunlash uchun 'exit' yoki 'quit' deb yozing!""\n"
   # f_chi = print(kirish)
  #  mahsulot = input("Mahsulot nomini kiriting! \n>>>""\n").lower()
  #  if mahsulot == 'exit' or mahsulot == 'quit':
   #     break
  #  narx = float(input("Mahsulot narxini raqamlarda kiriting! \n>>>""\n"))
  #  e_bozor[mahsulot] = (narx)
  #  print("Mahsulot va narx ro'yxatga kiritildi!""\n")

#print("Rahmat, dastur yakunlandi""\n")


buyurtmalar = ['olma','anjir','uzum','qovun']
mahsulotlar = {'olma':20000,
               'shaftoli':25000,
               'tarvuz':18000,
               'uzum':22000}

while buyurtmalar:
    buyurtma = buyurtmalar.pop()
    if buyurtma in mahsulotlar.keys():
        narh = mahsulotlar[buyurtma]
        print(f"{buyurtma.title()} - {narh} so'm")
    else:
        print(f"Bizda {buyurtma} yo'q")































