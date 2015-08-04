# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy.http import Request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from freeproxylist.items import FreeproxylistItem
import time
#import lxml.html
from lxml.html import fromstring
from selenium.webdriver.common.action_chains import ActionChains
import urllib
import re

class ProxyspiderSpider(scrapy.Spider):
    name = "proxyspider"
    allowed_domains = ["freeproxylist.net"]
    
    start_urls = ("http://freeproxylists.net/?page={}".format(x) for x in xrange(24) )

    #'http://freeproxylists.net/',

    def parse(self, response):

    	hxs = Selector(response)
    	rows = hxs.xpath('//tr[@class="Odd" or @class="Even"]')
    	for row in rows:
    		ip_address = row.xpath('./td[1]//text()').extract()
    		port = row.xpath('./td[2]/text()').extract()
    		protocol = row.xpath('./td[3]/text()').extract()
    		city = row.xpath('./td[7]/text()').extract()
    		uptime = row.xpath('./td[8]/text()').extract()

    		item = FreeproxylistItem()
    		#print ip_address

    		if ip_address:
    			ip_address = ip_address[0]
    			link = urllib.unquote(ip_address)
    			print link
    			ip = re.search('\d*\.\d*\.\d*\.\d*',link)
    			if ip:
    				item["IPAddress"] = ip.group()
    		
    		if port:
    			item["Port"] = port
    		if protocol:
    			item["Protocol"] = protocol
    		if city:
    			item["City"] = city
    		if uptime:
    			item["Uptime"] = uptime

    		yield item
        
