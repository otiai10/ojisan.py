import re

class Asset:
  def __init__(self, fpath):
    self.path = 'assets'
    self.prmt = "%{value}"
    self.content = open(self.path + fpath).read()

  def apply(self, params):
    for k,v in params.iteritems():
      pat_str = self.prmt.replace('value', k)
      self.content = re.sub(pat_str, v, self.content)
    return self

  def get(self):
    return self.content
