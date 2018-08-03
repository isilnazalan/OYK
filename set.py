demet=("a","b","c")
dizi=["a","b","c","a"]
kume={"a","b","c","a","a","a"}


print(demet)
print(dizi)
print(kume)

print(set(dizi))

sehir = "ankara" #str --> set
print(set(sehir))

sehir_kume = set(sehir)
for harf in sehir_kume:
    print(harf)

sehir2_kume =set("istanbul")

birlesik_kume = sehir_kume.union(sehir2_kume) #iki kumeyi birlestirir
print(birlesik_kume)

birlesik_kume = list(birlesik_kume) #kumeyi listeye çevirir
print(birlesik_kume)

print("-".join(sehir))
print("\t".join(birlesik_kume))
