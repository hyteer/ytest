from channels.routing import route,include

from im.consumers import ws_connect,ws_message, ws_disconnect
from realtime.consumers import ws_realtime_msg_con, ws_realtime_msg,ws_realtime_msg_disconnect

realtime_msg = [
	route("websocket.connect", ws_realtime_msg_con, path=r"^/real/$"),
	#route("websocket.connect", chat_connect, path=r"^/(?P<room>[a-zA-Z0-9_]+)/$"),
	route("websocket.receive", ws_realtime_msg, path=r"^/real/$"),
	route("websocket.disconnect", ws_realtime_msg_disconnect, path=r"^/real/$"),

]

channel_routing = [
    #route("http.request", "realtime.consumers.http_consumer"),
    route("websocket.connect", ws_connect, path=r"^/room/(?P<room>[a-zA-Z0-9_]+)/$"),
    #route("websocket.connect", ws_realtime_msg_con),
    route("websocket.receive", ws_message, path=r"^/room/(?P<room>[a-zA-Z0-9_]+)/$"),
    route("websocket.disconnect", ws_disconnect, path=r"^/room/(?P<room>[a-zA-Z0-9_]+)/$"),
    
]



routing = [
	#include(channel_routing, path=r"^chat"),
	include(channel_routing),
	include(realtime_msg),

]

