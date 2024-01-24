FROM apache/airflow:2.7.1
WORKDIR /home/sigmoid/TechDemo
COPY dags .
# RUN pip install python
