from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

# Define default_args dictionary to specify default parameters for the DAG
default_args = {
    'owner': 'geethanjali',
    'start_date': datetime(2024, 1, 1),
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Instantiate the DAG
dag = DAG(
    'tutorial_dag123',
    default_args=default_args,
    description='A simple example DAG',
    schedule_interval=timedelta(days=1),  # Run the DAG daily
)

# Define tasks in the DAG
start_task = DummyOperator(task_id='start_task', dag=dag)

def print_hello():
    print("Hello, this is a Python Operator task!")

python_task = PythonOperator(
    task_id='python_task',
    python_callable=print_hello,
    dag=dag,
)

end_task = DummyOperator(task_id='end_task', dag=dag)

# Set the task dependencies
start_task >> python_task >> end_task
