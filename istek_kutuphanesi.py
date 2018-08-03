import requests
#pip install requests
#sudo apt install python3-requests
url = "https://sezerbozkir.com"
bilgi = {"page":1,"rows":10}

#GET ile istek
response_get = requests.get(url,params=bilgi)

#POST ile istek
response_post = requests.post(url,data=bilgi)

##status
print(response_post.status_code)
print(response_get.status_code)

##¶aw response paketinin body
print(response_get.content)
print(response_post.text)