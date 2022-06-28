FROM python:3.9.9
WORKDIR /usr/src
RUN pip install django
RUN pip install requests
RUN pip install python-dotenv
RUN pip3 install djangorestframework
RUN pip3 install account
RUN pip3 install beautifulsoup4
COPY . .

EXPOSE 8000