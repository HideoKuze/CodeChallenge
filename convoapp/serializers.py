from convoapp import models 
from rest_framework import serializers
from models import SenderInfo, Messages

#will turn the message instance into a JSON object
class senderSerializer(serializers.ModelSerializer):

	class Meta:
		model = SenderInfo
		fields = ['sender']


'''class messageSerializer(serializers.ModelSerializer):

	class Meta:
		model = Messages 
		fields = ['message_sender', 'message_body']'''