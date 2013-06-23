
$(function(){
  socket = new WebSocket("ws://%{host}:%{port}/chat");
  socket.onmessage = function(ev){
    data = JSON.parse(ev.data);
    console.log(data);
    $('#stream').prepend('<li>' + data.nickname + ' (ﾟ⊿ﾟ) < ' +  data.echo + '</li>');
  } 
  socket.onopen = function(ev){
    console.log('open event => ', ev);
    mess = JSON.stringify({'request':'/member/id','params':null});
    socket.send(mess);
  }

  // register click event
  $(".submit").on('click', function(){
      var mess = $("#message").val();
      if (mess) {
        socket.send(mess);
        $("#message").val('').focus();
      } else {
        console.log('突然のNULL String');
      }
  });
});
