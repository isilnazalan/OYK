
# lambda map filter reduce
def carpma (say,say2):
    return say*say2
print(carpma(2,3))

a = lambda say1,say2:say1*say2
b = lambda deger:deger
print(a(10,15))
print(b("ornek"))

carpma(3,2)
bir_dizi_var = [5,10,2,18,21,55]
string_deger = []
for deger in bir_dizi_var:
     string_deger.append(str(deger))

print(bir_dizi_var,string_deger,sep="\n")
yeni_deger = map(lambda deger:str(deger),bir_dizi_var)
print(list(yeni_deger))
print(list(yeni_deger)) #bir kere listeyi bastı, ikinci kez basması gerektiğinde bir şey olmadığından boş[] bastı

sonuc = filter(lambda say:say%2==0, bir_dizi_var)
print(list(sonuc))

#reduce
#filter
#lambda
#map
from functools import reduce

sonuc=filter(lambda say:say%2==0,bir_dizi_var)
print(bir_dizi_var)
toplam= 0
for deg in bir_dizi_var:
    toplam +=deg
print(toplam)
resp=reduce(lambda x,y:x*y, bir_dizi_var)
print(resp)