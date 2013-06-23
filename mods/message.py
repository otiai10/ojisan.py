import json, datetime
from mods.handler import Handler
from mods.usher import Usher

class Message:

  def __init__(self, to_member):
    self.to_member = to_member

  def build(self, params):
    if params['sender']['key'] == self.to_member['key']:
      is_me = True
    else:
      is_me = False
    response = {
      'content' : params['content'],
      'sender'  : {
        'nickname' : params['sender']['nickname'],
        'is_me'    : is_me
      },
      'request' : params['request'],
    }
    #return json.dumps(response, ensure_ascii=False)
    return json.dumps(response)

  @classmethod
  def handle(self, msg, key):
    msg = msg.encode('utf-8')
    _orig = json.loads(msg)
    _orig['socket_key'] = key
    result = Handler(_orig).execute()
    return result

