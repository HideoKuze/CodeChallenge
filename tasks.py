#simple tasks to inform user when Db has been updated instead of having to run requests
#test
from celery import task, Celery
from datetime import timedelta
import time
from datetime import date
import os
import sqlite3

celery = Celery('tasks', broker='amqp://guest@localhost//')

CELERYBEAT_SCHEDULE = {
    'add-every-10-sec': {
        'task': 'tasks.show',
        'schedule': timedelta(seconds=10),
        #'args': (16, 16)
    },
}


@task()
def show():
	today = str(date.today())
	conn = sqlite3.connect('db.sqlite3')
	c = conn.cursor()
	c.execute("SELECT * FROM convoapp_inputinfo WHERE created = '%s'" % today)
	result = c.fetchone()

	return result
