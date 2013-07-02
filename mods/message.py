import json

class Message:
  def __init__(self):
    pass

  @classmethod
  def parse(self,jsn_str):
    return json.loads(jsn_str)
