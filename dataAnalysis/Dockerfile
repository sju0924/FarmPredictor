FROM python:3.9.9
WORKDIR /usr/src
RUN pip install flask
RUN pip install flask_restx
RUN pip install scikit-learn
RUN pip install numpy
RUN pip install pandas
RUN pip install joblib
RUN pip install lxml
RUN pip install bs4
RUN pip install -U flask-cors
RUN pip install requests
COPY . .

EXPOSE 5000