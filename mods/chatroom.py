
class Chatroom:

  __members = []

  def __init__(self):
    print __file__
    pass

  def join(self, member):
    member.set_chatroom(self)
    if member not in self.__members:
      # mess = message.generate('hoge')
      # self._deliver_all(mess)
      pass

  def _deliver_all(self, mess):
    removed_members = []
    for member in self.__members:
      try:
        member.recieve_message(mess)
      except:
        # this use has left this room
        removed_members.append(member)
    self._refresh_members(removed_members)

  def _deliver(self, to_member, mess):
    removed_members = []
    try:
      to_member.recieve_message
    except:
      removed_members.append(member)
    self._refresh_members(removed_members)

  # use lambda??
  # TODO: refactor
  def _refresh_members(self, removed_members):
    new_members = []
    for member in self.__members:
      if member not in removed_members:
        new_members.append(member)
    self.__members = new_members

  def get_member_count(self):
    return len(self.__members)
