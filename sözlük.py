sozluk = {'one':'bir','two':[2,10,3,1]}
print(sozluk.get('two'))
#sözlüklerde değişkenler bir değer alır
#anahtar kilit uyumu vardır

sozluk['one'] = 1 #one değeri 1 olarak değiştirilir
print(sozluk)

sozluk.update({'two':2})#sozlüğü günceller ya da yeniler
sozluk.update({'three':3})
print(sozluk)

sozluk['four'] = 4
print(sozluk)

del sozluk['one'] #sozlukten öge siler
print(sozluk)


print(sozluk.pop('two')) #two'nun karşılığını(degerini) verir

print(sozluk.keys())  #butun key'leri yazdırır
print(sozluk.values()) #değerleri yazdırır
print(sozluk.items())

# {"key"  : "value"}
# {"kişi" : "telefon num"}