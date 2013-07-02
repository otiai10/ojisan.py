var __my_id = '';
var __unread_cnt = 0;
var __socket;

$(function(){
  alert('ready');
  __socket = new WebSocket("ws://oti10.com:9090/chat");
  __socket.onmessage = function(ev){
    console.log('message event => ', ev);
  } 
  __socket.onopen = function(ev){
    console.log('open event => ', ev);
    first_mess = JSON.stringify({'request':'/me/id','params':null});
    __socket.send(first_mess);
  }
});
