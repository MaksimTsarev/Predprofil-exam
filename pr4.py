f=open("space.txt", encoding="UTF-8") #исходный файл
out=open("space_uniq_password.csv","w", encoding="UTF-8") #конечный файл
out.write("ShipName,planet,coord_place,direction,password"+"\n")
f.readline()
data=[] #список кораблей с информацией о них
for i in range(100):
    data.append(f.readline().split("*"))
f.close()
for i in data:
    pw1=i[1][-3]+i[1][-2]+i[1][-1]+i[0][2]+i[0][1]+i[1][2]+i[1][1]+i[1][0] #создание чернового варианта пароля
    pw=""
    for q in pw1:
        if 1000>ord(q)>96 or ord(q)>1071: #замена символов нижнего регистра на символы верхнего регистра
            pw=pw+chr(ord(q)-32)
        else:
            pw=pw+q
    out.write(i[0]+","+i[1]+","+i[2]+","+i[3][:-1]+","+pw+"\n") #запись в конечный файл
out.close()