from airflow.decorators import dag
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator, BranchPythonOperator
from plugins.common import greeting
from pendulum import datetime


@dag(
    dag_id='s04_operators',
    start_date=datetime(2024, 7, 7, tz="Asia/Seoul"),
    schedule=None,
    catchup=False,
)
def s04_operators():
    greeting_task = PythonOperator(
        task_id='greeting_task',
        python_callable=greeting.greet,
        op_args=['jangwonik']
    )


s04_operators()
