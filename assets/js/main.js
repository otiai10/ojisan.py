var __my_id = '';
var kaomoji = {
  '0':'(ﾟ⊿ﾟ)',
  '1':'(☝ ՞ਊ ՞）☝',
  '2':'（；^ω^）',
  '3':'(´・ω・`)',
  '101':'( ・`д・´)ｷﾘｯ',
};

$(function(){
  socket = new WebSocket("ws://%{host}:%{port}/chat");
  socket.onmessage = function(ev){
    var data = JSON.parse(ev.data);
    // console.log(data);
    dispatchMessage(data);
  } 
  socket.onopen = function(ev){
    // console.log('open event => ', ev);
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

  $(".nnchange").on('click', function(){
    var nickname = $("#nickname").val();
    var kaotype = $(this).attr('kaotype');
    if (nickname) {
      var data = JSON.stringify({'request':'/me/nickname','nickname':nickname,'kaotype':kaotype,'id':__my_id});
      socket.send(data);
      $("#message").val('').focus();
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
    case '/me/nickname':
      $('#nickname').val(data.content.nickname);
      $('#stream').prepend(buildMessageHTML(data));
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
  str += '<td class="content"><span>' + data.content.message + '</span></td>';
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
  return kaomoji[data.content.kaotype];
}
