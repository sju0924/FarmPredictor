FROM python:3.9.9
WORKDIR /usr/src
RUN pip install flask
RUN pip install flask_restx
RUN pip install scikit-learn
RUN pip install numpy
RUN pip install pandas
RUN pip install -U flask-cors
COPY tree_reg.pkl .
COPY app.py .

EXPOSE 5000