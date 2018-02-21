#take input and convert to json
#from models import InputInfo

import json 

'''{
    "id": "1234",
    "messages": [
        {
            "sender": "anson",
            "message": "I'm a teapot",
            "created": "2018-01-17T04:50:14.883Z"
        },
        {
            "sender": "david",
            "message": "Short and stout",
            "created": "2018-01-17T04:52:17.201Z"
        }
    ]
}'''

#input from user
#which are sender and message, ids will be produced automatically
messages = {'messages': []}
objects = ['shara', 'brandon', 'felisha']
message_body = {"test1", "test2", "test3"}
#entry = {}
 #object attribute will be here
#for i in objects entry['sender'] = i.name, entry['message']= i.message


for i in objects:
	entry = {}
	entry2= {}
	entry['sender'] = i 
	#entry2['message'] = 
	#entry2['message'] = 
	messages.get('messages').append(entry)

output = json.dumps(messages)
print output
