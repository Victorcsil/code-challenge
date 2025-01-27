from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG("my_dag", start_date=datetime(2021,1,1), catchup=False, schedule_interval='@daily') as dag:
    task1 = BashOperator(
        task_id="task1",
        bash_command="cd /home/victor/Desktop/TESTE/code-challenge; .meltano/run/bin run tap-csv--order-details target-csv"
    )

    task2 = BashOperator(
        task_id="task2",
        bash_command="cd /home/victor/Desktop/TESTE/code-challenge; .meltano/run/bin run tap-postgres target-csv"
    )
    task1 >> task2