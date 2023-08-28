from airflow.models import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python import PythonOperator
from airflow_project.common_lib.service import APIService
from airflow_project.common_lib.path_lib import data_to_file


api_service = APIService()


with DAG(
    dag_id='get_wather_api_dag',
    start_date=days_ago(1),
    schedule_interval='@daily',
) as dag:

    api_get_dag = PythonOperator(
        task_id='api_get',
        python_callable=api_service.whater,
        op_args=['São Paulo', 15],
    )

    data_to_file_dag = PythonOperator(
        task_id='data_to_file',
        python_callable=data_to_file,
        op_args=['{{ ti.xcom_pull(task_ids="api_get") }}', 'sao_paulo'],
    )

    api_get_dag >> data_to_file_dag
