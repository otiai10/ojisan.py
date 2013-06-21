
$(function(){
  socket = new WebSocket("ws://otiai10.com:9090/chat");
  socket.onmessage = function(mess){
    console.log(mess);
  };
  for (var i in socket) {
    console.log(i, socket[i]);
  }
});
