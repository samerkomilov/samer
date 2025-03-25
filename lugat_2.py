#bismillah
#muallif: Samer Komilov
#Dars: Lug'atlar ustida ishlash
#sana: 18.03.2025

sura = {
        'damas':'oq',
        'bmw':'qora', 
        'volvo':'kok', 
        'gentra':'sariq', 
        'captiva':'malla', 
        'ford':'qizil', 
        'audi':'tilla rang',
        'kia':'kulrang', 
        'benelli':'yashil',
        'bmw 015':'jigar rang', 
         }

#for s in sura.items():
#    print(s)
#sorted(sura)
#for i, r in sorted(sura.items()):
  #  print(f"Mashina {i.title()} va rangi {r} \n")

#for s in sorted(sura.keys()):
  #  print(s.title())
#print("\n")
#for s in sorted(sura.values()):
   # print(s.title())    

davlat = {
    'misr':'qohira',
    'rossiya':'moskva',
    'uzbekiston':'tashkent',
    'saudiya arabiston':'ar-riyad'
    }



#print('Dunyo davlatlari:')
#for davlat_1 in sorted(davlat):
  #  print(davlat_1.upper())

#print('\nDavlatlarning poytaxtlari')
#for poytaxt in sorted(davlat.values()):
 #   print(poytaxt.title())


#dav = input("Iltimos, istalgan davlat kiriting! \n>>>")
#if dav == 'misr':
 #   print(f"{dav.title()}ning poytaxti {davlat['misr'].title()}")
#elif dav == 'rossiya':
 #   print(f"{dav.title()}ning poytaxti {davlat['rossiya'].title()}")
#elif dav == 'uzbekiston':
 #   print(f"{dav.title()}ning poytaxti {davlat['uzbekiston'].title()}")
#elif dav == 'saudiya arabiston':
 #   print(f"{dav.title()}ning poytaxti {davlat['saudiya arabiston'].title()}")
#else:
 #   print("Bizda bunday ma'lumot yo'q")

#country = input('Qaysi davlatning poytaxtini bilishni istaysiz?:').lower()
#capital = davlat.get(country)
#if capital==None:
#    print('Kechirasiz, bizda bu haqida ma\'lumot yo\'q')    
#else:
 #   print(f"{country.upper()}ning poytaxti {capital.title()} shahri")
    
    
menu = {
        'osh':20000,
        'jiz':30000,
        'baliq':90000,
        'Manti':15000,
        'jigar':20000,
        'shashlik':25000,
        'somsa':12000,
        'shurva':20000
        }
narh = 0
print("Menudan uch xil taom buyurtma bering!")

buyurtmalar = []

for n in range(3):
    
    buyurtmalar.append(input(f"{n+1}-taom:").lower())
    
jami = 0

for buyurtma in buyurtmalar:
    
    if buyurtma in menu:
        
        narh=menu[buyurtma]  #bu yerda faqat menuda bor mahsulotlarni narxi chiqadi yani f_chi tanlagan mahsulotlar narxlari      
        #chunki bu <if buyurtma in menu:> ichida bolgani uchun faqat 3ta taom ni hisoblaydi va 
        # tepani davomi> <narh=menu[buyurtma]> bu yerda {buyurtma} f_chi kiritgan taomlar boladi faqat
        
        jami = jami+narh
        
        print(f"{buyurtma.title()} {menu[buyurtma]} so'm ")
        
    else:
        
        print(f"Kechirasiz, bizda {buyurtma} yo'q.")
        
print(f"\nUmumiy summa: {jami} so'm")






