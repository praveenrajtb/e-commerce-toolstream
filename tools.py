# -*- coding: utf-8 -*-
import scrapy

class ToolsSpider(scrapy.Spider):
	name = 'tools'
	allowed_domains = ['toolstream.com']
	start_urls = ['http://toolstream.com/']
	
	def parse(self, response):
# Brands are list of brands and categories are the categories associated with each brands		
		brands = response.xpath('//*[@class="leftNavCategoriesNodeName"]')
		categories = response.xpath('//*[@class="leftNavCategoriesNodePopupColumn"]')
# Select each brand and the category list associted with that brand
		for brand, category in zip(brands, categories):
			cat = category.xpath('.//a/@href').extract()
			br = brand.xpath('.//text()').extract_first()
# Select all the categories associated with each brand and yield			
			for c in cat:
				yield{'Brands': br, 'Categories_URL': response.urljoin(c)}
		
