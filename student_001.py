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
    dosya.seek(0)#dosyanın 0'ıncı karakterine döner


