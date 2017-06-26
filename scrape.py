#!/usr/bin/env python3

import sys
def enc(msg):
	return msg.encode(sys.stdout.encoding, errors='replace')

import scrapy
from scrapy.selector import Selector

class MagicSpider(scrapy.Spider):
	name = 'magicspider'

	# RED 	= R
	# GREEN = G
	# BLACK = B
	# WHITE = W
	# BLUE	= U


	# http://gatherer.wizards.com/Pages/Search/Default.aspx?page=<number>&color=%7C%5B<color code>%5D
	def start_requests(self):
		COLORS = ['R', 'G', 'B', 'W', 'U']
		for col in COLORS:
			for i in range(34):
				url = 'http://gatherer.wizards.com/Pages/Search/Default.aspx?page=' + str(i) + '&color=%7C%5B' + col + '%5D'
				yield scrapy.Request(url=url, meta={'color':col, 'page_num':i})

	# http://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=<>&type=card\
	def parse(self, response):
		filter_str = '<img src="../../Handlers/Image.ashx?multiverseid='
		site = response.selector.xpath('//table').css('img')
		filename = response.meta['color'] + str(response.meta['page_num']) + '.csv'
		with open(filename, 'w') as f:
			for item in site.extract():
				if item[0:len(filter_str)] == filter_str:
					result = item.partition('&amp;type=card')[0]
					f.write("%s," % result[len(filter_str):len(result)])
			self.log('Saved file %s' % filename)
