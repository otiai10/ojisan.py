import re
from geventwebsocket.handler import WebSocketHandler
from gevent import pywsgi

from mods import *

# 1 room by 1 app
chatroom = Chatroom()

def myapp (environ, set_header):

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

  me = Member(environ['HTTP_SEC_WEBSOCKET_KEY'],environ['wsgi.websocket'])
  chatroom.add_member(me)
  print '>>>>>>>>>>> ENTER : %s' % str(chatroom.get_member_count())
  while 1:
    msg = me.listen()
    if msg is None:
      chatroom.remove_member(me)
      break
    else:
      removed_list = chatroom.handle_message(msg, me)
    if me.get_key() in removed_list:
      break
  print '<<<<<<<<<< EXIT: %s' % str(chatroom.get_member_count())

server = pywsgi.WSGIServer(('oti10.com', 9090), myapp, handler_class = WebSocketHandler)
server.serve_forever()
