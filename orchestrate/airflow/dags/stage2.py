from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG("load", start_date=datetime(2021,1,1), catchup=False, schedule_interval='@daily') as dag:
    task1 = BashOperator(
        task_id="task1",
        bash_command="cd /home/victor/Desktop/TESTE/code-challenge; .meltano/run/bin run tap-csv target-postgres"
    )