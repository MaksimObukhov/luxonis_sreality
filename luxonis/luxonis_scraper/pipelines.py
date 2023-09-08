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
            host='postgres',
            port='5432',
            user='postgres',
            password='12345lux',
            dbname='luxonis_sreality'
        )

        self.cur = self.connection.cursor()

        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS flats_parsed(
            id serial PRIMARY KEY,
            title text,
            image_url text
        )
        """)
        print('TABLE flat created!')
        self.cur.execute("""
        DELETE FROM flat *
        """)


    def process_item(self, item, spider):
        self.cur.execute("""
        INSERT INTO flats_parsed (image_url, title)
        VALUES(%s, %s)""", (
            str(item["image_url"]),
            item["title"]
        ))

        self.connection.commit()
        return item

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()
