from time import sleep
from requests import get
from pprint import pprint
from json import dump



if __name__ == '__main__':
    # Bir sözlük oluştur. Api'den dönen veriyi buraya her döngüde ekle
    kullanicilar = []
    api_url = "https://reqres.in/api/users/"
    # Api'ye bir istek gönder, ilk sayfayı ıaç ve kaç sayfa oldugunun bilgiini al
    ilk_resp = get(api_url).json()
    ilk_sayfa = ilk_resp.get("data")
    if ilk_sayfa:
        for sayfa in ilk_sayfa:
            kullanicilar.append(sayfa)
        pprint(kullanicilar)
        #kullanicilar.update(ilk_sayfa)
        toplam_sayfa = ilk_resp["total_pages"]

        ##Data gelmeye devam ettiği sürece döngüyü sürdür
        # Her sayfayı isteyecek bir döngü oluştur
        if toplam_sayfa and toplam_sayfa >1:
            for sayfa_numarasi in range(2,toplam_sayfa+1):
                tmp_resp = get(api_url,params={"page":sayfa_numarasi})
                data_check = tmp_resp.json().get("data")
                if data_check:
                    for tmp_kul in tmp_resp.json().get("data"):
                        # Gelen datayı oluşturduğum sözlüğe her seferinde ekle
                        kullanicilar.append(tmp_kul)
        with open("kullanicilar.json","w+") as f:
            yazdir = {"kullanicilar":kullanicilar,
                      "toplam_sayfa": toplam_sayfa}

            dump(kullanicilar,f)

        # Döngü tamamlandığında, kullanıcılar.json dosyasına yaz