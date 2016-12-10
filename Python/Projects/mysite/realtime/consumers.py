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

@channel_session
def ws_realtime_msg_con(msg):
	print "Hi finally..."
	path = msg.content['path'].strip("/")
	#import pdb; pdb.set_trace()

	while True:
		#print(random.randint(1,9))
		
	
		msg.reply_channel.send({
			"text":str(random.randint(1,9)),
			})
		time.sleep(0.3)

def ws_realtime_msg(msg):
	msg.reply_channel.send({
		"text":msg.content['text'],
		})




