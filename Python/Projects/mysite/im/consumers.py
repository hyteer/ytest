# encoding: utf-8
from datetime import datetime
from django.utils import timezone
from django.http import HttpResponse
from channels.handler import AsgiHandler
from channels import Group
from channels.sessions import channel_session
import json

chatinfo = {}
# Connected to websocket.connect
@channel_session
def ws_connect(message):
	global chatinfo
	# Work out room name from path(ignore slashes)
	room = message.content['path'].strip("/")
	if not chatinfo.has_key(room):
		chatinfo[room] = {'num': 1,'person':[]}
	else:
		chatinfo[room]['num'] += 1
	print chatinfo[room]
	
	# Save room in session and add us to the group
	message.channel_session['room'] = room
	Group(room).add(message.reply_channel)
	#Group("chat-%s" %room).add(message.reply_channel)

# Connected to websocket.receive
@channel_session
def ws_message(msg):
	print msg['text'];
	#time = datetime.now()
	time = timezone.now()
	#import pdb; pdb.set_trace()
	data = json.loads(msg['text'])
	roomname = Group(msg.channel_session['room']).name
	username = data['name']
	print "room:%s,user:%s" % (roomname,username)
	
	if not username in chatinfo[roomname]['person']:
		chatinfo[roomname]['person'].append(username)
	print chatinfo[roomname]
	
	data['time'] = str(time)
	#import pdb; pdb.set_trace()
	data = json.dumps(data)

	#print data['name']
	#Group("chat-%s" % msg.channel_session['room']).send({
	Group(msg.channel_session['room']).send({
		"text": data,
		})
	


# Connected to websocket.disconnect
@channel_session
def ws_disconnect(msg):
	global chatinfo
	roomname = Group(msg.channel_session['room']).name
	#Group("chat-%s" % msg.channel_session['room']).discard(message.reply_channel)
	Group(msg.channel_session['room']).discard(msg.reply_channel)
	if not chatinfo.has_key(roomname):
		chatinfo[roomname] = {'num': 0}
	else:
		chatinfo[roomname]['num'] -= 1
	print chatinfo[roomname]


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


