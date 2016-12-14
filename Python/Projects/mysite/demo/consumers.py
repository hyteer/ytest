# encoding: utf-8
from datetime import datetime
import time, random
from django.utils import timezone
from django.http import HttpResponse
from channels.handler import AsgiHandler
from channels import Group
from channels.sessions import channel_session
import json

flag = False
counter = 0
textNow = ""

@channel_session
def ws_chart_con(msg):

	print("new connection...")
	res = {"data": "chartdata", "msg": "some one connected"}
	res = json.dumps(res)
	Group(msg.channel_session['chart']).send({"text":res})

	print("Total Connections: %d" % counter)

@channel_session
def ws_chart_msg(msg):

	print("received message: %s" % msg['text'])

	res = {"data": "chartdata", "msg": "recieved you message."}
	res = json.dumps(res)
	Group(msg.channel_session['chart']).send({"text":res})

@channel_session
def ws_chart_disconnect(msg):

	#import pdb; pdb.set_trace()
	res = {"data": "chartdata", "msg": "some one disconnected"}
	res = json.dumps(res)
	Group(msg.channel_session['chart']).send({"text":res})

	print("some one disconnected")




