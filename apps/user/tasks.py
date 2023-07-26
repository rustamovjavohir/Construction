from celery import shared_task, Task, current_task
from celery.exceptions import CeleryError, RetryTaskError
import requests
from config.celery import app
from celery.schedules import crontab


class LoginTask(Task):
    # Custom Celery task class with retry options
    max_retries = 5
    default_retry_delay = 10  # Seconds

    def on_retry(self, exc, task_id, args, kwargs, einfo):
        # This method will be called when the task is retried
        current_task.update_state(state='RETRY', meta={'exc': str(exc)})

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        # This method will be called when the task fails
        current_task.update_state(state='FAILURE', meta={'exc': str(exc)})


@shared_task(base=LoginTask)
def webhook_send_message_2_url(username, password,
                               url="https://rustamovjavohir.jprq.live/api/auth/login/"):
    data = {
        "username": username,
        "password": password
    }
    response = requests.post(url, json=data)
    if response.status_code != 200:
        raise RetryTaskError("Error occurred while sending message")
    return response.json()


@shared_task
def hello_world():
    return "hello world"


@shared_task
def add(x, y):
    return x + y


# @shared_task
# def webhook_send_message_2_url(username, password,
#                                url="https://rustamovjavohir.jprq.live/api/auth/login/"):
#     data = {
#         "username": username,
#         "password": password
#     }
#     response = requests.post(url, json=data)
#     return response.json()


# app.conf.beat_schedule = {
#     'add-every-10-seconds': {
#         'task': 'apps.user.tasks.webhook_send_message_2_url',
#         'schedule': 10.0,
#         'args': ("Javohir", "Java200527")
#     },
# }
app.conf.timezone = 'UTC'

# webhook_send_message_2_url.s('Javohir', "Java200527").apply_async()
# when task is failed retry after 5 seconds
webhook_send_message_2_url.s('Javohir2', "Java200527").apply_async(retry=True, retry_policy={
    'max_retries': 5,
    'interval_start': 0,
    'interval_step': 0.2,
    'interval_max': 0.2,
})


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    sender.add_periodic_task(10.0, webhook_send_message_2_url.s('Javohir', "Java200527"), name='add every 10',
                             args=("Javohir", "Java200527"))

    # Calls test('hello') every 30 seconds.
    # It uses the same signature of previous task, an explicit name is
    # defined to avoid this task replacing the previous one defined.
    # sender.add_periodic_task(30.0, webhook_send_message_2_url.s('hello'), name='add every 30')

    # Calls test('world') every 30 seconds
    # sender.add_periodic_task(30.0, webhook_send_message_2_url.s('world'), expires=10)

    # Executes every Monday morning at 7:30 a.m.
    # sender.add_periodic_task(
    #     crontab(hour=7, minute=30, day_of_week=1),
    #     webhook_send_message_2_url.s('Javohir', "Java200527"),
    # )
