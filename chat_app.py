# -*- coding: utf-8 -*-
import os
import random
from geventwebsocket.handler import WebSocketHandler
from gevent import pywsgi, sleep

print __file__

ws_list = set()

def chat_handle (environ, start_response):
  global cnt
  ws = environ['wsgi.websocket']
  ws_list.add(ws)
  print '>>>>>>>>>>> ENTER', len(ws_list)
  while 1:
    # msg = ws.wait()
    # @see : http://www.gelens.org/code/gevent-websocket/
    msg = ws.receive()
    msg = msg.encode('utf-8')
    if msg is None:
      break
    remove = set()
    for s in ws_list:
      try:
        s.send("This is Server. I'v just got your message => " + msg)
      except Exception:
        remove.add(s)
    for s in remove:
      ws_list.remove(s)
  print '<<<<<<<<<< EXIT' , len(ws_list)

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
