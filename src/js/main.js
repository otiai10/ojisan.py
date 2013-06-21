
$(function(){
  socket = new WebSocket("ws://otiai10.com:9090/chat");
  socket.onmessage = function(ev){
    //console.log('On Message Event =>', ev);
    $('#stream').prepend('<li>' + ev.data + '</li>');
  } 
  socket.onopen = function(ev){
    //console.log('On Open Event =>', ev);
    socket.send('Hi, this is Client!!');
  }

  // register click event
  $("#submit").on('click', function(){
      var mess = $("#message").val();
      if (mess) {
        socket.send(mess);
        $("#message").val('');
      } else {
        console.log('突然のNULL String');
      }
  });
});
