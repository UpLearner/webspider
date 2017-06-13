#!usr/bin/env python3
# -*- coding: utf-8 -*-

# 在笔趣味阁下载指定小说

from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import re, time

req_header = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

def this_page(url):
	req = Request(url, headers=req_header)
	html = urlopen(req)

	bsObj = BeautifulSoup(html,'html.parser')

	title = bsObj.h1

	contents = bsObj.find('div',{'id':'content'})
	text = contents.get_text().split('    ')

	with open('content.txt','a') as f:
		f.write(title.get_text()+'\n')
		for line in text:
			f.write(line+'\n')

def next_page(url):
	req = Request(url, headers=req_header)
	html = urlopen(req)
	bsObj = BeautifulSoup(html,'html.parser')
	for link in bsObj.findAll('a',href=re.compile('\d{7}.html')):
		if 'href' in link.attrs:
			if link.get_text() == '下一章>>':
				return(main_url+link.attrs['href'])

start_page = input("Pls enter the start_page: ")
# main_url = 'http://www.bqg5200.com/xiaoshuo/3/3866/' #重生完美时代
# main_url = 'http://www.bqg5200.com/xiaoshuo/4/4599/' # 放开那个女巫
main_url = 'http://www.bqg5200.com/xiaoshuo/3/3194/'  #五行天
url = main_url+str(start_page)+'.html'

down_page = input("Pls enter the page number you want download: ")
down_page = int(down_page)

count = 0
i = 0
while i < down_page:
	this_page(url)
	count = count + 1
	print(count,"page down!")
	url = next_page(url)
	i = i + 1
	time.sleep(5)
print('collect finish!')





