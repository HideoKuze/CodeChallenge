# CodeChallenge
Ada Support Code Challenge

I originally thought we need to create some UI for input, but we didn't so I tried to scale back Django a bit lol

Clone repo 
run pip install -r requirements.txt

***Optional - Run asyncronous task queue***
Follow steps to download message broker and Erlang (http://www.rabbitmq.com/download.html), you can also use another broker like Redis. 

Run `celery -A tasks worker --loglevel=info` to start the worker process
Open a second terminal and run the python shell (`python manage.py shell`)
Then `from convoapp import tasks` then `from tasks import show` 
then `show.delay()` Note: Make sure to run `post_requests` once populate the `SQLite` database 

Thank you for considering me for this challenge =)
