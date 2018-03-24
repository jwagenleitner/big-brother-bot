# -*- coding: utf-8 -*-

# ################################################################### #
#                                                                     #
#  BigBrotherBot(B3) (www.bigbrotherbot.net)                          #
#  Copyright (C) 2005 Michael "ThorN" Thornton                        #
#                                                                     #
#  This program is free software; you can redistribute it and/or      #
#  modify it under the terms of the GNU General Public License        #
#  as published by the Free Software Foundation; either version 2     #
#  of the License, or (at your option) any later version.             #
#                                                                     #
#  This program is distributed in the hope that it will be useful,    #
#  but WITHOUT ANY WARRANTY; without even the implied warranty of     #
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the       #
#  GNU General Public License for more details.                       #
#                                                                     #
#  You should have received a copy of the GNU General Public License  #
#  along with this program; if not, write to the Free Software        #
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA      #
#  02110-1301, USA.                                                   #
#                                                                     #
# ################################################################### #

import re
from b3.parsers.iourt42 import Iourt42Parser


__version__ = '1.30.1'


class Iourt43Parser(Iourt42Parser):

    gameName = 'iourt43'

    _rePlayerScore = re.compile(r'^(?P<slot>[0-9]+):(?P<name>.*)\s+'
                                r'TEAM:(?P<team>RED|BLUE|SPECTATOR|FREE)\s+'
                                r'KILLS:(?P<kill>[0-9]+)\s+'
                                r'DEATHS:(?P<death>[0-9]+)\s+'
                                r'ASSISTS:(?P<assist>[0-9]+)\s+'
                                r'PING:(?P<ping>[0-9]+|CNCT|ZMBI)\s+'
                                r'AUTH:(?P<auth>.*)\s+IP:(?P<ip>.*)$', re.IGNORECASE)

    ## kill modes
    MOD_WATER = '1'
    MOD_LAVA = '3'
    MOD_TELEFRAG = '5'
    MOD_FALLING = '6'
    MOD_SUICIDE = '7'
    MOD_TRIGGER_HURT = '9'
    MOD_CHANGE_TEAM = '10'
    UT_MOD_KNIFE = '12'
    UT_MOD_KNIFE_THROWN = '13'
    UT_MOD_BERETTA = '14'
    UT_MOD_DEAGLE = '15'
    UT_MOD_SPAS = '16'
    UT_MOD_UMP45 = '17'
    UT_MOD_MP5K = '18'
    UT_MOD_LR300 = '19'
    UT_MOD_G36 = '20'
    UT_MOD_PSG1 = '21'
    UT_MOD_HK69 = '22'
    UT_MOD_BLED = '23'
    UT_MOD_KICKED = '24'
    UT_MOD_HEGRENADE = '25'
    UT_MOD_SR8 = '28'
    UT_MOD_AK103 = '30'
    UT_MOD_SPLODED = '31'
    UT_MOD_SLAPPED = '32'
    UT_MOD_SMITED = '33'
    UT_MOD_BOMBED = '34'
    UT_MOD_NUKED = '35'
    UT_MOD_NEGEV = '36'
    UT_MOD_HK69_HIT = '37'
    UT_MOD_M4 = '38'
    UT_MOD_GLOCK = '39'
    UT_MOD_COLT1911 = '40'
    UT_MOD_MAC11 = '41'
    UT_MOD_FRF1 = '42'
    UT_MOD_BENELLI = '43'
    UT_MOD_P90 = '44'
    UT_MOD_MAGNUM = '45'
    UT_MOD_TOD50 = '46'
    UT_MOD_FLAG = '47'
    UT_MOD_GOOMBA = '48'

    # HIT LOCATIONS
    HL_HEAD = '1'
    HL_HELMET = '2'
    HL_TORSO = '3'
    HL_VEST = '4'
    HL_ARM_L = '5'
    HL_ARM_R = '6'
    HL_GROIN = '7'
    HL_BUTT = '8'
    HL_LEG_UPPER_L = '9'
    HL_LEG_UPPER_R = '10'
    HL_LEG_LOWER_L = '11'
    HL_LEG_LOWER_R = '12'
    HL_FOOT_L = '13'
    HL_FOOT_R = '14'

    ## weapons id on Hit: lines are different than the one
    ## on the Kill: lines. Here the translation table
    hitweapon2killweapon = {
        1: UT_MOD_KNIFE,
        2: UT_MOD_BERETTA,
        3: UT_MOD_DEAGLE,
        4: UT_MOD_SPAS,
        5: UT_MOD_MP5K,
        6: UT_MOD_UMP45,
        8: UT_MOD_LR300,
        9: UT_MOD_G36,
        10: UT_MOD_PSG1,
        14: UT_MOD_SR8,
        15: UT_MOD_AK103,
        17: UT_MOD_NEGEV,
        19: UT_MOD_M4,
        20: UT_MOD_GLOCK,
        21: UT_MOD_COLT1911,
        22: UT_MOD_MAC11,
        23: UT_MOD_FRF1,
        24: UT_MOD_BENELLI,
        25: UT_MOD_P90,
        26: UT_MOD_MAGNUM,
        27: UT_MOD_TOD50,
        28: UT_MOD_KICKED,
        29: UT_MOD_KNIFE_THROWN,
    }

    ## damage table
    ## Fenix: Hit locations start with index 1 (HL_HEAD).
    ##        Since lists are 0 indexed we'll need to adjust the hit location
    ##        code to match the index number. Instead of adding random values
    ##        in the damage table, the adjustment will be made in _getDamagePoints.
    damage = {
        MOD_TELEFRAG: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        UT_MOD_KNIFE: [100, 60, 44, 35, 20, 20, 40, 37, 20, 20, 18, 18, 15, 15],
        UT_MOD_KNIFE_THROWN: [100, 60, 44, 35, 20, 20, 40, 37, 20, 20, 18, 18, 15, 15],
        UT_MOD_BERETTA: [100, 40, 33, 22, 13, 13, 22, 22, 15, 15, 13, 13, 11, 11],
        UT_MOD_DEAGLE: [100, 66, 57, 38, 22, 22, 42, 38, 28, 28, 22, 22, 18, 18],
        UT_MOD_SPAS: [100 ,80 ,80 ,40 ,32 ,32 ,59 ,59 ,40 ,40 ,40 ,40 ,40 ,40],
        UT_MOD_UMP45: [100, 51, 44, 29, 17, 17, 31, 28, 20, 20, 17, 17, 14, 14],
        UT_MOD_MP5K: [50, 34, 30, 22, 13, 13, 22, 20, 15, 15, 13, 13, 11, 11],
        UT_MOD_LR300: [100, 51, 44, 29, 17, 17, 31, 28, 20, 20, 17, 17, 14, 14],
        UT_MOD_G36: [100, 51, 44, 29, 17, 17, 29, 28, 20, 20, 17, 17, 14, 14],
        UT_MOD_PSG1: [100, 100, 97, 70, 36, 36, 75, 70, 41, 41, 36, 36, 29, 29],
        UT_MOD_HK69: [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50],
        UT_MOD_BLED: [15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15],
        UT_MOD_KICKED: [30, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20],
        UT_MOD_HEGRENADE: [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50],
        UT_MOD_SR8: [100, 100, 100, 100, 50, 50, 100, 100, 60, 60, 50, 50, 40, 40],
        UT_MOD_AK103: [100, 58, 51, 34, 19, 19, 39, 35, 22, 22, 19, 19, 15, 15],
        UT_MOD_NEGEV: [50, 34, 30, 22, 11, 11, 23, 21, 13, 13, 11, 11, 9, 9],
        UT_MOD_HK69_HIT: [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20],
        UT_MOD_M4: [100, 51, 44, 29, 17, 17, 31, 28, 20, 20, 17, 17, 14, 14],
        UT_MOD_GLOCK: [100, 45, 29, 35, 15, 15, 29, 27, 20, 20, 15, 15, 11, 11],
        UT_MOD_COLT1911: [100, 60, 40, 30, 15, 15, 32, 29, 22, 22, 15, 15, 11, 11],
        UT_MOD_MAC11: [50, 29, 20, 16, 13, 13, 16, 15, 15, 15, 13, 13, 11, 11],
        UT_MOD_GOOMBA: [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100],
        UT_MOD_TOD50: [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100],
        UT_MOD_FRF1: [100, 100, 96, 76, 40, 40, 76, 74, 50, 50, 40, 40, 30, 30],
        UT_MOD_BENELLI: [100, 100, 90, 67, 32, 32, 60, 50, 35, 35, 30, 30, 20, 20],
        UT_MOD_P90: [50, 40, 33, 27, 16, 16, 27, 25, 17, 17, 15, 15, 12, 12],
        UT_MOD_MAGNUM: [100, 82, 66, 50, 33, 33, 57, 52, 40, 33, 25, 25],
    }

    def __new__(cls, *args, **kwargs):
        return Iourt42Parser.__new__(cls)

    def is_valid_game(self, gamename):
        return gamename == 'q3urt43'

    def startup(self):
        """
        Called after the parser is created before run().
        """
        Iourt42Parser.startup(self)
        self.Events.createEvent('EVT_ASSIST', 'Event assist')

    def OnAssist(self, action, data, match=None):
        # Assist: 0 14 15: -[TPF]-PtitBigorneau assisted Bot1 to kill Bot2
        cid = match.group('acid')
        vid = match.group('dcid')
        aid = match.group('kcid')

        client = self.getByCidOrJoinPlayer(cid)
        if not client:
            self.debug('No client')
            return None

        victim = self.getByCidOrJoinPlayer(vid)
        if not victim:
            self.debug('No victim')
            return None

        attacker = self.getByCidOrJoinPlayer(aid)
        if not attacker:
            self.debug('No attacker')
            return None

        return self.getEvent('EVT_ASSIST', client=client, target=victim, data=attacker)

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

    def getTeamScores(self):
        """
        Return current team scores in a tuple.
        """
        data = self.write('players')
        if not data:
            return None

        line = data.split('\n')[3]
        m = re.match(self._reTeamScores, line.strip())
        if m:
            return [int(m.group('RedScore')), int(m.group('BlueScore'))]
        return None

    def getScores(self):
        """
        NOTE: this won't work properly if the server has private slots.
        See http://forums.urbanterror.net/index.php/topic,9356.0.html
        """
        data = self.write('players')
        if not data:
            return None

        scores = {'red': None, 'blue': None, 'players': {}}
        line = data.split('\n')[3]
        m = re.match(self._reTeamScores, line.strip())
        if m:
            scores['red'] = int(m.group('RedScore'))
            scores['blue'] = int(m.group('BlueScore'))

        for line in data.split('\n')[3:]:
            self.verbose("JMW: %s" % line)
            m = re.match(self._rePlayerScore, line.strip())
            if m:
                scores['players'][int(m.group('slot'))] = {'kills': int(m.group('kill')),
                                                           'deaths': int(m.group('death'))}

        return scores
