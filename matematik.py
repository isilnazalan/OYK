# buradaki * tüm kütüphaneyi çeker
#from math import sqrt
#math kütüphanesinin kullanımına, içindekilere bakmak için math. yapmalıyız
#print(math.sqrt(16))
#yarıçapı girilen dairenin çevresini ve alanını bulun
#from math import pi
import math
r =6
alan = (math.pi) * r * r
print(alan)
cevre = 2*(math.pi) * r
print(cevre)



def uzaklik(*args):
    x1,x2,y1,y2 = args
# x1 = args[0]
# x2 = args[1]
# y1 = args[2]
# y2 = args[3]

    uzunluk = math.sqrt((math.pow(x1- x2,2) + math.pow (y1 - y2,2)))
    print(uzunluk)

uzaklik(1,6,14,2)
import random
def uzaklik2(*args):
    sonuc = sqrt(
        (args[2]-args[0])**2)
         +
         (args[3] - args[1])**2)
        )
    return sonuc
def main():
    x1,y1,x2,y2 = random.randint(1,20),\
                  random.randint(1,20),\
                  random.randint(1,20),\
                  random.randint(1,20)
    sonuc = uzaklik(x1,y1,x2,y2)
    print(f"({x1},{y1} ile ({x2}, {y2})",\
          f"arasındaki uzaklık:{sonuc}")
main()

"""def main(), if __name__ =="__main__": aynı anlama gelir. ancak fonksyonumuzun başka bir projede çalışmamasını istiyorsak
sadece kendi projesinde çalışsın istiyorsak if'li koşulu kullanırız.