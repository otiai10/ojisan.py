
class Member:

  __name   = ''
  __key     = ''
  __socket = object
  __room   = object

  def __init__(self, _key, socket):
    self.__key     = _key
    self.__socket = socket
    self.set_default_nickname()

  def set_default_nickname(self):
    self.__name = self.__key[:5]

  def listen(self):
    return self.__socket.receive()

  def receive_message(self,mess):
      self.__socket.send(mess)

  def set_chatroom(self, room):
      self.__room = room

  def get_key(self):
    return self.__key
