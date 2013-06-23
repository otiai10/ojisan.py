import cgi

class Main:
  def __init__(self):
    pass

  def before(self, params):
    self.params = params

  def perform(self):
    new_nickname = cgi.escape(self.params['nickname'].encode('utf-8'))
    self.result = {
      'content' : {
        'message'  : 'Name changed! => ' + new_nickname,
        'nickname' : new_nickname,
        'kaotype' : 101,
      },
      'nickname' : new_nickname,
      'sender'   : self.params['id'],
    }

  def after(self):
    self.result['private'] = False
    return self.result
