#dogum gunumuze kac gun kac ay kaldigini
#vve yaşı hesaplayan program
class Zaman:
    def __init__(self,tarih):
        self.gun, self.ay, self.yil = map(int,tarih.split("/"))

    def __str__(self):
        return "{gun}/{ay}/{yil}".format(gun=self.gun,
                                         ay=self.ay,
                                         yil=self.yil)
    def __sub__(self,other):
        return self.yil - other.yil


    def kalan_zaman(self,other):
        pass


if __name__ == "__main__":
    bugun_tarihi = Zaman("28/07/2018")
    dogum_gunum  = Zaman("25/11/1998")
    yasi = bugun_tarihi - dogum_gunum
    print("Yaş:{}".format(yasi))
    kalan_zaman =dogum_gunum.kalan_zaman(bugun_tarihi)
