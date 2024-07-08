from airflow.decorators import dag

from airflow.operators.bash import BashOperator
from pendulum import datetime

@dag(
    dag_id='s02_dags_task_direction',
    start_date=datetime(2024, 7, 7, tz="Asia/Seoul"),
    schedule="0 0 * * *",
    catchup=False,
)
def s02_dags_task_direction():
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


s02_dags_task_direction()
