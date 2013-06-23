
class Main:
  def __init__(self):
    pass

  def before(self, params):
    self.params = params

  def perform(self):
    message = self.params['message'].encode('utf-8')
    self.result = {
      'content' : {
        'message' : message,
        'kaotype' : self.params['kaotype'],
      },
      'sender'  : self.params['id'],
    }

  def after(self):
    self.result['private'] = False
    return self.result
