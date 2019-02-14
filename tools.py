# -*- coding: utf-8 -*-
import scrapy

class ToolsSpider(scrapy.Spider):
	name = 'tools'
	allowed_domains = ['toolstream.com']
	start_urls = ['http://toolstream.com/']
	
	def parse(self, response):
		brands = response.xpath('//*[@class="leftNavCategoriesNodeName"]')
		categories = response.xpath('//*[@class="leftNavCategoriesNodePopupColumn"]')
		for brand, category in zip(brands, categories):
			cat = category.xpath('.//a/@href').extract()
			br = brand.xpath('.//text()').extract_first()
			for c in cat:
				yield{'Brands': br, 'Categories_URL': response.urljoin(c)}
		
