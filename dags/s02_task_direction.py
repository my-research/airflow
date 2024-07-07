from airflow import DAG
from airflow.operators.bash import BashOperator
from pendulum import datetime

"""
기본적으로 dags 는 다음과 같이 정의할 수 있음
"""
with DAG(
    dag_id='s02_task_direction',
    schedule="0 0 * * *",
    start_date=datetime(2024, 7, 7, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    t1 = BashOperator(task_id='t1', bash_command='echo hello t1')
    t2 = BashOperator(task_id='t2', bash_command='echo hello t2')
    t3 = BashOperator(task_id='t3', bash_command='echo hello t3')
    t4 = BashOperator(task_id='t4', bash_command='echo hello t4')
    t5 = BashOperator(task_id='t5', bash_command='echo hello t5')
    t6 = BashOperator(task_id='t6', bash_command='echo hello t6')
    t7 = BashOperator(task_id='t7', bash_command='echo hello t7')
    t8 = BashOperator(task_id='t8', bash_command='echo hello t8')

t1 >> [t2, t3] >> t4
t5 >> t4
[t4 >> t7] >> t6 >> t8
