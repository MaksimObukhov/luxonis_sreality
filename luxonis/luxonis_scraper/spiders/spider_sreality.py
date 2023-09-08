import scrapy
from scrapy.spiders import Spider
from scrapy import Request
from sys import path


class FlatItem(scrapy.Item):
    title = scrapy.Field()
    image_url = scrapy.Field()


class CrawlingSpider(Spider):
    name = 'sreality_spider'

    start_urls = [
        'https://www.sreality.cz/api/cs/v2/estates?category_main_cb=1&category_type_cb=1&sort=0&per_page=' + str(
            100) + '&page=' + str(x) + '' for x in range(1, 6)
    ]

    def parse(self, response):
        json_response = response.json()
        for item in json_response["_embedded"]['estates']:
            yield Request('https://www.sreality.cz/api' + item['_links']['self']['href'],
                          callback=self.parse_flat)

    def parse_flat(self, response):
        json_response = response.json()
        flat = FlatItem()
        flat['title'] = json_response['name']['value']

        for images in json_response['_embedded']['images']:
            if images['_links']['dynamicDown']:
                tmp = images['_links']['dynamicDown']['href'].replace('{width}', '400')
                tmp = tmp.replace('{height}', '300')
                flat['image_url'] = tmp
                break

        yield flat
