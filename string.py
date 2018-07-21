test_degiskeni ="  bu bir test degiskenidir.   "
print(test_degiskeni.upper().lower())  #string dizinini önce büyük harflerle, ardından küçük harfle yazdırma komutu
print(test_degiskeni.capitalize()) #Sadece baş harfleri büyük yazdırır
print(test_degiskeni.strip()) #dışarıdaki boşlukları siler
"""
\r bir space boşluk bırakır
\n (newline) bir satır boşluk bırakır

"""
x = 5
y = 10

print( x + y )

x = "5"
y = "10"

print( x + y )
"""
iki işlem arasındaki fark, ilk işlemde x ve y integer olarak tanımlandığından toplama işlemi yapılır
ikinci işlemde x ve y string olarak tırnak içinde tanımlandığından string toplaması yapılır.
"""

x = 5
y = 2
print (type( x*y )) #type() : değişkenin tipini gösterir

print(type(x/y)) #float olarak 2.5 yazdırır
print(type (x//y)) #integer olarak 2 yazdırır

x = "5"
y = 1
z = int(x)/y

dogru = True
yanlis = False
print(dogru == False) #Ekrana 'False' yazar

liste = [x,y, "elma", dogru,z] #listelerde tip dönüşümü yapılmıyor, her değişken kendi tipini korur
liste.append("armut") #listenin sonuna ekler
print(liste [2]) #2. indexi yazdırır
liste.insert(0,"yeni") #0. index'e 'yeni' ekler

cikarilan = liste.pop() #sondaki elemanı siler
print(cikarilan)
print(liste)
liste.pop(2) #listedeki 2. elemanı siler

liste.remove( "5")# remove çıkarılan elemanın kendisini ister
print(liste)

liste2 = [5,4,3,2,1]
liste.append(liste2) #liste içine lise2'yi ekler, son eleman liste2 olur
print(liste)

print(liste.index(liste2))
liste.extend(liste2)#listedeki elemanları ayrıştırarak, birer eleman yaparak yazdırır
print(liste)

liste2.sort()#listedeki elemanları artarak sıralar
print(liste2)

liste3 = sorted(liste2)#liste2'yi değiştirmez, liste3 olarak kaydeder
print(liste3)

liste4 = [2,6,1,9,10,2]

liste4.reverse()#listeyi ters çevirir
print(liste4)

liste4.sort(reverse=True)#listeyi azalarak sıralar
print(liste4)

print(liste4.count(1))#1 elemanından kaç tane olduğunu yazdırır

print(len(liste4))#liste uzunluğunu gösterir

print(max(liste4))#listedeki en büyük elemanı gösterir










