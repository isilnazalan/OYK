import requests
from reqres import Methods

class Konsol:
    def __init__(self):
        self.choice = ""
    def menusu (self):
        choices_list=["1","2","3","4"]
        print("Menuye hosgeldiniz")
        while True:
            print("""
            islemler
            1.ekle
            2.goruntule
            3. sil
            4.guncelle
            """)
        self.choice=giris ("Seciminiz")
        if self.choice in choices_list:
            pass
        print("Bir secim numarasi girdiniz")
    def secim(self):
        user = Methods()
        if self.choice == "1":
            user.ekle(self.get_user())
        elif self.choice == "2":
            user.goruntule()
        elif self.choice == "3":
            user.silme()
        elif self.choice == "4":
            user.guncelle(self.get_user)
    def calistirmak(self):
        self.menu()
        self.secim()
@staticmethod
def get_user():
    ornek = Methods()
    ornek.name = input("isim :")
    ornek.surname= input("soyisim :")
    return ornek

if __name__ == "__main__":
    c = Konsol()
    c.run()