import json
import sys
import re
import Part2
from bs4 import BeautifulSoup
import os
import re

# apple_dat = BeautifulSoup(open("C:\\Users\Maurice\PycharmProjects\APT2017\Homework2\Part2\aapl.dat"))
# print(apple_dat)

apple_dat= open('aapl.dat')
apple_json = open('aapl.json')
f_dat = open('f.dat')
f_json = open('f.json')
xom_dat = open('xom.dat')
xom_json = open('xom.json')


apple_txt = apple_json.read()
f_txt = f_json.read()
xom_txt = xom_json.read()
apple_soup = BeautifulSoup(apple_txt, 'lxml')
f_soup = BeautifulSoup(f_txt, 'lxml')
xom_soup = BeautifulSoup(xom_txt, 'lxml')
# print(type(apple_soup))
# print(apple_soup.prettify()[0:100])
txt_only_apple = apple_soup.get_text()
txt_only_f = f_soup.get_text()
txt_only_xom = xom_soup.get_text()
# print(txt_only_apple)
# print(apple_soup.find_all(['optionQuotes']['Open']))
apple_obj = json.loads(apple_txt)
f_obj = json.loads(f_txt)
xom_obj = json.loads(xom_txt)
# print(obj)
# options_sorted = sorted(obj['optionQuotes'][0]['Open'])
# print((obj['currPrice']))
# print(obj['dateUrls'])
# print(obj['optionQuotes'][0])
# print(options_sorted)

# #load json from file
# lines = []
# while True:
#     line = apple_json.readline()
#     if not line: break
#     line = line.strip()
#     json_obj = json.loads(line)
#     lines.append(json_obj)
#
# #sort json
# lines = sorted(lines, key=lambda k: k['optionQuotes']['Open'], reverse=True)
#
# #output result
# for line in lines:
#     print(line)


def contractAsJson(filename):
  jsonQuoteData = "[]"
  if filename == 'aapl.dat':
    jsonQuoteData = apple_txt
    print(jsonQuoteData)
  elif filename == 'f.dat':
    jsonQuoteData = f_txt
  elif filename == 'xom.dat':
    jsonQuoteData = xom_txt
  else:
    jsonQuoteData = "Not a valid file"
  return jsonQuoteData

