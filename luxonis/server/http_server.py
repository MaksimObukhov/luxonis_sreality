from flask import Flask, render_template
import psycopg2

app = Flask(__name__, template_folder='server/templates')


@app.route('/')
def display_ads():
    connection = psycopg2.connect(
        host='localhost',
        port='5432',
        user='postgres',
        password='12345lux',
        dbname='luxonis_sreality'
    )
    cur = connection.cursor()

    cur.execute("""
    SELECT title, image_url FROM flats_parsed
    """)
    data = cur.fetchall()

    cur.close()
    connection.close()

    return render_template('website_page.html', data=data)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
