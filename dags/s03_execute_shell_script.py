from airflow.decorators import dag
from airflow.operators.bash import BashOperator
from pendulum import datetime


@dag(
    dag_id='s03_execute_shell_script',
    start_date=datetime(2024, 7, 7, tz="Asia/Seoul"),
    schedule=None,
    catchup=False,
)
def s03_execute_shell_script():
    t1 = BashOperator(
        task_id='t1',
        bash_command="$AIRFLOW_HOME/include/sample-bash.sh "
    )


s03_execute_shell_script()
