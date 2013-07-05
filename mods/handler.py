import json

class Handler:

  __message    = {}
  __chatroom   = object
  __generator  = object
  __result     = object

  __gnrtr_root = 'mods.result.'
  __gnrtr_clss = 'Main'

  def __init__(self, chatroom, message):
    self.__message  = json.loads(message)
    self.__chatroom = chatroom

  def parse(self):
    mod_name   = self.__gnrtr_root + '.'.join(self.__message['request'].split('/')[1:])
    class_name = self.__gnrtr_clss
    mod = __import__(mod_name, globals(), locals(), [class_name], -1)
    clss = getattr(mod, class_name)
    self.__generator = clss()
    return self

  def generate(self):
    return self.__generator.before().perform().after()
