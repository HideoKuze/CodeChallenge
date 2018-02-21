from __future__ import unicode_literals
from django.contrib import admin
from models import InputInfo
#from kombu.transport.django import models as kombu_models

admin.site.register(InputInfo)
#admin.site.register(kombu_models.Message)