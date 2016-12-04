// Note that the path doesn't matter right now; any WebSocket
// connection gets bumped over to WebSocket consumers

room_label = document.getElementsByTagName('h2')[0].innerText;


socket = new WebSocket("ws://" + window.location.host + "/"+room_label+"/");
socket.onmessage = function(msg) {
	//data = e.data;
    console.log("data:"+msg.data);
    var data = JSON.parse(msg.data);
    
    var chat = $("#chat")
    var ele = $('<tr></tr>');

    console.log("[Name]:"+data.name+" [Message]:"+data.message);
    ele.append($("<td></td>").text(data.name));
    ele.append($("<td></td>").text(data.message));
    ele.append($("<td></td>").text(data.time));
    //alert(ele);
    chat.append(ele);
};
/*
socket.onopen = function() {
    
	msg = "[notice] a new anonymous has been joined this room.";
    socket.send(msg);
}
*/
$("#chatform").on("submit", function(event) {
    var sender = document.getElementById("sender");
    if (sender.value == ""){
        var name = "anonymous";
    }
    else{
        var name = sender.value;
    }
    data = {
        name: name,
        message: $('#message').val(),
    }

    var data = JSON.stringify(data);
    //alert(data)
    socket.send(data);
    $("#message").val('').focus();
    return false;
});