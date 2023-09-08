FROM python:latest
WORKDIR ./luxonis_scraper
COPY luxonis_scraper/requirements.txt .


RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip3 install --upgrade pip
RUN pip3 install --disable-pip-version-check --no-cache-dir -r requirements.txt

RUN pip install scrapy
RUN pip install Twisted==22.10.0

WORKDIR ../
COPY luxonis_scraper ./luxonis_scraper
COPY scrapy.cfg .

CMD ["scrapy", "crawl", "sreality_spider"]
