########################
#
# B3 Bitchslap Command
#
########################

__author__ = 'HSO Clan Development http://www.hsoclan.co.uk'
__version__ = '0.0.2'

import b3.events


class UrtbslapPlugin(b3.plugin.Plugin):
    minlevel = 0
    _adminPlugin = None

    def onLoadConfig(self):
        try:
            self.minlevel = self.config.getint('settings', 'minlevel')
        except:
            self.minlevel = 80

    def onStartup(self):
        self._adminPlugin = self.console.getPlugin('admin')
        if self._adminPlugin:
            self._adminPlugin.registerCommand(self, 'mslap', self.minlevel, self.cmd_mslap, 'f')
            self._adminPlugin.registerCommand(self, 'bslap', self.minlevel, self.cmd_bslap, 'f')

    def cmd_mslap(self, data, client=None, cmd=None):
        input = self._adminPlugin.parseUserCmd(data)
        if not input:
            client.message('^7command is !mslap <playername or partialname> <number of slaps>')
            return False
        if len(input) < 2:
            client.message('^7 correct syntax is !mslap <playername or part> <number of slaps>')
            return False
        cname = input[0]
        creps = input[1]
        sclient = self._adminPlugin.findClientPrompt(cname, client)
        if not sclient: return False
        self.console.write('bigtext "^7Play by 30+ Rules Please!"')
        self.__do_slap(sclient, int(creps))
        return True

    def cmd_bslap(self, data, client=None, cmd=None):
        input = self._adminPlugin.parseUserCmd(data)
        if not input:
            client.message('^7Slap who???')
            return False
        sclient = self._adminPlugin.findClientPrompt(input[0], client)
        if not sclient:
            return False
        self.console.write('bigtext "^7Slapped to Death Because You Deserved It!"')
        self.__do_slap(sclient, 20)

    def __do_slap(self, sclient, reps):
        while reps > 0:
            self.console.write('slap %s' % (sclient.cid))
            reps -= 1