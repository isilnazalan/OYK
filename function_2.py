def ornek_fonksiyon (*args):
    print("ahmet",sep="#", end="\n\n")
ornek_fonksiyon ("ahmet","mehmet")


def yazdirma(*args):
    print(args[:-2])
    print(args[-2])
    yazdirilacaklar = args[:-2]
    bitirici = args[-1]
    ayirici = args[-2]
    for kelime in yazdirilacaklar:
        print(kelime,end="", sep="")
        print(ayirici, end="", sep="")

    print(*yazdirilacaklar , sep=ayirici, end=bitirici)

#yazdirma("ahmet","mehmet","ayşe","fatma", "#22","\n\n")#demet

def kw_yazdirma(**kwargs):
    print(kwargs)
    print(kwargs.get("yazdirilacaklar"))
kw_yazdirma(yazdirilacaklar =["ahmet","mehmet","ayşe","fatma"],
            ayirici="#22",bitirici="bitirdik")



