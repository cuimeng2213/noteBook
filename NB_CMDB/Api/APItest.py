#coding:utf-8
"""
import json
from urllib import parse
from urllib import request

url = "http://192.168.1.25:8000/api/CMDBApi/"
user_pasw = {
        "username": "while",
        "password": "123456"
    }
json_data = json.dumps(user_pasw)

data = {
    "type": "login",
    "data": user_pasw,
    "token": ''
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
}
sendData = parse.urlencode(data).encode()

req = request.Request(url = url,headers = headers,data = sendData)

response = request.urlopen(req)

result = response.read().decode()

print(result)


import json
from urllib import parse
from urllib import request

url = "http://127.0.0.0:8000/api/CMDBApi/"

headers = {
}
"""
#coding:utf-8

import json
from urllib import parse
from urllib import request

url = "http://127.0.0.1:8000/api/CMDBApi/"

headers = {
}

userData = {
   "username": "cuimen",
   "password": "cm123456"
}


userData = json.dumps(userData)
login_data = {
   "type": "login",
   "data": userData,
   "token": ""
}
sendData = parse.urlencode(login_data).encode()

req = request.Request(url = url,headers = headers,data = sendData)

response = request.urlopen(req)

content = response.read()


print(content)



