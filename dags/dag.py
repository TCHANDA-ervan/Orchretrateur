from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
    

default_args = {
    'owner' : "team" ,
    'retries': 5,
    'retry_delay': timedelta(minutes=2)

}


dag = DAG(
    dag_id='PRODUIT',
    default_args=default_args,
    description='Produit nutritionnel',
    start_date=datetime(2024 , 1, 14,12) ,
    schedule_interval=timedelta(days=15)
)


#task_1_ingestion = BashOperator(
   # task_id='first_dag_1',
   # bash_command=" lancement ingestion",
   # dag=dag
#)


task_2_ingestion = BashOperator(
    task_id='second_dag',
    bash_command= """ /home/ubuntu/Desktop/project/injections/injection.sh""",
    dag=dag
)

task_job= BashOperator(
    task_id='first_dag_2',
    bash_command=" /home/ubuntu/Desktop/project/jobs/job1/scala && park-submit --class main.scala.mnmc.MnMcount target/scala-2.12/main-scala-mnmc_2.12-1.0.jar",
    dag=dag
)



task_2_ingestion >> task_job