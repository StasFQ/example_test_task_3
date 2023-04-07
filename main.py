import requests
from bs4 import BeautifulSoup

file = 'Enter your file path here'

with open(file, 'r') as f:
    data = f.readlines()

for i in data:
    responce = requests.get(i)
    if responce.status_code == 200:
        list = []
        soup = BeautifulSoup(responce.content, 'html.parser')
        text = soup.get_text()
        words = [word.strip('.,!;()[]') for word in text.split()]
        for word in words:
            if word not in list:
                list.append(word)

        print(list)
