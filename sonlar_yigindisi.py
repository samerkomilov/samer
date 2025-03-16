
# 1 dan n gacha bo'lgan juft sonlar yig‘indisini hisoblash
n = int(input("n ni kiriting: "))

yigindi = 0  # Yig‘indini saqlash uchun o‘zgaruvchi

for i in range(0,n+1, 2):  # 2 dan boshlab n gacha 2 qadam bilan o'tamiz
    yigindi += i  # Yig‘indiga qo‘shamiz,yigindi = yigindi + i

print(f"Juft sonlar yig‘indisi: {yigindi}")
