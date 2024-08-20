from datetime import datetime
from datetime import timedelta
from airflow.models.dag import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from pokemon_etl import getAllPokeData

default_args = {
    'owner':'airflow',
    'depends_on_past':False,
    'start_date': datetime(2024,8,19),
    'email': '',
    'email_on_failure': False,
    'email_on_success': False,
    'retries': 1,
    'retry_delay':timedelta(minutes=1)
}

dag = DAG(
    'pokemon_dag',
    default_args=default_args,
    description='pokemon etl aws'
)

run_etl = PythonOperator(
    task_id="complete_pokemon_etl",
    python_callable = getAllPokeData,
    dag=dag
)

run_etl