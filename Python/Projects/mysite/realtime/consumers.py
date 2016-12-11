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
def ws_realtime_msg_con(msg):
	global counter,flag,textNow
	print("new connection...")
	realtext = msg.content['path'].strip("/")
	msg.channel_session['realtext'] = realtext
	#import pdb; pdb.set_trace()
	Group(realtext).add(msg.reply_channel)
	counter += 1
	#import pdb; pdb.set_trace()

	res1 = {"flag": flag, "num": counter, "text": textNow, "message": "you connected"}
	res1 = json.dumps(res1)
	res2 = {"flag": flag, "num": counter, "text": textNow, "message": "new one connected"}
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
	print("Total Connections: %d" % counter)

@channel_session
def ws_realtime_msg(msg):
	global flag,textNow

	print "received message: %s" % msg['text']

	if msg['text'] == 'start':
		flag = True
	elif msg['text'] == 'stop':
		flag = False
	else:
		print("recieved signal: %s" % msg['text'])
		pass
	while flag != False:

		#print(random.randint(1,9))
		textNow = str(random.randint(100,999))
		resp = {"flag": flag, "message": "realtime text", "text": textNow}
		resp = json.dumps(resp)
		Group(msg.channel_session['realtext']).send({
			"text": resp,
			})
		time.sleep(1)
		'''
		elif msg['text'] == 'stop':
			print("stop sending.")
			import pdb; pdb.set_trace()
			return
		'''
	else:
		print("[action]: realtext stoped.")
		resp = {"flag": flag, "message": "realtext stoped", "text": textNow}
		resp = json.dumps(resp)
		Group(msg.channel_session['realtext']).send({
			"text": resp
			})
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

	print("Total Connections: %d" % counter)




