# -*- coding: utf-8 -*-
class Main:
  def __init__(self):
    pass

  def before(self, params):
    self.params = params

  def perform(self):
    self.result = {
      'content' : {
        'message' : self.params['removed_member']['nickname'] + ' just exited this room',
        'kaotype' : self.params['kaotype'],
      },
      'sender'  : self.params['removed_member']['id'],
    }

  def after(self):
    self.result['private'] = False
    return self.result
