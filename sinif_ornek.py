class Calisan:
    def __init__(self,isim,soyisim,maas):
        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas
        self.email = isim  + soyisim + "@asd.com"

    def GiveNameSurname(self):
        return self.isim + " " + self.soyisim

isci1 = Calisan("ışılnaz","alan","3000")

print(isci1.soyisim, isci1.isim,isci1.maas, isci1.email)
print(isci1.GiveNameSurname())