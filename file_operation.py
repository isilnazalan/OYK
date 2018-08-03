"""
with open("ornek.txt", "a+") as f:
    komple = f.read()
    print(komple)
    print(f.tell())
    f.seek(0)
    ilk_5 = f.read(5)
    print(ilk_5)
    print(f.tell())


ogrenciler = {
    "120101003":{"vize": 80, "final": 90},
    "120101004":{"vize": 30, "final": 50}
}
with open ("ogrencilerim", "a+") as f:
    for ogr_no, notlar in ogrenciler.items():
        f.write("{} {} {}".format(ogr_no,
                                  notlar.get("vize"),
                                  notlar.get("final")))
        #strip() \n'leri göstermez
        #split()("") boşluklara dikkat ederek her birini diziye çevirir
"""

with open ("ogrencilerim") as f:
    oku =f.read()
    print(oku)
