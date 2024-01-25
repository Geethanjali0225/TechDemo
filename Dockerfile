FROM apache/airflow:2.7.1
WORKDIR /opt/airflow
COPY /dags/ $AIRFLOW_HOME/dags/