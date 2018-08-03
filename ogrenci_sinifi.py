"""
class Ogrenci(object):
    def __init__(self, isim,soyisim,numara,anne_adi,baba_adi):
        self.isim = isim
        self.soyisim = soyisim
        self.numara = numara
        self.anne_adi = anne_adi
        self.baba_adi = baba_adi



class Sinif(object):
    def ogrenci_goruntule(self):
        print("N:{} İ:{} S:{}".format(
            self.numara,self.isim,self.soyisim
        ))
        sezer = Ogrenci("Sezer", "Bozkır", 120101003, "Gönül", "Can")
        sezer.ogrenci_goruntule()
    def ogrenci_sil(self,):
        self.__anne_adi=c_anne_adi

    def ogrenci_ekle(self):
        pass
    """
class Ogrenci:
    def __init__(self,isim,soyisim,numara,vize,final):
        self.isim = isim
        self.soyisim = soyisim
        self.numara = numara
        self.vize = vize
        self.final = final
    def Goruntule(self):
        print("Ogrenci ismi:{self.isim}\n".format(self.isim)
              "Ogrenci numarasi:{self.numara}\n".format(self.numara)
              "Ogrenci ortalamasi: {self.ortalamasi()}".)
    def Ortalamasi(self):
        return self.vize * 0.4 + self.final * 0.6


if __name__=="__main__":
    isim = input("Ogrencinin ismi")
    soyisim = input("Ogrencinin soyismi")
    numarasi = input("Numarasi")
    vize = int(input("Ogrenci vizesi"))
    final = int(input("Ogrenci finali"))
    ogrenci= Ogrenci(isim,soyisim,
                     numarasi,
                     final=final,
                     vize=vize)
    ogrenci.goruntule()
###EKSİK###