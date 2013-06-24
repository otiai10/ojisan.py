import os, json, datetime, re
from geventwebsocket.handler import WebSocketHandler
from gevent import pywsgi, sleep

from mods import Usher, Asset, Const, Message

usher = Usher()
conf  = Const.get('conf')

def socket_by_socket(environ):
  key = environ['HTTP_SEC_WEBSOCKET_KEY']
  if usher.is_room_available():
    _nick_tmp = key[0:4]
    usher.add_member({'key':key,'socket':environ['wsgi.websocket'],'nickname':_nick_tmp})
  else:
    return False

  ws = usher.get_member_socket(key)
  print '>>>>>>>>>>> ENTER', usher.get_member_num()
  removed_list = set()
  while 1:

    # wait message from this socket
    msg = ws.receive()

    if msg is None:
      removed_list.add(key)
    else:
      # --- handle msg
      result = Message.handle(msg, key)
      # ---

      # --- append sender info
      if 'nickname' in result:
        usher.set_nickname(result['sender'], result['nickname'])
      sender = usher.get_member(result['sender'])
      if sender is None:
        removed_list.add(result['sender'])
      result['sender'] = sender 
      # ---

      # --- send
      if result['private']:
        to_member = usher.get_member(key)
        message = Message(to_member).build(result)
        ws.send(message)
        continue
      for key, to_member in usher.find_all_members().iteritems():
        message = Message(to_member).build(result)
        try:
            to_member['socket'].send(message)
        except Exception as e:
          # print e.message
          removed_list.add(key)
      # ---

    # --- refresh member list
    already_left = False
    for k in removed_list:
      removed_member = usher.get_member(k)
      remained_members = usher.remove_member(k, get_remained=True)
      for rk,rm in remained_members.iteritems():
        msg = json.dumps({'request':'/me/leave','removed_member':{'nickname':removed_member['nickname'],'id':removed_member['key']},'kaotype':'101'}).encode('utf-8')
        result  = Message.handle(msg, key)
        message = Message(rm).build(result)
        try:
          rm['socket'].send(message)
        except Exception as e:
          # print e.message
          pass
      if k == key:
        # it's me
        already_left = True
    # ---

    if already_left:
      break

  print '<<<<<<<<<< EXIT' , usher.get_member_num()

def myapp (environ, set_header):
  path = environ["PATH_INFO"]
  if path == '/':
    set_header('200 OK',[("Content-type","text/html")])
    return Asset('/view/index.html').get()
  elif path == '/chat':
    return socket_by_socket(environ)
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
