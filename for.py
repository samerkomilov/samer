#bismillah
#Sana:07.03.2025
#Muallif: Samer komilov
#09-dasr<for tsikli>"loop" bilan ishlash

ismlar = ['Samer','Ali','Vasila','Maryam',"Rasul"]
for i in ismlar:
    print(f"Yaxshimisiz {i}")
print("Kod besh marotaba takrorlandi.")

son = list(range(10,100),10)
for s in son:
    so = (s**3)
    print(f"{s}ning kvadrati teng {so}ga")

kino = [ ] 
print("Yoqtirgan beshta kinogizni kiriting!")
for k in range(5):
    kino.append(input(f"{k+1}-kino "))
print(kino)

while True:
    try: 
        odamlar = int(input("Bugun qancha odam bilan gaplashdiz?""\n>>>")) #sonli javob soraydi yani raqam
        break
    except ValueError:
      print("\nFaqat SON kiriting!")
ism = []
for od in range(odamlar):
    ism.append(input(f"{od+1}-odam kim edi "))
print("\nSiz gaplashgan odamlar")
print(ism)
















