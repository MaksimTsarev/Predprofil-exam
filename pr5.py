f=open("space.txt", encoding="UTF-8") #исходный файл
data=[] #список кораблей с информацией о них
f.readline()
for i in range(100):
    data.append(f.readline().split("*"))
f.close()
co=0
for i in data: #вывод информации
    if co<10:
        print("{"+i[1]+"}:{"+i[0]+"}")
        co+=1