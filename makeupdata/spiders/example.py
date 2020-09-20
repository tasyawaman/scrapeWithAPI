import scrapy
import json
from makeupdata.items import MakeupdataItem


class MakeupSpider(scrapy.Spider):
    name = 'makeup'
    # allowed_domains = ['example.com']
    # start_urls = ['http://example.com/']

    def start_requests(self):
    	url = 'http://makeup-api.herokuapp.com/api/v1/products.json?brand=maybelline'

    	yield scrapy.http.Request(url)

    def parse(self, response):
    	jsonresponse = json.loads(response.text)
    	item = MakeupdataItem()

    	for index in jsonresponse:
    		item['id'] = {'value' : index['id']}
    		item['name'] = {'value' : index['name']}
    		item['brand'] = {'value' : index['brand']}
    		item['price'] = {'value' : index['price']}
    		item['description'] = {'value' : index['description']}
    		yield item







