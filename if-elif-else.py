#0-40 dc
#41-60 cb
#61-80 bb
#80-100 aa
from builtins import print, int
"""
vize = int(input("Notunuzu girin:"))
final = int(input("Final notunuzu girin:"))
"""
"""

if type(vize) == "int" and type(final) == "int":
    if 0 < vize < 100 and 0 < final < 100:
        kul_not = (vize*10/100) + (final*60/100)

        if 0 < kul_not <= 40:
            print("Notunuz dc")
        elif 40 < kul_not <= 60:
            print("Notunuz cb")
        elif 61 < kul_not <= 80:
            print("Notunuz bb")
        elif 81 < kul_not <= 100:
            print("Notunuz aa")
        else:
            print("Tanımsız")
"""

def ortalama_hesapla(gecici_vize, gecici_final):

    if type(vize) == int and type(final) == int:
        if 0 < vize < 100 and 0 < final < 100:
            kul_not = (vize * 10 / 100) + (final * 60 / 100)

            if 0 < kul_not <= 40:
                print("Notunuz dc")
            elif 40 < kul_not <= 60:
                print("Notunuz cb")
            elif 61 < kul_not <= 80:
                print("Notunuz bb")
            elif 81 < kul_not <= 100:
                print("Notunuz aa")
            else:
                print("Tanımsız")
    else:
        print("Lütfen sayi giriniz")

        ogr_1_vize = int(input("İlk öğrencinin vizesini giriniz"))
        ogr_1_final = int(input("ilk öğrencinin finalini girin"))
        ortalama_hesapla(ogr_1_vize, ogr_1_final)
