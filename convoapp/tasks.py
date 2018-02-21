#simple tasks to inform user when Db has been updated instead of having to run requests

from celery import task, Celery
import django

broker_url = 'amqp://myuser:mypassword@localhost:5672/myvhost'
celery = Celery('tasks', broker=broker_url)

@task()
def add(x, y):
	return x + y
