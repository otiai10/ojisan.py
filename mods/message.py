import json, datetime

class Message:

  def __init__(self, member):
    self.member = member

  def handle(self, msg):
    self.msg = msg.encode('utf-8')
    return self

  def generate(self):
    res = {
      'message'   : "This is Server. I've just got your message => " + self.msg,
      'echo'      : self.msg,
      'timestamp' : str(datetime.datetime.now()),
      'id'        : self.member['key'],
      'nickname'  : self.member['nickname']
    }
    self.result = json.dumps(res, ensure_ascii=False)
    return self.result

  @classmethod
  def parse_request(self, request_str):
    print request_str.split('/')
