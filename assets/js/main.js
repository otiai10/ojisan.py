
$(function(){
  socket = new WebSocket("ws://%{host}:%{port}/chat");
  socket.onmessage = function(ev){
    data = JSON.parse(ev.data);
    console.log(data);
    $('#stream').prepend('<li>' + data.sender.nickname + ' (ﾟ⊿ﾟ) < ' +  data.content.message + '</li>');
  } 
  socket.onopen = function(ev){
    console.log('open event => ', ev);
    mess = JSON.stringify({'request':'/me/id','params':null});
    socket.send(mess);
  }

  // register click event
  $(".submit").on('click', function(){
      var mess = $("#message").val();
      if (mess) {
        data = JSON.stringify({'request':'/message/send','params':mess});
        socket.send(data);
        $("#message").val('').focus();
      } else {
        console.log('突然のNULL String');
      }
  });
});
