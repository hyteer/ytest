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

@channel_session
def ws_realtime_msg_con(msg):
	global counter
	print "new connection..."
	realtext = msg.content['path'].strip("/")
	msg.channel_session['realtext'] = realtext
	#import pdb; pdb.set_trace()
	Group(realtext).add(msg.reply_channel)
	counter += 1
	#import pdb; pdb.set_trace()

	res1 = {"num": counter, "msg": "you connected"}
	res1 = json.dumps(res1)
	res2 = {"num": counter, "msg": "new one connected"}
	res2 = json.dumps(res2)
	

	if hasattr(msg, 'channel_session'):
		Group(msg.channel_session['realtext']).send({
			"text": res2,
		})
	else:
		msg.reply_channel.send({
			"text": res1,
			})
	#msg.reply_channel.send(res)

	'''
	data_dict = {"txt": str(random.randint(10,99)), "num": counter}
	
	data = json.dumps(data_dict)

	while True:
		#print(random.randint(1,9))
		
		Group("realtext").channel_session.send({
			"text": data,
			})
		"""
		msg.reply_channel.send({
			"text": data,
			})
		"""
		time.sleep(0.3)
	'''
	'''
	msg.reply_channel.send({
			"text": "you connected.",
			})
	'''
@channel_session
def ws_realtime_msg(msg):
	print "received message: %s" % msg['text']

	while msg['text'] == 'start':
		#print(random.randint(1,9))
		
		Group(msg.channel_session['realtext']).send({
			"text":str(random.randint(10,99)),
			})
		time.sleep(0.3)
		'''
		elif msg['text'] == 'stop':
			print("stop sending.")
			import pdb; pdb.set_trace()
			return
		'''
	else:
		print("invalid client signal: %s" % msg['text'])
	'''

	msg.reply_channel.send({
		"text":msg.content['text'],
		})
	'''

@channel_session
def ws_realtime_msg_disconnect(msg):
	global counter
	counter -= 1
	#import pdb; pdb.set_trace()

	res = {"num": counter, "msg": "some one disconnected"}
	res = json.dumps(res)
	Group(msg.channel_session['realtext']).send({"text":res})




