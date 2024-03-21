from celery import Celery

app = Celery('tasks', broker='redis://localhost//')

app.conf.broker_connection_retry_on_startup = True
app.conf.broker_connection_retry = True
app.conf.update(
    broker_transport_options={
        'max_retries': 3,
        'interval_start': 0,
        'interval_step': 0.2,
        'interval_max': 0.5,
    }
)
app.conf.result_backend = 'redis://localhost:6379/0'
