ovqat = {
        'osh':15000,
        'barak':20000,
        'somsa':12000,
        'shashlik':15000,
        'jiz':20000
        }
buyurtma = []
print("Menudan uchta taom tanlang!")
for n in range(3):
    buyurtma.append(input(f"{n+1}-taom >"))
narh = 0
um = 0 
for buyurt in buyurtma:
    if buyurt in ovqat:
        narh=ovqat[buyurt]
        um = um+narh
        print(f"Sizning buyurtmangiz>>{buyurt.title()} {ovqat[buyurt]}")
    else:
        print(f"Kechirasiz, {buyurt.title()} bu taom bizda yo'q!")
print(f"\nUmumiy summa:{um} so'm")
      
       
       
       
       
       
       









































