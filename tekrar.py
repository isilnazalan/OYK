#print
print("Burası çok güzel sen de gelsene")
yuz_olcumu = "200"
tevellut = "1990"
print("Bizim köyün yüz ölçümü " + yuz_olcumu +"tevellutu " + tevellut) #biri str biri int, çalışmaz
print("Bizim köyün yüz ölçümü {} tevellütü {}".format(yuz_olcumu,tevellut))
print("Bizim köyün yüz ölçümü {yo} tevellütü {tv}".format(yo=yuz_olcumu, tv=tevellut))



#degisken turleri
ilk    = "ornek"
iki    = 10
uc     = 10.0
boolean= True



#input



#liste
bu_bir_listedir = ["bir","kac","tane","degisken"]
#bu_bir_listedir.append({"bu":"sozluktur"}) #listenin son elemanı bir sözlük olur
print(bu_bir_listedir)

for degisken in bu_bir_listedir:
    print(degisken)
    if type(degisken) == dict: #son eleman olan sözlüğü yazdırır
        print(degisken)
        print(degisken.get("bu")) #son elemanı sözlük olanın value'su yazdırılır
print(bu_bir_listedir [3][0:5])

bu_bir_listedir.sort()#önce işlemi yaptırıp sonra yazdırabiliriz, print içinde sort yapmaz
print(bu_bir_listedir)

siralanmis_liste = sorted((bu_bir_listedir))
print(siralanmis_liste)

#sözlük
meyveler = {"yaz":
    {"sevdiklerimiz":{"avokado","guantanamo elması","çarkıfelek"},
     "sevmediklerimiz":{"elma","armut","kiraz"}
     },
            "kis":{
                "ozlediklerimiz":"portakal çilek mandalina",
                "efsaneler":0
            }}


cumle = "bu bir cümledir"
cumle=cumle.replace("b", "*")
print(cumle)


sozluk = {"ilk", "iki","üç"}
print(type(sozluk))

#demetler-kumeler

#koşullu ifadeler
if 10 is 10:
    pass
if 10 ==10:
    pass
#döngüler for, while
for i in range(1,10,2):
    print(i)

sayilar = []
for say in range (1,10): #bir listeyi 1den 10a kadar sayılardan oluşturmak
    sayilar.append(say*say)
    #sayilar=[say*say for say in range(1,10)]
    #sayilar2=[say*say for say in range(1,10) if say % 2 == 0] #2yle modu 0 olan sayılrın karesini basar
    #print(sayilar2)
print(sayilar)



#fonks
def yazdir(kelime):
    print(kelime)
    return 10

yazdir("meyve")
def args_yazdir(*args):
    print(args)
    yazdir("meyve")

def arg_yazdir(ilki,ikinci,*args):
    print(args)
arg_yazdir(1,2,3,4,5,6)

def kwargs_yazdir(bir,**kwargs): #girilen parametreleri sözlük gibi gösterir
    print(kwargs)
    print(bir)
kwargs_yazdir(bir=1,iki=2)

def args_kwargs_yazdir(ilki, ikinci, *args,bir=1,
                       **kwargs):
    print(ilki)
    print(ikinci)
    print(args)
    print(bir)
    print(kwargs)
args_kwargs_yazdir(9,8,7,6,bir=1,iki=2)



#dosya işlemleri
def dosya_ac (dosya_ismi):
    dosya = open(dosya_ismi, "r")
    return dosya
dosya = dosya_ac("dosya.txt")
#print(dosya.readline())
print(dosya.readlines())
#print(dosya.read())
def dosya_oku (dosya):
    return dosya.read()
def dosya_yaz(dosya, *args):
    pass

def dongu():
    for i in range(1,10):
        yield str(i)
for x in dongu():
    print(x)



#hata yakalama

#kwargs - args
#(len, type, range)