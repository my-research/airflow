from __future__ import annotations

import pendulum
from airflow import DAG

with DAG(
    dag_id="dags_bash_operator",
    catchup=False,
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    schedule="@daily",
    tags=["produces", "dataset-scheduled"],
)