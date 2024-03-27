f=open("space.txt", encoding="UTF-8") #исходный файл
data=[] #список кораблей с информацией о них
for i in range(100):
    data.append(f.readline().split("*"))
f.close()
inp=input()
while inp!="stop":
    sc=0 #буферный счётчик
    for i in data:
        if i[0]==inp: #сравнение запрошенного названия с названиями в списке
            sc+=1
            print("Корабль", i[0], "был отправлен с планеты:", i[1], "и его направление движения было:", i[3])
    if sc==0:
        print("error.. er.. ror..")
    inp=input()
