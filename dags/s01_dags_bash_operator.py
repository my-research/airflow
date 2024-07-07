from airflow import DAG
from airflow.operators.bash import BashOperator
from pendulum import datetime

"""
기본적으로 dags 는 다음과 같이 정의할 수 있음
"""
with DAG(
    dag_id='s01_dags_bash_operator',
    schedule="0 0 * * *",
    start_date=datetime(2019, 12, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    bash_t1 = BashOperator(
        task_id='bash_t1',
        bash_command='echo hello jang'
    )
    bash_t2 = BashOperator(
        task_id='bash_t2',
        bash_command='echo $HOSTNAME'
    )

bash_t1 >> bash_t2
