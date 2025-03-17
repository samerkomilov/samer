#bismillah
#muallif: Samer Komilov
#Dars: Lug'atlar ustida ishlash
#sana: 17.03.2025
dadam = {'ism' : 'Ashurov sobir', 'yosh' : 1977, 'manzil' : 'Samarqand viloyati, Narpay tumani'}
ayam = {'ism' : 'Ashurova Mahfuza', 'yosh' : 1980, 'manzil' : 'Samarqand viloyati, narpay tumani'}
akam = {'ism' : 'komilov abdulaziz', 'yosh':2001,'manzil':'Samarqand viloyati, narpay tumani'}
akam_1 = {'ism':'komilov rasul', 'yosh':2000, 'manzil':'Samarqand viloyati, narpay tumani'}
momam = {'ism':'arziqulova mohira', 'yosh':1954, 'manzil':'samarqand viloyati narpay tumani'}
#print(f"Momamning ismi {momam['ism'].title()}, {momam['yosh']}-yilda, {momam['manzil'].title()}da tug'ilgan\
  #    \nDadamning ismi {dadam['ism'].title()}, {dadam['yosh']}-yilda, {dadam['manzil'].title()} tug'ilgan\
#      \nAyamning ismi {ayam['ism'].title()}, {ayam['yosh']}-yilda, {ayam['manzil'].title()}da tug'ilgan\
 #     \nAkamning ismi {akam['ism'].title()}, {akam['yosh']}-yilda, {akam['manzil'].title()}da tug'ilgan\
  #    \nAkamning ismi {akam_1['ism'].title()}, {akam_1['yosh']}-yilda, {akam_1['manzil'].title()}da tug'ilgan")
      
oilam = {'momam_i':'momamning', 'momam_o':'shurva',
         'dadam_i':'dadamning', 'dadam_o':'osh',
         'ayam_i' :'ayamning', 'ayam_o':'barak',
         'akam_i':'akamlarning','akam_o':'shashlik'
         } 
#print(f"{oilam['momam_i'].title()} sevimli taomi {oilam['momam_o']}.\
  #    \n{oilam['dadam_i'].title()} sevimli taomi {oilam['dadam_o']}.\
  #    \n{oilam['ayam_i'].title()} sevimli taomi {oilam['ayam_o']}.\
  #    \n{oilam['akam_i'].title()} sevimli taomi {oilam['akam_o']}.")      
      
     
lugat = {'variable':"o'zgaruvchi",'tar':'unga har qanday vaqtda har xil nomlar berish mumkin',
         'string':'matn', 'tar_0':"bu, matn ko'rishdagi xabarlardir",
         'integer':"birlik son ko'rinishi", "tar_1":"unga misol 10, 20, 30",
         'float':"o'nlik son ko'rinishi", "tar_2":"unga misol 10.5, 20.25",
         'if':'agar','tar_3':"misol agar bu bo'lsa bunday qil",
         'else':'aksincha', 'tar_4':"misol aksincha bunday qil bu 'if' ga bog'liq",
         'elif':'agar aksincha', 'tar_5':'misol agar aksincha bunday qil',
         'for':'takrorlash', 'tar_6':"bu <for loop> takrorlash sikli bo'lib xizmat qiladi",
         'upper()':'katta harf', "tar_7":"bu matnni barcha harfni katta harfga o'zgartiradi",
         'lower()':'kichik harf', 'tar_8':"bu, matnni barcha harflarini katta harfga o'zgartiradi",
         'title()':'boshlangich katta harf', 'tar_9':"bu, matnni barcha boshlang'ich harflarini katta harfga o'zgartiradi",
         'isdigit()':'harf ekanligini tekshiradi', "tar_10":"bu, input orqali kiritilgan malumotni son yoki belgilar emasligini tekshiradi"}

f_chi = input("lug'atni yozing" "\n>>>")      
if f_chi == 'variable':
    print(f"Bu lugat pythonda {lugat['variable']} manosini beradi, va {lugat['tar']}")
elif f_chi == 'string':
    print(f"Bu lugat pythonda {lugat['string']} manosini beradi, va {lugat['tar_0']}")
elif f_chi == 'integer':
    print(f"Bu lugat pythonda {lugat['integer']} manosini beradi, va {lugat['tar_1']}") 
elif f_chi == 'float':
    print(f"Bu lugat pythonda {lugat['float']} manosini beradi, va {lugat['tar_2']}")      
elif f_chi == 'if':
    print(f"Bu lugat pythonda {lugat['if']} manosini beradi, va {lugat['tar_3']}")     
elif f_chi == 'else':
    print(f"Bu lugat pythonda {lugat['else']} manosini beradi, va {lugat['tar_4']}")      
elif f_chi == 'elif':
    print(f"Bu lugat pythonda {lugat['elif']} manosini beradi, va {lugat['tar_5']}")    
elif f_chi == 'for':
    print(f"Bu lugat pythonda {lugat['for']} manosini beradi, va {lugat['tar_6']}")      
elif f_chi == 'upper()':
    print(f"Bu lugat pythonda {lugat['upper()']} manosini beradi, va {lugat['tar_7']}")   
elif f_chi == 'lower()':
    print(f"Bu lugat pythonda {lugat['lower()']} manosini beradi, va {lugat['tar_8']}")   
elif f_chi == 'title()':
    print(f"Bu lugat pythonda {lugat['title()']} manosini beradi, va {lugat['tar_9']}")    
elif f_chi == 'isdigit':
    print(f"Bu lugat pythonda {lugat['isdigit']} manosini beradi, va {lugat['tar_10']}")
else:
    f_chi != lugat
    print("Kechirasiz, Bu so'z lug'atda yo'q")
    
    
    
    
    
    
    
    
    