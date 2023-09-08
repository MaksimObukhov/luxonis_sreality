FROM python:latest
WORKDIR /server
COPY . /server

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip3 install --upgrade pip
RUN pip3 install --disable-pip-version-check --no-cache-dir -r requirements.txt

EXPOSE 8080
ENV NAME World
CMD ["python", "http_server.py"]

