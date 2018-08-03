class Sayi :
    def __init__(self,deger):
        self.deger = deger
    def __add__(self, other):
        return self.deger + other.deger


class Iki(Sayi):
    pass
class Alti(Sayi):
    pass
print(Alti(6) + Iki(2))
print(Alti(6).__add__(Iki(2)))

