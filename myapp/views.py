from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup
from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup
import requests
from difflib import get_close_matches
import webbrowser
from collections import defaultdict
import random
from .models import products

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
    url_flip = 'https://www.flipkart.com/search?q=' + str(key) + '&marketplace=FLIPKART&otracker=start&as-show=on&as=off'
    map = defaultdict(list)
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    source_code = requests.get(url_flip,headers = headers)
    soup = BeautifulSoup(source_code.text, "html.parser")
    home = 'https://www.flipkart.com'
    for block in soup.find_all('div', {'class': '_2kHMtA'}):
            title, price, link = None, 'Currently Unavailable', None
            for heading in block.find_all('div', {'class': '_4rR01T'}):
                title = heading.text
            for p in block.find_all('div', {'class': '_30jeq3 _1_WHN1'}):
                price = p.text[1:]
            for l in block.find_all('a', {'class': '_1fQZEK'}):
                link = home + l.get('href')
            map[title] = [price, link]
    l = 1
    prod_id1 = products() 
    prod_id2 = products() 
    prod_id3 = products() 
    prod_id4 = products() 
    prod_id5 = products() 
    for i in map:
      if l == 1:
        prod_id1.id = i
        ct = 1
        for j in map[i]:
           if ct == 1:
            prod_id1.name = j
           else:
            prod_id1.link = j
           ct += 1
      if l == 2:
        prod_id2.id = i
        ct = 1
        for j in map[i]:
           if ct == 1:
            prod_id2.name = j
           else:
            prod_id2.link = j
           ct += 1
      if l == 3:
        prod_id3.id = i
        ct = 1
        for j in map[i]:
           if ct == 1:
            prod_id3.name = j
           else:
            prod_id3.link = j
           ct += 1
      if l == 4:
        prod_id4.id = i
        ct = 1
        for j in map[i]:
           if ct == 1:
            prod_id4.name = j
           else:
            prod_id4.link = j
           ct += 1
      if l == 5:
        prod_id5.id = i
        ct = 1
        for j in map[i]:
           if ct == 1:
            prod_id5.name = j
           else:
            prod_id5.link = j
           ct += 1
      l += 1

    url_a = 'https://www.amazon.in/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=' + str(key)
    # Faking the visit from a browser
    headers_a = {
      'authority': 'www.amazon.com',
      'pragma': 'no-cache',
      'cache-control': 'no-cache',
      'dnt': '1',
      'upgrade-insecure-requests': '1',
      'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
      'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
      'sec-fetch-site': 'none',
      'sec-fetch-mode': 'navigate',
      'sec-fetch-dest': 'document',
      'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }
    map_a = defaultdict(list)
    home_a = 'https://www.amazon.in'
    proxies_list = ["128.199.109.241:8080", "113.53.230.195:3128", "125.141.200.53:80", "125.141.200.14:80",
                        "128.199.200.112:138", "149.56.123.99:3128", "128.199.200.112:80", "125.141.200.39:80",
                        "134.213.29.202:4444"]
    proxies = {'https': random.choice(proxies_list)}
    source_code_a = requests.get(url_a, headers=headers_a)
    plain_text = source_code_a.text
    soup_a = BeautifulSoup(plain_text, "html.parser")

    for html in soup_a.find_all('div', {'class': 'sg-col-inner'}):
            title, link = None, None
            for heading in html.find_all('span', {'class': 'a-size-medium a-color-base a-text-normal'}):
                title = heading.text
            for p in html.find_all('span', {'class': 'a-price-whole'}):
                price = p.text
            for l in html.find_all('a', {'class': 'a-link-normal a-text-normal'}):
                link = home_a + l.get('href')
            # print(title,link,price)
            if title and link:
                map_a[title] = [price, link]
    a_prod_id1 = products() 
    a_prod_id2 = products() 
    a_prod_id3 = products() 
    a_prod_id4 = products() 
    a_prod_id5 = products() 
    l = 1
    for i in map_a:
      if l == 1:
        a_prod_id1.id = i
        ct = 1
        for j in map_a[i]:
           if ct == 1:
            a_prod_id1.name = j
           else:
            a_prod_id1.link = j
           ct += 1
      if l == 2:
        a_prod_id2.id = i
        ct = 1
        for j in map_a[i]:
           if ct == 1:
            a_prod_id2.name = j
           else:
            a_prod_id2.link = j
           ct += 1
      if l == 3:
        a_prod_id3.id = i
        ct = 1
        for j in map_a[i]:
           if ct == 1:
            a_prod_id3.name = j
           else:
            a_prod_id3.link = j
           ct += 1
      if l == 4:
        a_prod_id4.id = i
        ct = 1
        for j in map_a[i]:
           if ct == 1:
            a_prod_id4.name = j
           else:
            a_prod_id4.link = j
           ct += 1
      if l == 5:
        a_prod_id5.id = i
        ct = 1
        for j in map_a[i]:
           if ct == 1:
            a_prod_id5.name = j
           else:
            a_prod_id5.link = j
           ct += 1
      l += 1
  
    return render(request,'counter.html',{'prod_id1': prod_id1,'prod_id2': prod_id2,'prod_id3': prod_id3,'prod_id4': prod_id4,'prod_id5': prod_id5})
    #return render(request,'counter.html',{'a_prod_id1': a_prod_id1,'a_prod_id2': a_prod_id2,'a_prod_id3': a_prod_id3,'a_prod_id4': a_prod_id4,'a_prod_id5': a_prod_id5})
    #title = soup.title
    #return render(request,'counter.html',{'products': prod_id}) 