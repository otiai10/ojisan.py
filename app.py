import os, json, datetime, re
from geventwebsocket.handler import WebSocketHandler
from gevent import pywsgi

from mods import *

def myapp (environ, set_header):
  mparser.hoge()
  chatroom = Chatroom()
  path = environ["PATH_INFO"]
  if path == '/chat':
    return socket_by_socket(environ)
  if path == '/':
    # TODO : enable partials
    set_header('200 OK',[("Content-type","text/html")])
    return open('assets/view/index.html').read()
  # {{{  handle js request
  # TODO : squash to Asset module
  elif re.match('/js/app.js', path):
    set_header('200 OK',[("Content-type","text/javascript")])
    return open('assets/js/app.js').read()
  elif re.match('/js/core/jquery.js', path):
    set_header('200 OK',[("Content-type","text/javascript")])
    return open('assets/js/core/jquery.js').read()
  elif re.match('/js/core/underscore.js', path):
   set_header('200 OK',[("Content-type","text/javascript")])
   return open('assets/js/core/underscore.js').read()
  elif re.match('/js/core/backbone.js', path):
   set_header('200 OK',[("Content-type","text/javascript")])
   return open('assets/js/core/backbone.js').read()
  # }}}
  else:
    set_header('200 OK',[])
    return ''

def socket_by_socket(environ):

  ws = environ['wsgi.websocket']

  member = Member(ws)
  print '>>>>>>>>>>> ENTER'
  while 1:
    msg = ws.receive()# wait for message
    if msg is None:
      break
    else:
      ws.send(msg)
  print '<<<<<<<<<< EXIT'

server = pywsgi.WSGIServer(('oti10.com', 9090), myapp, handler_class = WebSocketHandler)
server.serve_forever()
