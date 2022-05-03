import os
from celery import Celery
from kombu import Exchange, Queue

# setting the default settings module for CELERY
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'plattuit.settings')
app = Celery('plattuit')
# adding the CELERY_ prefix namespace
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.task_queues = [
    Queue(
        name='interaction.microblog.queue',
        exchange=Exchange('background.process.updater'),
        routing_key='interaction.microblog.service'
    ),
    Queue(
        name='tracking.microblog.queue',
        exchange=Exchange('background.process.tracker'),
        routing_key='tracking.microblog.service'
    ),
]

app.autodiscover_tasks()
