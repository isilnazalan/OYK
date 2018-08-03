

def us_alma(deger_1,deger_2):
    sonuc = deger_1**deger_2
    print ("Sonuç: {}.".format(sonuc))
    return sonuc
try:
    deger1 = int(input("Lütfen ilk degeri giriniz"))
    deger2 = int(input("Lütfen ikinci degeri giriniz"))
    sonucu = us_alma(deger1,deger2)

except ValueError as e:
    print(e)
    print("Lütfen sayi degeri giriniz")
except Exception:
    print("Bir hata oluştu :(")
else:
    print(sonucu)

def topla_cikarma(sayi1,sayi2,topla=True):
    return sayi1+sayi2 if topla + sayi2 else sayi1 -sayi2
    #if topla:
    #   return  sayi1 + sayi2
    #return sayi1 - sayi2
topla_cikarma(3,5)

#deger1 = int(input("Lütfen ilk degeri giriniz"))
#deger2 = int(input("Lütfen ikinci degeri giriniz"))
#topla_cikarma (sayi2=deger1,sayi1=deger2)

