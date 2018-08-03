import requests, json
from pprint import pprint
class Kisi:
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
class Methods :
    def __init__(self):
        self.path = "https://reqres.in.api/users"
    def add(self,user):
        resp2 = requests.post(self.path, data={"name":user.name,"surname": user.surname.format()})

        pprint(resp2)
        pprint(resp2.json())
    def view(self):
        resp = requests.get("{self.path}?page=2".format())
        data=resp.json()
        pprint(resp)
        for sezer in data["data"]:
            for key, value in sezer.items():
                print(key,value)
    def delete(self):
        resp3=requests.delete("{self.path}/2".format())
        pprint(resp3)
    def update(self,user):
        resp4=requests.put("{self.path}/2",data={"name":user.name,"surname":user.surname.format()})
        pprint(resp4)
        pprint(resp4.json())

