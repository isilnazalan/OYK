"""
dosya=open("file.txt") #dosyayı açar
icerik = dosya.read() #dosyayı okur
print(icerik) #dosyayı okur
print(dosya.readlines())

dosya.close()

"""
#dosya = open("file.txt")
#satirlar= dosya.readlines()
#print(*satirlar)

# r -> read
# w -> write
# a -> append
# x -> create

try:
    dosya = open("file.txt")
    icerik = dosya.readlines()
    temizlenmis_icerik = []
    for satir in icerik:
        temizlenmis_icerik.append(satir.strip())
        print(temizlenmis_icerik)
    dosya.close()
except Exception as e:
    print(e)
    print("Dosya yoktur.")
#PEP8 standartı

ogrenciler = {
    "120101003":{"vize": 80, "final": 90},
    "120101004":{"vize": 30, "final": 50}
}
try:
    dosya = open("student.txt","a+")
except Exception:
    dosya = open("student.txt", "x")
for ogr_no, notlar in ogrenciler.items():
    dosya.write("{} numarali ogrencinin vizesi :{} finali: {}".format(ogr_no,
                                                                      notlar.get("vize"),
                                                                      notlar.get("final")))