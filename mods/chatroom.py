from handler import Handler

class Chatroom:

  __members = []
  __removed_members = []

  def __init__(self):
    pass

  #def join(self, member):
  def add_member(self, member):
    member.set_chatroom(self)
    if member not in self.__members:
      # mess = message.generate('hoge')
      # self._deliver_all(mess)
      self.__members.append(member)

  def remove_member(self, member):
    if member in self.__members:
      # mess = hoge
      self.__members.remove(member)

  def deliver_all(self, mess):
    for member in self.__members:
      try:
        member.receive_message(mess)
      except:
        # this use has left this room
        self.__removed_members.append(member.get_key())

  def deliver(self, to_member, mess):
    try:
      to_member.receive_message
    except:
      self.__removed_members.append(member.get_key())

  def handle_message(self, message, socket_owner):
    res = Handler(self, message).parse().generate()
    if res.is_private:
      sender = socket_owner
      self.deliver(sender, res.get_content())
    else:
      self.deliver_all(res.get_content())
    removed_members = self.__removed_members
    self.refresh_members(self.__removed_members)
    return removed_members

  # use lambda??
  # TODO: refactor
  def refresh_members(self, removed_members):
    new_members = []
    for member in self.__members:
      if member not in removed_members:
        new_members.append(member)
    self.__members = new_members
    return removed_members

  def get_member_count(self):
    return len(self.__members)

  def get_member_by_key(self, key):
    for member in self.__members:
      if key is member.get_key():
        return member
