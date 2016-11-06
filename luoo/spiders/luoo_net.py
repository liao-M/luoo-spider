# -*- coding: utf-8 -*-
import scrapy
from luoo.items import LuooItem
class LuooSpider(scrapy.Spider):
	name = "luoo"
	allowed_domains = ["luoo.net"]
	start_urls = ["http://www.luoo.net/music/"]


	def parse(self, response):
		for url in response.xpath("//a[@class='page']/@href").extract():
			yield scrapy.Request(url, self.parse)
		
		item = LuooItem()
		item['image_urls'] = response.xpath("//img[@class='cover rounded']/@src").extract()
		yield item