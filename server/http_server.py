from flask import Flask, render_template
import psycopg2
import time

app = Flask(__name__, template_folder='templates')


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


@app.route('/')
def display_ads():
    connection = create_conn()
    cur = connection.cursor()

    cur.execute("""
    SELECT title, image_url FROM flats_parsed
    """)
    data = cur.fetchall()

    cur.close()
    connection.close()

    return render_template('website_page.html', data=data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
