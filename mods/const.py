import os

class Const:
  def __init__(self):
    self.conf = {
      'www15224uf' : {
        'host' : 'www15224uf.sakura.ne',
        'rurl' : 'http://www15224uf.sakura.ne.jp/',
      },
    }

  def get_conf(self):
    host = os.uname()[1]
    return self.conf[host]
