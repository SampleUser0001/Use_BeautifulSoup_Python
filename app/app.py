# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests

SAMPLE_URL='https://sampleuser0001.github.io/Use_BeautifulSoup_Python/html/sample.html'

def print_soup(url, bs4_constructor_args):
    print("-------------")
    print('---- start ----')
    print('URL:', url)
    print('BeautifulSoup:' , bs4_constructor_args)

    soup = BeautifulSoup(requests.get(url).text, bs4_constructor_args)

    print("---- All ----")
    # Webページをそのまま取得する。
    print(soup)

    print("---- find_all('a') ----")
    # aタグを取得する
    print(soup.find_all('a'))

    print("---- end ----")
    print("-------------")
    print()


print_soup(SAMPLE_URL, "html.parser")
print_soup(SAMPLE_URL, "lxml")
