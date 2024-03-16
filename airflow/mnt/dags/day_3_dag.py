from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.utils import timezone

with DAG(
    "day_3_dag",
    schedule="0 18 3 * *",
    start_date=timezone.datetime(2024,1,20),
):
    #code here
    my_day_3_task = EmptyOperator(task_id="my_day_3_task")