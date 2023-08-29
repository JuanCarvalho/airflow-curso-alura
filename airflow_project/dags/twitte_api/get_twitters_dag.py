from airflow.models import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python import PythonOperator

from airflow_project.common_lib.path_lib import data_to_file
from airflow_project.operators.twitter_operator import TwitterOperator


with DAG(
    dag_id='get_twitters_dag',
    start_date=days_ago(1),
    schedule_interval='@daily',
) as dag:

    twitter_get_dag = TwitterOperator(
        task_id='twitter_get',
    )

    data_to_file_dag = PythonOperator(
        task_id='data_to_file',
        python_callable=data_to_file,
        op_args=['{{ ti.xcom_pull(task_ids="twitter_get") }}', 'username', 'twitter'],
    )

    twitter_get_dag >> data_to_file_dag
