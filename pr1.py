def coord(n,m,xd,yd,t):
    '''
    Функция рассчёта координат
    n -  первая цифра номера корабля
    m - вторая цифра номера корабля
    xd, yd - координаты вектора направления
    t - количество букв в названии планеты
    '''
    if n>5:
        x=n+xd
    else:
        x=-(n+xd)*4+t
    if m>3:
        y=m+t+yd
    else:
        y=-(n+yd)*m
    return str(x)+" "+str(y) #возврат координат в виде строки


f=open("space.txt", encoding="UTF-8") #исходный файл
out=open("space_new.txt","w",encoding="UTF-8") #конечный файл
out.write(f.readline())
data=[] #список кораблей с информацией о них
for i in range(100):
    data.append(f.readline().split("*"))
for i in data:
    if i[2]=="0 0":
        a,b=i[3].split(" ")
        i[2]=coord(int(i[0][5]),int(i[0][6]),int(a),int(b),len(i[1]))
        '''
        поиск строки с отсутствющими координатами и подстановка рассчитанных координат
        a, b - буферные переменные
        '''
    out.write(i[0]+"*"+i[1]+"*"+i[2]+"*"+i[3])
    if i[0][3]=="V":
        print(i[0]," - (",i[2],")",sep="")
        #поиск и вывод корабля с последним элементом кода "V" и его координат
out.close()
f.close()