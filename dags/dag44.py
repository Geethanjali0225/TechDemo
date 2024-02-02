from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {
    'owner': 'airflow',
    'start_date': datetime.utcnow(),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'dag44',
    default_args=default_args,
    description='A simple example DAG',
    schedule_interval='@daily',
)

task1 = BashOperator(
    task_id='task_1',
    bash_command='echo "Hello"',
    dag=dag,
)

task2 = BashOperator(
    task_id='task_2',
    bash_command='echo "World"',
    dag=dag,
)

task1 >> task2
