#
# BigBrotherBot(B3) (www.bigbrotherbot.net)
# Copyright (C) 2012 Thomas LEVEIL <courgette@bigbrotherbot.net>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA
#

import re
from b3.parsers.iourt42 import Iourt42Parser

class Iourt43Parser(Iourt42Parser):

    gameName = 'iourt43'

    _rePlayerScore = re.compile(r'^(?P<slot>[0-9]+):(?P<name>.*)\s+'
                                r'TEAM:(?P<team>RED|BLUE|SPECTATOR|FREE)\s+'
                                r'KILLS:(?P<kill>[0-9]+)\s+'
                                r'DEATHS:(?P<death>[0-9]+)\s+'
                                r'ASSISTS:(?P<assist>[0-9]+)\s+'
                                r'PING:(?P<ping>[0-9]+|CNCT|ZMBI)\s+'
                                r'AUTH:(?P<auth>.*)\s+IP:(?P<ip>.*)$', re.IGNORECASE)

    def __new__(cls, *args, **kwargs):
        return Iourt42Parser.__new__(cls)

    def startup(self):
        """
        Called after the parser is created before run().
        """
        try:
            cvar = self.getCvar('gamename')
            gamename = cvar.getString() if cvar else None
            if gamename != 'q3urt43':
                self.error("The iourt43 B3 parser cannot be used with a game server other than Urban Terror 4.3 [%s]" % gamename)
                raise SystemExit(220)
        except Exception, e:
            self.warning("Could not query server for gamename.", exc_info=e)

        Iourt42Parser.startup(self)

    def defineGameType(self, gametype_int):
        """
        Translate the gametype to a readable format (also for teamkill plugin!)
        """
        gametype = str(gametype_int)

        if gametype == '11':
            gametype = 'gungame'
        else:
            gametype = Iourt42Parser.defineGameType(self, gametype_int)

        return gametype
