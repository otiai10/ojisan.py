import os

class Const:

  const = {
    'conf' : {
      'www15224uf' : {
        'host' : 'www15224uf.sakura.ne.jp',
        'rurl' : 'http://www15224uf.sakura.ne.jp/',
        'port' : 9090,
      }
    }
  }

  def __init__(self):
    pass

  @classmethod
  def get(self, key):
    if key == 'conf':
      host = os.uname()[1]
      return self.const['conf'][host]
    else:
      return self.const[key]
