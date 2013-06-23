class Handler:

  def __init__(self, params):
    self.procedure = self._get_instance(params['request'])
    self.params = params

  def execute(self):
    self.procedure.before(self.params)
    self.procedure.perform()
    result = self.procedure.after()
    result['request'] = self.params['request']
    return result

  def _get_instance(self, request):
    mod_name   = 'mods.procedure.' + '.'.join(request.split('/')[1:])
    class_name = 'Main'
    mod = __import__(mod_name, globals(), locals(), [class_name], -1)
    clss = getattr(mod, class_name)
    return clss()
