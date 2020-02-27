import datetime as dt
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

def Writetofile():
    print('Writing in file')
    with open('D:\Local_Testing/airflow_tutorial/wishes.txt', 'a+', encoding='utf8') as f:
        now = dt.datetime.now()
        t = now.strftime("%Y-%m-%d %H:%M")
        f.write(str(t) + '\n')
    return 'Wished'


def respond():
    return 'Wishes Acknowledged'


default_args = {
    'owner': 'airflow',
    'start_date': dt.datetime(2020, 2, 26, 10, 00, 00),
    'concurrency': 1,
    'retries': 0
}

with DAG('my_simple_dag',
         catchup=False,
         default_args=default_args,
         schedule_interval='*/5 * * * *',
         # schedule_interval=None,
         ) as dag:
    opr_greet = BashOperator(task_id='Greet them',
                             bash_command='echo "Hello How are you!!"')

    opr_wishesback = PythonOperator(task_id='acknowledgement',
                               python_callable=greet)
    opr_sleep = BashOperator(task_id='sleep_me',
                             bash_command='sleep 5')

    opr_respond = PythonOperator(task_id='respond',
                                 python_callable=respond)

opr_hello >> opr_greet >> opr_sleep >> opr_respond
