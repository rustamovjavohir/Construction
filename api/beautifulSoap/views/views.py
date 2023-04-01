from django.http import HttpResponse
from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
import base64
from apps.beautifulSoap.data import data as base_data


def beautifulSoap(request):
    url = 'https://kun.uz/'
    response = requests.get(url)
    html_content = response.content

    soup = BeautifulSoup(html_content, 'html.parser')
    # title = soup.find('title').text

    title = soup.find(class_="big-news__title").text
    description = soup.find(class_="big-news__description").text
    content = soup.find(class_="big-news__content").text
    img = soup.find(class_="big-news__img").find_all('img')[0].get("src")

    # images = soup.find_all('img', {'class': 'my-class'})

    context = {
        "title": title,
        "description": description,
        "content": content,
        "img": img
    }
    return render(request, 'beautifulsoap.html', context=context)


def katm(request):
    with open(r'media/base64.txt', mode='rb') as file:
        text = file.read()

    decode_text = base64.b64decode(base_data).decode('utf-8')
    context = {
        "title": "KATM",
        "data": decode_text
    }
    with open('templates/katm/salom.html', mode='w', encoding='utf-8') as file:
        file.write(decode_text)
    return HttpResponse(decode_text)
