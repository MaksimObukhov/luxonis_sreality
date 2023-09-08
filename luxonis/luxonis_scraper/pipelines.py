# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter
import psycopg2


class LuxonisPipeline:
    def __init__(self):
        # self.create_connection()
        print("INIT 1")
        hostname = 'postgres'
        port = '5432'
        username = 'postgres'
        password = '12345lux'
        database = 'luxonis_sreality'

        self.connection = psycopg2.connect(
            host=hostname,
            user=username,
            password=password,
            dbname=database,
            port=port)
        print("INIT 2")
        self.cur = self.connection.cursor()
        print("INIT 3")
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS public.flats_parsed(
            id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
            image_url character varying COLLATE pg_catalog."default",
            title character varying COLLATE pg_catalog."default",
            CONSTRAINT flats_parsed_pkey PRIMARY KEY (id)
        )
        """)
        print("INIT 4")
        self.cur.execute("""
        DELETE FROM flats_parsed *
        """)
        print("INIT 5")

    # def create_connection(self):
    #     self.connection = psycopg2.connect(
    #         host='postgres',
    #         port='5432',
    #         user='postgres',
    #         password='12345lux',
    #         dbname='luxonis_sreality'
    #     )
    #
    #     self.cur = self.connection.cursor()
    #
    #     self.cur.execute("""
    #     CREATE TABLE IF NOT EXISTS flats_parsed(
    #         id serial PRIMARY KEY,
    #         title text,
    #         image_url text
    #     )
    #     """)
    #     print('TABLE flat created!')
    #     self.cur.execute("""
    #     DELETE FROM flat *
    #     """)

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
