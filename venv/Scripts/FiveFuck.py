'''
from bs4 import BeautifulSoup
import requests
import fake_useragent

link = "https://my.5ka.ru/api/v1/auth/signin"

user = fake_useragent.UserAgent().random


header = {
    'user-agent':user
}



data = {
    'login':'+7...',
    'password':	'pas...',
    'schema':'by-phone'

}

response = requests.post(link, data=data, headers = header).text

print(response)
'''


'''
import requests
from bs4 import BeautifulSoup
import json
import fake_useragent

link = "https://my.5ka.ru/api/v1/auth/signin"
user = fake_useragent.UserAgent().random

cookies = "_gcl_au=1.1.186685286.1607505336; _ga=GA1.2.1048794421.1607505336; _ym_uid=1607505337859475361; _ym_d=1607505337; _ga=GA1.3.1048794421.1607505336; _ga_GGZL4CMG0F=GS1.1.1607506423.1.1.1607506784.0; __odnoklassnikiOnBoard=%7B%22value%22%3A%22false%22%2C%22date%22%3A%222020-12-09%22%7D; TS01c37a3d=01a93f754775297d0c146437eedfb09215551ca1fb963351a4409a24935a0c4f889d77f28b38279b3e501c9c4529c78d87f7b66e54; TS1d0b9c8a027=08549da071ab2000694bfeee157cdf94baa5226bed6db87d89d03a24f0f1d96ffaa0f568bd4edcdf08f2d669a31130…13d08d02033c3cdbb7ce351f639a8e9756b5e69abf313f5bcc51ce0050b448afe761cebcd; TS010a09ac=01a93f75470a4867ebc1c8b70b1b2373ec8ab745bf8fd1a3978da9e3e96d941797a7dfca0cf4dbf3b90533fdbf2565d5ed1eb86d6879cb91448db990d3be0a42f32420af16; TS012a049e030=01df5387bb6d6197ce1d99a4b07ea52d934fbc6fbc40cbc30e672cf7a0889f6f7d3027c05aeb44edcc428b1c631d8e39f47d28278f; token=Tokenefb57889bf2f2dac6d6a6a39346a9149f17e72c3; location_id=1814; _gid=GA1.2.1945013999.1607720255; _dc_gtm_UA-77780429-1=1; _ym_isad=2; _ym_visorc_49423435=w"

cookies = {i.split("=")[0]:i.split("=")[1] for i in cookies.split(";")}

headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "content-type": "application/json;charset=UTF-8",
    "pragma": "no-cache",

    "User-Agent":user,
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "x-authorization": "Tokenefb57889bf2f2dac6d6a6a39346a9149f17e72c3",
    "cookie": ""
  }

data = {
    "login":"+79872338809",
    "password":"qwerty123",
    "schema":"by-phone"
}


response = requests.post(link, data=json.dumps(data), headers=headers, cookies = cookies).text

print (response)
'''
#response = requests.post(link, data=data, headers = header).text

import requests
from bs4 import BeautifulSoup
import json
import fake_useragent

link = "https://my.5ka.ru/api/v1/auth/signin"


s = requests.Session()
s.get("https://5ka.ru/")

user = fake_useragent.UserAgent().random

data = {
    "login":"+79872338809",
    "password":"qwerty123",
    "schema":"by-phone"
}


header = {
    "User-Agent":user
}

#Token93ed64d09d873959559050a7c7db7814dd98302a

response = s.post(link, data=json.dumps(data), headers=header)

print (response.text)



##next step


token = (json.loads(response.text.replace("'",'"')))["token"]

code = input()

data = {
    "token":token,
    "code":code
}


link = "https://my.5ka.ru/api/v1/auth/2fa"


header = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "content-type": "application/json;charset=UTF-8",
    "pragma": "no-cache",

    "User-Agent":user,
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    #"x-authorization": token,
    #"cookie": ""
}

response = s.post(link, data=json.dumps(data), headers=header)

print (response.text)

