#bismillah
#muallif: Samer Komilov
#Dars: def:funksiya va ro'yhat 
#sana: 31.03.2025

def katta_harf(matn):
    royhatlar = []
    while matn:
        royhatlar.append(matn.pop().title())
        
    return royhatlar
royhat = ['samer', 'men', 'sen', 'ular', 'maktab', 'kitob']
matn=katta_harf(royhat[:])
print(matn)

def katta_harf(matnlar):
    for i in range(len(matnlar)):
        matnlar[i]=matnlar[i].title()   

ismlar = ['ali', 'vali', 'hasan', 'husan']
katta_harf(ismlar)
print(ismlar)

def bahola(ismlar):
    baholar = {}
    for ism in ismlar:
        if ismlar == talaba:
            baho = int(input(f"Talaba {ism.title()}ning bahosini kiriting: "))
            baholar[ism]=baho
    return baholar
talaba = ["samer", 'ali', 'vali', 'husan']
bahola=bahola(talaba)
print(bahola)
print(talaba)



















