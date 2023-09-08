import psycopg2
import time


class LuxonisPipeline:
    def __init__(self):
        hostname = 'postgres'
        port = '5432'
        username = 'postgres'
        password = '12345lux'
        database = 'luxonis_sreality'
        def create_conn():
            conn = None
            while not conn:
                try:
                    conn = psycopg2.connect(
                        host='postgres',
                        port='5432',
                        user='postgres',
                        password='12345lux',
                        dbname='luxonis_sreality'
                    )
                    print("Database connection successful")
                except psycopg2.OperationalError as e:
                    print(e)
                    time.sleep(5)
            return conn
        self.connection = create_conn()
        # self.connection = psycopg2.connect(
        #     host=hostname,
        #     user=username,
        #     password=password,
        #     dbname=database,
        #     port=port)

        self.cur = self.connection.cursor()

        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS public.flats_parsed(
            id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
            image_url character varying COLLATE pg_catalog."default",
            title character varying COLLATE pg_catalog."default",
            CONSTRAINT flats_parsed_pkey PRIMARY KEY (id)
        )
        """)

        self.cur.execute("""
        DELETE FROM flats_parsed *
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
