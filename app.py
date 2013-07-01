import os, json, datetime, re
from geventwebsocket.handler import WebSocketHandler
from gevent import pywsgi

def socket_by_socket(environ):

  ws = environ['wsgi.websocket']

  print '>>>>>>>>>>> ENTER'

  removed_list = set()

  while 1:
    # wait message from this socket
    msg = ws.receive()
    if msg is None:
      break
    else:
      ws.send(msg)
  print '<<<<<<<<<< EXIT'

def myapp (environ, set_header):
  path = environ["PATH_INFO"]
  if path == '/':
    set_header('200 OK',[("Content-type","text/html")])
    return open('assets/view/index.html').read()
  elif path == '/chat':
    return socket_by_socket(environ)
  elif path == '/js/main.js':
    set_header('200 OK',[("Content-type","text/javascript")])
    return open('assets/js/main.js').read()
  else:
    set_header('200 OK',[])
    return ''

server = pywsgi.WSGIServer(('oti10.com', 9090), myapp, handler_class = WebSocketHandler)
server.serve_forever()
