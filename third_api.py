import requests, json
from pprint import pprint
from http import HTTPStatus


class Kisi:
    def __init__(self):
        self.name = ""
        self.surname = ""


class Methods:
    def __init__(self):
        self.path = "https://reqres.inapi/users"

    def add(self, user):
        resp = requests.post(self.path, data={"name": user.name,
                                              "surname": user.surname})
        # if resp.status_code == 201:
        #    return resp.json()
        # return {"hata":"bir hata olustu"}
        return resp.json() if resp.status_code == HTTPStatus.CREATED else json.dumps({"hata": "bir hata olustu"})

    def list_user(self):
        resp = requests.get(self.path)
        if resp.status_code == HTTPStatus.OK:
            return resp.json()
        return json.dumps({"hata": "bir hata var"})

    def update(self, user):
        resp = requests.put("{self.path}/2", data={"name": user.name, "surname": user.surname.format()})
        pprint(resp)
        pprint(resp.json())
        return resp.json() if resp.status_code == HTTPStatus.CREATED else json.dumps({"hata": "bir hata olustu"})
    def delete(self):
        resp=requests.delete("{self.path}/2".format())
        pprint(resp3)

if __name__ == '__main__':
    yeni = Methods()
    user=Kisi()
    user.name=input("İsminiz")
    user.surname = input("Soyisim")
    yeni.add(user)