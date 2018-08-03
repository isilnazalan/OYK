class Sinif:
    def __init__(self,ozellik):
        self.ozellik=ozellik

guncel = setattr(Sinif,"ornek","degeri")
print(guncel,Sinif.ornek)
resp=getattr(Sinif,"ornek")
print(resp)
resp_2=hasattr(Sinif,"baska")
print(resp_2)
delattr(Sinif,"ornek")
# print(Sinif.ornek)
