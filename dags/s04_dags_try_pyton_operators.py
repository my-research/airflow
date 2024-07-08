from airflow.decorators import dag
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
from pendulum import datetime

from plugins.common import greeting

"""
PythonOperator
"""
@dag(
    dag_id='s04_dags_try_pyton_operators',
    start_date=datetime(2024, 7, 7, tz="Asia/Seoul"),
    schedule=None,
    catchup=False,
)
def s04_dags_try_pyton_operators():
    start = EmptyOperator(task_id='start')

    greeting_task = PythonOperator(
        task_id='greeting_task',
        python_callable=greeting.greet,
        op_args=['jangwonik']
    )

    end = EmptyOperator(task_id='end')

    start >> greeting_task >> end


s04_dags_try_pyton_operators()
