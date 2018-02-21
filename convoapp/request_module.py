#will make requests here
#note: NEVER name the file the same name as the library...
import os
import requests


post_data = {'name': 'smith', 'conversation_id': '1', 'message_body': 'Ada Challenge'}
post_request = requests.session()
post_request.get('http://127.0.0.1:8000/message/')
csrftoken = post_request.cookies['csrftoken']

req = post_request.post('http://127.0.0.1:8000/message/', data={'csrfmiddlewaretoken' : csrftoken}, cookies=post_request.cookies)

print req.status_code