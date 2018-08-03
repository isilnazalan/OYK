while True:
    print("Sonsuza dek sürer")
    break#sonsuza dek sürmemesini, bu satıra gelince looptan çıkmasını sağlar

sayac = 0
while True:
    sayac += 1
    if sayac == 10:
        break
    if sayac % 2 == 0 :
        continue
    print(sayac)