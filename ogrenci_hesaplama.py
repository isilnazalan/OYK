
vize_final_notlari = {}

for i in range(5):
    ogrenci_ismi = input("Ogrenci ismi:")
    vize_notu  = int( input("Vize Notu ") )
    final_notu = int( input("Final Notu:") )
    vize_final_notlari.update({ogrenci_ismi: {"vize" :vize_notu,
                                              "final":final_notu}
                               })
    print(vize_final_notlari)




