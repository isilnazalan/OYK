import random
numb=random.randint(1,6)
print(numb)
def tahmin():
    guess=int(input("tahmin giriniz"))
    if guess!=numb:                            
        print("yanlış")


    elif guess==numb:
        print("doğru")
        a=100+1
        print(a)


def main():
    while True:
        answer=input("cikmak istiyorsaniz cevap giriniz:E/H")
        if answer=="H":
            continue
        elif answer=="E":
            print(sonuc)
            break
main()