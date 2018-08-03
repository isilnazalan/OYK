

#ogrenci ekle ogrenci sil ögrencileri görüntüle ana menu formu
#ögrenci ekleme öğrenci silme ögrencilerin tümünü gör while ile
# sözlük olacak eğer ogrenci eklemek istiyorsa ismini vizesini finalini alcam bunu sözlüge ekle tekrar ana menuye dön
#eğer silmek istiyorsa öğrencini varlıgını kontrol et varsa sil yoksa ogrenci bulunamadı silme pop ile
#ana menuye geri dön
#ogrencileri görüntülemek istiyorsa ogrenci listesini yazdır
#cıkıs istıyorsa cıkıs yoksa devam

ogrenciler={
    '123456': {'vize':80, "final": 90},
    '143656': {'vize':70, "final": 100}
}
#ogrenciler{}
print("ogrenci kayıt programına hosgeldınız")
while True:
    #print()
    secim=input("""
    1)ogrenci ekle(e)
    2)ogrenci sil(s)
    3)ogrencileri goruntule(g)
    4)ogrencileri_sil(d)
    5)cıkıs(c)\n""").lower()
    if secim == 'e':
        ogr_no = input("ogrencinin numarasını giriniz")
        tmp_sayac=0
        while True:
            tmp_sayac+=1
            if tmp_sayac==4:
                print("deneme hakkınız doldu")
                break
            if len(ogr_no) != 6:
                print("ogrenci numarası 6 haneli olmalıdır")
                continue
            ogr_vize = input("ogrencinin vizesini giriniz")
            ogr_final = input("ogrencinin fınal notunu giriniz")
            ogrenciler.update({ogr_no : {'vize':ogr_vize,
                                       'final' : ogr_final}})
            break
    elif secim == 'g':
        # for ogr_numara in ogrenciler:
        #     print("""ogrenci_no : {}
        #     ogrenci_vize : {}
        #     ogrenci_final : {}""".format(ogr_numara,
        #                                  ogrenciler[ogr_numara].get('vize'),
        #                                  ogrenciler[ogr_numara].get('final')))
            for ogr_numara,ogr_notlari in ogrenciler.items():
                print("""ogrenci_no: {}
                ogrenci_vize: {}
                ogrenci_fiznal:{}""".format(ogrenciler[ogr_numara],
                                             ogrenciler[ogr_numara].get('vize'),
                                             ogrenciler[ogr_numara].get('final')))
    elif secim == 's':
        silinecek_ogr_no = input("lütfen silinecek ogr noyu giriniz")
        if silinecek_ogr_no in ogrenciler.keys():
            ogrenciler.pop(silinecek_ogr_no)
            print("{} numaralı ögrenci silinmiştir.".format(silinecek_ogr_no))
        else:
            print("numaralı ogrenci sistemde bulunamadı".format((silinecek_ogr_no)))
    elif secimm == 'c':
        break
    elif secim == 'd':
        ogrenciler.clear()
        print("ogrenci listesi basarıyla temizlendi")
    else:
        print("bilinmeyen bir komut girdiniz")