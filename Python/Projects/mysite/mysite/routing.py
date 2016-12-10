from channels.routing import route,include

from im.consumers import ws_connect,ws_message, ws_disconnect
from realtime.consumers import ws_realtime_msg_con, ws_realtime_msg

realtime_msg = [
	route("websocket.connect", ws_realtime_msg_con, path=r"^/real/$"),
	#route("websocket.connect", chat_connect, path=r"^/(?P<room>[a-zA-Z0-9_]+)/$"),
	route("websocket.receive", ws_realtime_msg),
]

channel_routing = [
    #route("http.request", "realtime.consumers.http_consumer"),
    route("websocket.connect", ws_connect, path=r"^/room/(?P<room>[a-zA-Z0-9_]+)/$"),
    #route("websocket.connect", ws_realtime_msg_con),
    route("websocket.receive", ws_message),
    route("websocket.disconnect", ws_disconnect),
    
]



routing = [
	#include(channel_routing, path=r"^chat"),
	include(channel_routing),
	include(realtime_msg),

]

