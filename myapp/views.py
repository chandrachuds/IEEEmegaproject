from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup
import requests
from difflib import get_close_matches
import webbrowser
from collections import defaultdict
import random

# Create your views here.
def index(request):
    return render(request,'index.html')
# def counter(request):
#     text = request.POST['text']
#     amount_of_words = len(text.split())
#     return render(request,'counter.html',{'amount': amount_of_words})
def counter(request):
    text = request.POST['text']
    product_arr = text.split()
    key = ""
    count = 1
    for word in product_arr:
        if count == 1:
            key = key + str(word)
            count += 1
        else:
            key = key + '+' + str(word)
    print(key)
    #url_flip = 'https://www.flipkart.com/search?q=' + str(key) + '&marketplace=FLIPKART&otracker=start&as-show=on&as=off'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    url_flip = "https://www.codewithharry.com"
    source_code = requests.get(url_flip,headers = headers).text
    soup = BeautifulSoup(source_code.text, "html.parser")
    title = str(soup.title)
    return render(request,'counter.html',{'str': title.string}) 