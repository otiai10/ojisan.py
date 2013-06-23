
$(function(){
  //socket = new WebSocket("ws://%{host}:9090/chat");
  socket = new WebSocket("ws://www15224uf.sakura.ne.jp:9090/chat");
  socket.onmessage = function(ev){
    data = JSON.parse(ev.data);
    console.log(data);
    $('#stream').prepend('<li>' + data.nickname + ' (ﾟ⊿ﾟ) < ' +  data.echo + '</li>');
  } 
  socket.onopen = function(ev){
    socket.send('Hi, this is Client!!');
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
