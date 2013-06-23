
class Main:
  def __init__(self):
    pass

  def before(self, params):
    self.params = params

  def perform(self):
    self.result = {
      'content' : {
        'id' : self.params['socket_key'],
      },
      'sender'  : self.params['socket_key'],
    }

  def after(self):
    self.result['private'] = True
    return self.result
