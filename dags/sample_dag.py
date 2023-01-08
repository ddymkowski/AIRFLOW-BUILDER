from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator

with DAG(
    dag_id="first_sample_dag", start_date=datetime(2022, 5, 28), schedule_interval=None
) as dag:

    first_task = BashOperator(task_id="print_hello_world", bash_command=f'echo "!"')


first_task
