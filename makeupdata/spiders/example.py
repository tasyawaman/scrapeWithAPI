import scrapy
import json
from makeupdata.items import MakeupdataItem


class MakeupSpider(scrapy.Spider):
    name = 'makeup'
    # allowed_domains = ['example.com']
    # start_urls = ['http://example.com/']

    def start_requests(self):
    	url = 'http://makeup-api.herokuapp.com/api/v1/products.json?'

    	yield scrapy.http.Request(url)

    def parse(self, response):
    	jsonresponse = json.loads(response.text)
    	item = MakeupdataItem()
    	first_only = jsonresponse[1]
    	item['id'] = { 'value' : first_only['id']}
    	item['name'] = {'value' : first_only['name'] }
    	item['brand'] = {'value' : first_only['brand']}
    	item['price'] = { 'value' : first_only['price']}
    	item['description'] = {'value' : first_only['description']}
    	yield item





