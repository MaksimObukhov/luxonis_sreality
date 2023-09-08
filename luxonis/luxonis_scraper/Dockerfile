FROM python:latest
WORKDIR /luxonis/luxonis_scraper
COPY requirements.txt ./
#WORKDIR /app
#COPY . /app

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip3 install --upgrade pip
RUN pip3 install --disable-pip-version-check --no-cache-dir -r requirements.txt

RUN pip install scrapy

COPY . .
CMD ["scrapy", "crawl", "sreality_spider"]
