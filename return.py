#bismillah
#muallif: Samer Komilov
#Dars: return:qiymat qaytaruvchi funksiya
#sana: 26.03.2025

def oraliq(min,max,qadam=''):
    """ Bu funksiya 2 ta son qabul qilib, 
    shu ikki son orali'g'idagi sonlarni qaytaradi."""
    sonlar = []
    while min<max:
        if qadam:
           min += 2          
           sonlar.append(min)
        else:   
            sonlar.append(min)
            min += 1
    return sonlar    

print(oraliq(1, 21, 2))
print(oraliq(18, 25))

def salon_info(kompaniya,model,rangi,karobka,yili,narx=None):
    """ Avto salon uchun mashinalar ro'yxatini, 
    shakillantiruvchi funksiya """
    avto = {
           'kompaniya':kompaniya,
           'model':model,
           'rangi':rangi,
           'karobka':karobka,
           'yili':yili,
           'narx':narx
           }
    return avto 

avto1 = salon_info('GM','Damas', 'Oq', 'Mexanika', 2023, 10000)
avto2 = salon_info('GM','Labo', 'Oq', 'Mexanika', 2023)
avtolar = [avto1, avto2]   
print('Onlayn bozordagi mavjud avtomashinalar:')
for avto in avtolar:
    if avto['narx']:
        narx = avto['narx']
    else: 
        narx = "Noma'lum"
    print(f"{avto['rangi']} {avto['model']}, yili-{avto['yili']},"
          f"karobkasi {avto['karobka']}, narxi {narx}," )
        
print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")
avtolar=[] # salondagi avtolar uchun bo'sh ro'yxat
while True:
    print("\nQuyidagi ma'lumotlarni kiriting.")
    kompaniya=input("Ishlab chiqaruvchi: ")
    model=input("Modeli: ")
    rangi=input("Rangi: ")
    korobka=input("Korobka: ")
    yili=input("Ishlab chiqarilgan yili: ")
    narx=input("Narhi: ")
    
    #Foydalanuvchi kiritdan ma'lumotlardan avto_info yordamida 
    #lug'at shakllantirib, har bir lug'atni ro'yxatga qo'shamiz:
    avtolar.append(salon_info(kompaniya, model, rangi, korobka, yili, narx))
    
     #Yana avto qo'shish-qo'shmaslikni so'raymiz
    javob = input("Yana avto qo'shasizmi? (yes/no): ")
    if javob=='no':
        break
print("Salonimizdagi avtolar:")
for avto in avtolar:
    print(f"{avto['rangi']} {avto['model']}, yili-{avto['yili']},"
          f"karobkasi {avto['karobka']}, narxi {narx}," )

from datetime import datetime
hozirgi_yil = datetime.now().year
def malumotlar_bazasi(ism,familiya,t_yil,t_joy,t_raqam=None,email=None):
    """ Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, 
    email manzili va telefon raqamini qabul qilib, 
    lug'at ko'rinishida qaytaruvchi funksiya """
    info = {
        'ism':ism,
        'familiya':familiya,
        't_yil':t_yil,
        't_joy':t_joy,
        't_raqam':t_raqam,
        'email':email,
        'yoshi':hozirgi_yil-t_yil
         }
    return info
odam_1 = malumotlar_bazasi('samer', 'komilov', 2005, 'aktash', +998557068055, 'samerkomilov1876@gmail.com')
odam_2 = malumotlar_bazasi('vasila', 'komilova', 2013, 'oqtosh')
odamlar = [odam_1, odam_2]
for odam in odamlar:
    if odam['t_raqam']:
        t_raqam = odam['t_raqam']
    if odam['email']:
        email = odam['email']
    else:
        nomalum = odam['t_raqam'] 
        nomalum = odam["email"]
    print(f"\n{odam['familiya']} {odam['ism']}, {odam['t_yil']}-yilda "
          f"{odam['t_joy']}da tug'ilgan, telefon raqami {odam['t_raqam']},"
          f" email pochta manzili:{odam['email']}")


print("Mijozlarni ro'yxatga qo'shish:")
mijozlar = []
while True:
    ism = input("Mijozning ismi: ").lower()
    familiya = input("Familyasi: ").lower()
    t_yil = int(input("Tug'ilgan yili: "))
    t_joy = input("Tug'ilgan joyi:").lower()
    t_raqam = input("Telefon raqami xohlasangiz: ")
    email = input("Email manzil xohlasangiz: ")
    mijozlar.append(malumotlar_bazasi(ism, familiya, t_yil, t_joy, t_raqam, email))
    javob = input("Yana mijozlar qo'shishni xohlaysizmi? (yes/no) \n>>>").lower()
    if javob == 'no':
        break
print("Bizning mijozlar bular:")
for mijoz in mijozlar:
    print(f"\n{mijoz['familiya'].title()} {mijoz['ism'].title()}, {mijoz['yoshi']}-yoshda "
          f"{mijoz['t_joy'].title()}da tug'ilgan, telefon raqami {mijoz['t_raqam']}, "
          f"Email pochta manzili:{mijoz['email']}.")



def son_qabul_qil(son_1, son_2, son_3):
    """ Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya """ 
    eng_katta = max(son_1, son_2, son_3)  # Eng katta sonni topish
    return eng_katta

 #Funksiyani chaqirish
natija = son_qabul_qil(10, 25, 15)  # 10, 25 va 15 sonlari berildi
print(f"Eng katta son: {natija}")  # Natija: Eng katta son: 25


a = int(input("1-sonni kiriting: "))
b = int(input("2-sonni kiriting: "))
c = int(input("3-sonni kiriting: "))

print(f"Eng katta son: {son_qabul_qil(a, b, c)}")

def kattasi(x,y,z):
    max = x
    if y>=max:
        max = y
    if z>=max:
        max = z
    return max

print(kattasi(10,20,-5))

def aylana_info(radius,pi=3.14159):
    aylana = {"radius":radius,
              "diametr":2*radius,
              "perimetr":2*radius*pi,
             "yuza":pi*radius**2}
    return aylana
ay=aylana_info(5)
print(ay)

def tub_sonlar_top(min,max):    
    tub_sonlar = []    
    for n in range(min,max+1):
        tub = True
        if (n==1):
            tub = False
        elif(n==2):
            tub = True
        else:
            for x in range(2,n):
                if(n%x==0):
                    tub = False
        if tub:
            tub_sonlar.append(n)
                
    return tub_sonlar

tub=tub_sonlar_top(1,20)
print(tub)


def fibonacci(n):
    sonlar = []
    for x in range(n):
        if x==0 or x==1:
            sonlar.append(1)        
        else:
            sonlar.append(sonlar[x-1]+sonlar[x-2])
    return sonlar

print(fibonacci(10))





















