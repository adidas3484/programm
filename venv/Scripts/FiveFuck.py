
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

