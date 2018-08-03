
def fonksyon_adi():
    print("Merhaba Dünya")

fonksyon_adi()


def dilekce_gonder():
    print ("""
    Sayın Mehmet Bey,
    19.12.2009 tarihinde yaptığımız başvurunun sonuçlandırılması hususunda yardımlarınızı rica
    ederiz.
    
    saygılarımızla,
    Orçun Kunek""")

dilekce_gonder()

def selamla():
    print("Merhaba Işılnaz.")
    print("Nasılsın?")

selamla()

def tek():
    print("Girdiginiz sayı bir tek sayıdır.")

def cift():
    print("Girdiginiz sayı bir çift sayıdır.")
sayi=input("Lütfen bir sayı giriniz:")
if int(sayi) % 2 ==0:
    cift()
else:
    tek()
def selamla(isim):
    #print("merhaba,benim adım {}".format(isim))
    print("merhaba,benim adım %s" %(isim))
selamla("ışılnaz")

sayilar = [45,90,43]
a=1
for i in sayilar:
    a= a*i
print(a)



def carp(liste):
    a=1
    for i in liste:
        a = a *i
    print(a)



