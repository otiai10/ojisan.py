# -*- coding: utf-8 -*-
import os, json, datetime, re
from geventwebsocket.handler import WebSocketHandler
from gevent import pywsgi, sleep

from mods.usher import Usher
from mods.asset import Asset
from mods.const import Const

usher = Usher()
conf  = Const.get('conf')

def chat_handle (environ, set_header):
  key = environ['HTTP_SEC_WEBSOCKET_KEY']
  if usher.is_room_available():
    _nick_tmp = key[0:4]
    usher.add_member({'key':key,'socket':environ['wsgi.websocket'],'nickname':_nick_tmp})
  else:
    return False

  ws = usher.get_member_socket(key)
  print '>>>>>>>>>>> ENTER', usher.get_member_num()
  while 1:
    msg = ws.receive()
    if msg is None:
      break
    remove = set()
    msg = msg.encode('utf-8')
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
        # print member
        member['socket'].send(jsn)
      except Exception:
        remove.add(key)
    for s in remove:
      usher.remove_member(key)
  print '<<<<<<<<<< EXIT' , usher.get_member_num()

def myapp (environ, set_header):
  path = environ["PATH_INFO"]
  if path == '/':
    # first rendering
    set_header('200 OK',[("Content-type","text/html")])
    return Asset('/view/index.html').get()
  elif path == '/chat':
    # ws connection
    return chat_handle(environ, set_header)
  elif re.match('.*\.js', path) is not None:
    set_header('200 OK',[('Content-Type','text/javascript')])
    return Asset(path).apply({'host':conf['host'],'port':conf['port']}).get()
  elif re.match('.*\.css', path) is not None:
    set_header('200 OK',[('Content-Type','text/css')])
    return Asset(path).get()
  else:
    set_header('200 OK',[])
    return Asset(path).get()

server = pywsgi.WSGIServer((conf['host'], conf['port']), myapp, handler_class = WebSocketHandler)
server.serve_forever()
