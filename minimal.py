def register(trg):
    trg._parent.log_message('Registering UserAction command from:%s' % __file__)
    type(trg).myrun = run
    trg._action_dict['GNIP_MINIMAL'] = 'myrun'


def run(self, track, args):
    self._parent.show_message('ClyphX GNIP_MINIMAL command is working')
    self._parent.log_message('ClyphX GNIP_MINIMAL command is working')
