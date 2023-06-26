from celery import shared_task
import requests
from config.celery import app
from celery.schedules import crontab


@shared_task
def hello_world():
    return "hello world"


@shared_task
def add(x, y):
    return x + y


@shared_task
def webhook_send_message_2_url(message="Hello", url="https://rustamovjavohir.jprq.live/api/auth/login/"):
    data = {
        "username": "Javohir",
        "password": "Java200527"
    }

    response = requests.post(url, json=data)
    return response.json()


app.conf.beat_schedule = {
    'add-every-10-seconds': {
        'task': 'apps.user.tasks.webhook_send_message_2_url',
        'schedule': 10.0,
        'args': ("hello", )
    },
}
app.conf.timezone = 'UTC'


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    sender.add_periodic_task(10.0, webhook_send_message_2_url.s('hello'), name='add every 10')

    # Calls test('hello') every 30 seconds.
    # It uses the same signature of previous task, an explicit name is
    # defined to avoid this task replacing the previous one defined.
    sender.add_periodic_task(30.0, webhook_send_message_2_url.s('hello'), name='add every 30')

    # Calls test('world') every 30 seconds
    sender.add_periodic_task(30.0, webhook_send_message_2_url.s('world'), expires=10)

    # Executes every Monday morning at 7:30 a.m.
    sender.add_periodic_task(
        crontab(hour=7, minute=30, day_of_week=1),
        webhook_send_message_2_url.s('Happy Mondays!'),
    )
