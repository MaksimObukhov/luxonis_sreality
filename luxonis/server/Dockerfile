FROM tiangolo/uwsgi-nginx-flask:python3.8
WORKDIR /luxonis/server
COPY . /luxonis/server

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip3 install --upgrade pip
RUN pip3 install --disable-pip-version-check --no-cache-dir -r requirements.txt

EXPOSE 80
ENV NAME World
CMD ["python", "http_server.py"]

