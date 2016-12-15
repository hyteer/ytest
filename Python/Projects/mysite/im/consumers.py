# encoding: utf-8
from datetime import datetime
from django.utils import timezone
from django.http import HttpResponse
from channels.handler import AsgiHandler
from channels import Group
from channels.sessions import channel_session
import json
import collections 

chatinfo = {}

# Connected to websocket.connect
@channel_session
def ws_connect(msg, room):
	global chatinfo
	data = collections.OrderedDict() 
	print "room %s connect..." % room
	time = timezone.now()
	# Work out room name from path(ignore slashes)
	#import pdb; pdb.set_trace()
	#room = msg.content['path'].strip("/")
	room = room
	if not chatinfo.has_key(room):
		chatinfo[room] = {'num': 1,'person':[]}
	else:
		chatinfo[room]['num'] += 1
	print chatinfo[room]
	
	# Save room in session and add us to the group
	msg.channel_session['room'] = room
	Group(room).add(msg.reply_channel)
	data['type'] = 1
	data['info'] = chatinfo[room]
	data['time'] = str(time)
	#data = {'type':1,'msg':chatinfo[room],'time':str(time)}			# type1:system message, type2:chat message
	data = json.dumps(data)
	Group(msg.channel_session['room']).send({
		"text": data ,
		})
	#Group("chat-%s" %room).add(msg.reply_channel)

# Connected to websocket.receive
@channel_session
def ws_message(msg, room):
	data = collections.OrderedDict()
	print msg['text'];
	#time = datetime.now()
	time = timezone.now()
	#import pdb; pdb.set_trace()

	msg_text = json.loads(msg['text'])
	roomname = Group(msg.channel_session['room']).name
	username = msg_text['name']
	print "room:%s,user:%s" % (roomname,username)
	
	if not username in chatinfo[roomname]['person']:
		chatinfo[roomname]['person'].append(username)
	print chatinfo[roomname]

	data['type'] = 2
	data['info'] = msg_text
	data['time'] = str(time)
	#data = {'type':2,'msg':msg_text,'time':str(time)}		# type1:system message, type2:chat message

	#import pdb; pdb.set_trace()
	data = json.dumps(data)

	#print data['name']
	#Group("chat-%s" % msg.channel_session['room']).send({
	Group(msg.channel_session['room']).send({
		"text": data,
		})
	


# Connected to websocket.disconnect
@channel_session
def ws_disconnect(msg, room):
	global chatinfo
	data = collections.OrderedDict()
	time = timezone.now()
	#import pdb; pdb.set_trace()
	#data = json.loads(msg['text'])
	#username = data['name']
	roomname = Group(msg.channel_session['room']).name
	#Group("chat-%s" % msg.channel_session['room']).discard(message.reply_channel)
	Group(msg.channel_session['room']).discard(msg.reply_channel)
	'''
	if not chatinfo.has_key(roomname):
		chatinfo[roomname] = {'num': 0}
	else:
		chatinfo[roomname]['person'].remove(username)
		chatinfo[roomname]['num'] -= 1
	'''
	chatinfo[roomname]['num'] -= 1
	print chatinfo[roomname]
	data['type'] = 1
	data['info'] = chatinfo[roomname]
	data['time'] = str(time)
	data = json.dumps(data)
	Group(msg.channel_session['room']).send({
		"text": data,
		})


"""
def http_consumer(message):
	response = HttpResponse("hello world! you asked for %s" % message.content['path'])
	for chunk in AsgiHandler.encode_response(response):
		message.reply_channel.send(chunk)
		
def ws_message(message):
    # ASGI WebSocket packet-received and send-packet message types
    # both have a "text" key for their textual data.
    message.reply_channel.send({
        "text": message.content['text'],
    })

# Connected to websocket.content
def ws_add(message):
	Group("chat").add(message.reply_channel)

def ws_message(message):
	Group("chat").send({
		"text": "[user] %s" % message.content['text'],
		})

# Connected to websocket.disconnect
def ws_disconnect(message):
	Group("chat").discard(message.reply_channel)
"""


