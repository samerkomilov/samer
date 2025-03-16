#Sana:11.03.2025
#Muallif:Samer Komilov
#Loyihalar ustida ishlash

# Sana: 11.03.2025
# Muallif: Samer Komilov
# Magazindagi xaridlarni hisoblash

print("Assalomu Alaykum!\nXush kelibsiz, Hurmatli mijoz!\nBizning magazinimizga")

# Mahsulotlar va narxlar
mahsulotlar = {
    'Non': 4000,
    'Makaron': 10000,
    'Vafli': 10000,
    'Gazli ichimliklar': 8000,
    'Kolbasa': 25000,
    'Shokalad': 12000,
    'Qaymoq': 20000,
    'Sut': 10000,
    'Kartoshka': 18000,
    'Piyoz': 15000,
}

# Mavjud mahsulotlarni ko'rsatish
xaridor_xohishi = input("Bizda mavjud mahsulotlarni ko'rishni xohlaysizmi? (ha/yo'q): ").lower()
if xaridor_xohishi == "ha":#agar ha deb yozsa printni chiqar
    print("Bizda quyidagi mahsulotlar bor:")
    for mahsulot, narx in mahsulotlar.items():#mahsulot bu yerda lug'atning yani magazinda bor mahsulotlarning kalit qismi yani non sut v.h.z
        print(f"{mahsulot}: {narx} so'm")#mahsulot va narx bu yerda royhatni chiqarish uchun print bilan
if xaridor_xohishi == "yoq":
    print("Tashrifingiz uchun rahmat, Yana sizni kutib qolamiz!")
        

# Xarid qilish
tanlangan_mahsulotlar = input("\nSiz nimalarni xarid qilmoqchisiz? Mahsulot nomlarini vergul bilan kiriting:\n>>> ").title()
tanlangan_royxat = tanlangan_mahsulotlar.split(", ")

umumiy_narx = 0
mavjud_mahsulotlar = []
nomavjud_mahsulotlar = []

for mahsulot in tanlangan_royxat:
    if mahsulot in mahsulotlar:
        mavjud_mahsulotlar.append(mahsulot)
        umumiy_narx += mahsulotlar[mahsulot]
    else:
        nomavjud_mahsulotlar.append(mahsulot)

# Natijalarni chiqarish
if mavjud_mahsulotlar:
    print("\nSiz xarid qilgan mahsulotlar:")
    for mahsulot in mavjud_mahsulotlar:
        print(f"- {mahsulot}: {mahsulotlar[mahsulot]} so'm")
    print(f"\nUmumiy narx: {umumiy_narx} so'm")

if nomavjud_mahsulotlar:
    print("\nQuyidagi mahsulotlar bizda mavjud emas:")
    for mahsulot in nomavjud_mahsulotlar:
        print(f"- {mahsulot}")

print("\nRahmat! Yana keling!")















