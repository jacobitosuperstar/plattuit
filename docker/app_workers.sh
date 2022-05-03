#!/bin/sh

# python3 /appuser/rabbitmq/rabbitmq_init.py >> /appuser/logs/rabbitmq.log
celery -A plattuit worker -l INFO
