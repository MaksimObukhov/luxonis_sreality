# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import psycopg2


class LuxonisPipeline:
    def __init__(self):
        self.create_connection()

    def create_connection(self):
        self.connection = psycopg2.connect(
            host='localhost',
            port='5432',
            user='postgres',
            password='12345lux',
            dbname='luxonis_sreality'
        )

        self.cur = self.connection.cursor()

    def process_item(self, item, spider):
        self.cur.execute("""
        INSERT INTO public.flats_parsed (image_url, title)
        VALUES(%s, %s)""", (
            str(item["image_url"]),
            item["title"]
        ))

        self.connection.commit()
        return item

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()
