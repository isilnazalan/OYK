class Motorsiklet(object):
    #lastik = 2
    #parca = ["gidon","teker"]
    def __init__(self,lastik):
        self.lastik = lastik
    def gosterge(self):
        print(self.lastik)
    def get_lastik(self):
        return self.lastik
    def set_lastik(self,lastik):
        self.lastik = lastik

motor = Motorsiklet(2) #buraki 2, def__init__ içindeki lastik yerine geçer.
#print(Motorsiklet().lastik)
print(motor.lastik)
#class yapısında kullanılan 'def'ler funct değil method olur.
sezer_hocanin_chopperi = Motorsiklet(2)
print(sezer_hocanin_chopperi.get_lastik())


