
class Usher:
  def __init__(self):
    self.members = {}

  def get_member_num(self):
    return len(self.members)
  def get_member_socket(self, key):
    return self.members[key]['socket']

  def find_all_members(self):
    return self.members

  def is_room_available(self):
    if self.get_member_num() > 5:
      return False
    else:
      return True

  def add_member(self, member):
    self.members[member['key']] = member
    return self.members

  def get_member(self, key):
    if self.members.has_key(key):
      return self.members[key]
    else:
      return None

  def remove_member(self, key):
    if self.members.has_key(key):
      self.members.pop(key)
    return True

  def get_name_by_key(self, key):
    if self.members.has_key(key):
      return self.members[key]['nickname']
    else:
      return False

  def set_nickname(self, key, nickname):
    if self.members.has_key(key):
      self.members[key]['nickname'] = nickname
      return nickname
    else:
      return None
