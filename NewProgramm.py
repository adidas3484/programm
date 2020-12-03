import requests
response = requests.get("http://himiyaklas.ru/")

#print(response.text)

START_PATTERN = 'span class="text-wrap">'
FINISH_PATTERN = '</span></a></li>'

answer = response.text
item = []
if_it_found = False

while (not if_it_found):

    index = answer.find(START_PATTERN)
    if (index == -1): if_it_found=True
    else:
        lenght = len(START_PATTERN)
        index += lenght


        index2 = answer.find(FINISH_PATTERN)
        item.append( answer[index:index2])


        answer = answer[(index2 + len(FINISH_PATTERN)):]

print (item)