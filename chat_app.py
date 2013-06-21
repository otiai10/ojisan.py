# -*- coding: utf-8 -*-
import os, json, random, datetime
from geventwebsocket.handler import WebSocketHandler
from gevent import pywsgi, sleep
from mods.usher import Usher

usher = Usher()

def chat_handle (environ, start_response):
  key = environ['HTTP_SEC_WEBSOCKET_KEY']
  if usher.is_room_available():
    _nick_tmp = key[0:4]
    usher.add_member({'key':key,'socket':environ['wsgi.websocket'],'nickname':_nick_tmp})
  else:
    return False

  ws = usher.get_member_socket(key)
  print '>>>>>>>>>>> ENTER', usher.get_member_num()
  while 1:
    msg = ws.receive().encode('utf-8')
    if msg is None:
      break
    remove = set()
    for key, member in usher.find_all_members().iteritems():
      try:
        res = {
          'message'   : "This is Server. I've just got your message => " + msg,
          'echo'      : msg,
          'timestamp' : str(datetime.datetime.now()),
          'id'        : key,
          'nickname'  : usher.get_name_by_key(key),
        }
        jsn =  json.dumps(res, ensure_ascii=False)
        print member
        member['socket'].send(jsn)
      except Exception:
        remove.add(key)
    for s in remove:
      usher.remove_member(key)
  print '<<<<<<<<<< EXIT' , usher.get_member_num()

def myapp (environ, start_response):
  path = environ["PATH_INFO"]
  if path == '/':
    start_response('200 OK',[("Content-type","text/html")])
    return open('./src/view/index.html').read()
  elif path == '/chat':
    return chat_handle(environ, start_response)
  elif path == '/js/main.js':
    start_response('200 OK',[("Content-type","text/javascript")])
    return open('./src/js/main.js').read()
  elif path == '/css/main.css':
    start_response('200 OK',[("Content-type","text/css")])
    return open('./src/css/main.css').read()
  elif path == '/favicon.ico':
    start_response('200 OK',[("Content-type","image/jpeg")])
    return open('./src/img/favicon.jpg').read()
  else:
    pass
  #raise Exception('Not Found!')

server = pywsgi.WSGIServer(('otiai10.com', 9090), myapp, handler_class = WebSocketHandler)
server.serve_forever()
