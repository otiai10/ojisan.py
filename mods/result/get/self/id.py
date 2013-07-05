from mods.result.base import ResultBase

class Main(ResultBase):

  is_private = True
  conent     = {}
  sender     = object

  def __init__(self):
    pass

  def before(self):
    return self

  def perform(self):
    return self

  def after(self):
    return self
