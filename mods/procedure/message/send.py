
class Main:
  def __init__(self):
    pass

  def before(self, params):
    self.params = params

  def perform(self):
    message = self.params['params'].encode('utf-8')
    self.result = {
      'content' : {
        'message' : message,
      },
      'sender'  : self.params['socket_key'],
    }

  def after(self):
    self.result['private'] = False
    return self.result
