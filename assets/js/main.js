var __my_id = '';
$(function(){
  socket = new WebSocket("ws://%{host}:%{port}/chat");
  socket.onmessage = function(ev){
    var data = JSON.parse(ev.data);
    dispatchMessage(data);
  } 
  socket.onopen = function(ev){
    console.log('open event => ', ev);
    mess = JSON.stringify({'request':'/me/id','params':null});
    socket.send(mess);
  }

  // register click event
  $(".submit").on('click', function(){
      var mess = $("#message").val();
      var kaotype = $(this).attr('kaotype');
      if (mess) {
        var data = JSON.stringify({'request':'/message/send','message':mess,'kaotype':kaotype,'id':__my_id});
        socket.send(data);
        $("#message").val('').focus();
      } else {
        console.log('＿人人人人人人人人人人人＿\n＞　突然の NULL String　＜\n￣Y^Y^Y^Y^Y^Y^Y^Y^Y￣');
      }
  });
});

function dispatchMessage(data){
  switch(data.request){
    case '/message/send':
      $('#stream').prepend(buildMessageHTML(data));
      break;
    case '/me/id':
      __my_id = data.content.id;
      break;
    default:
  }
}

function buildMessageHTML(data){
  var str = '<tr>';
  if (data.sender.is_me) {
    str += '<td class="person me">';
    str += getKaoHtml(data) + ' < ';
    str += '<br>' + data.sender.nickname;
    str += '</td>';
  }else{ str += '<td></td>'; }
  str += '<td><span>' + data.content.message + '</span></td>';
  if (!data.sender.is_me) {
    str += '<td class="person">';
    str += ' > ' + getKaoHtml(data);
    str += '<br>' + data.sender.nickname;
    str += '</td>';
  }else{ str += '<td></td>'; }
  str += '</tr>';
  return str;
}

function getKaoHtml(data){
  return '(ﾟ⊿ﾟ) ';
}
