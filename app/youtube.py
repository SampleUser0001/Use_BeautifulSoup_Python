# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import re
import ast

YOUTUBE_URL='https://www.youtube.com/watch?v=iZDDXbzK7WQ'

def print_soup(url, bs4_constructor_args):
    print("-------------")
    print('---- start ----')
    print('URL:', url)
    print('BeautifulSoup:' , bs4_constructor_args)

    soup = BeautifulSoup(requests.get(url).text, bs4_constructor_args)

    print("---- all ----")
    print(soup)

    print("---- title.string ----")
    print(soup.title.string)

    print('---- script ytInitialData ----')
    dict_str = ''
    for script in soup.find_all('script'):
        script_text = str(script)

        for line in script_text.splitlines():
            print(line)
            if 'ytInitialData' in line:
                dict_str = ''.join(script_text.split(" = ")[1:])


        # Capitalize booleans so JSON is valid Python dict.
        dict_str = dict_str.replace("false", "False")
        dict_str = dict_str.replace("true", "True")


        # Strip extra HTML from JSON.
        dict_str = re.sub(r'};.*\n.+<\/script>', '}', dict_str)

        print(dict_str)

        # Correct some characters.
        dict_str = dict_str.rstrip("  \n;")

        dics = ast.literal_eval(dict_str)

        print(dics)

    print("---- end ----")
    print("-------------")
    print()

print_soup(YOUTUBE_URL, "html.parser")
