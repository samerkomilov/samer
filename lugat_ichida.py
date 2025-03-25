#bismillah
#muallif: Samer Komilov
#Dars: Lug'atlar ustida ishlash
#sana: 19.03.2025

samer = {
        'ism':'Samer Komilov',
        'tyil':2005,
        'manzil':'Samarqand',
        'dini':'Islam',
        'kitobi':'Quran',
        'kasbi':'IT',
        'asari':['it kitobi','uni']
        }

vasila = {
        'ism':'Vasila Komilova',
        'tyil':2013,
        'manzil':'Samarqand',
        'dini':'Islam',
        'kitobi':'Quran',
        'kasbi':'Ingliz tili',
        'asari':['ingliz kitobi','kim']
        }

rasul = {
        'ism':'Rasul Komilov',
        'tyil':2000,
        'manzil':'Samarqand',
        'dini':'Islam',
        'kitobi':'Quran',
        'kasbi':'Tolib ilm',
        'asari':['robot kitobi','sen']
        }
abdu = {
        'ism':'Abdulaziz Komilov',
        'tyil':2001,
        'manzil':'Samarqand',
        'dini':'Islam',
        'kitobi':'Quran',
        'kasbi':'IT',
        'asari':['itchilar kitobi','men']}

#info = [samer, vasila, rasul, abdu]
#for inf in info:
  #  print(f"\n{inf['ism']}, "
  #        f" Tug'ilgan yili {inf['tyil']}, "
     #     f"Yashash manzili:{inf['manzil']}, "
    #      f"Qaysi dinga mansub:{inf['dini']}, "
     #     f"Kitobi:{inf['kitobi']}, "
      #    f"Kasbi:{inf['kasbi']} \n", end='')
  


#for inf in info:
 #   ism = inf['ism']
  #  asar = inf['asari']
  #  print(f"\n{ism}ning mashxur asarlari: ")
  #  for asr in asar:
  #      print(asr)


#suralar = {'samer':['fotiha', 'baqara', 'ixlos'],
 #         'vasila':['nasr','falaq','nas'],
   #        'rasul':['amma', 'yasin', 'asr']}
#for ism, sura in suralar.items():
  #  print(f"\n{ism.title()}ning yoqtirgan surasi")
   # for sur in sura:
   #     print(sur)

davlatlar = {
    'misr':{'poytaxti':'qohira',
            'aholisi':'150mln',
            'iqlimi':'issiq',
            'havo':"o'rtacha"},
    
    'uzbekiston':{'poytaxti':'toshkent',
                  'aholisi':'35mln',
                  'iqlimi':"4 fasl",
                  'havo':"o'rtacha"},
    
    'rossiya':{'poytaxti':'moskva',
              'aholisi':'150mln',
              'iqlimi':"6 oy o'rtacha 6 oy sovuq",
              'havo':'juda tozza'
              }
    }


#for davlat, malu in davlatlar.items():
 #   print(f"\n{davlat.title()}ning poytaxti {malu['poytaxti']}, "
  #        f"aholisi {malu['aholisi']}, "
   #       f"iqlimi {malu['iqlimi']}, "
    #      f"havosi {malu['havo']}")

davlat = input('Qaysi davlat haqida malumot kerak?:').lower()
if davlat in davlatlar:
    info = davlatlar[davlat]
    print(f"\n{davlat.capitalize()}ning poytaxti {info['poytaxti'].title()}"
          f"\nAholisi: {info['aholisi']} "
          f"\niqlimi: {info['iqlimi']}"
          f"\nhavo: {info['havo']}")
else:
    print("Bizda bu davlat haqida ma'lumot mavjud emas")
    









































































































