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

from .iourt42 import Poweradminurt42Plugin


class Poweradminurt43Plugin(Poweradminurt42Plugin):

    requiresParsers = ['iourt43']

    _weapons43 = dict(p90='k', frf1='i', mag='l', ben='j')

    _weapon_aliases43 = {
        "nail": "p90",
        "fr": "frf1",
        "44": "mag",
        ".44": "mag",
        "slug": "ben",
    }

    _weapon_groups43 = {
        'all_snipers': 'NZi',
        'all_pistols': 'FGfgl',
        'all_auto': 'IJLMacehk',
        'all_shotgun': 'Hj',
        'all_sec': 'HIJhjk',
        'all_ak': 'HIJhjkFGfgl',
    }

    def onStartup(self):
        """
        Initialize plugin settings
        """
        Poweradminurt42Plugin.onStartup(self)

        # Adjust for new weapons in 4.3
        self._gears['none'] = 'FGHIJKLMNZacefghijklOQRSTUVWX'
        self._weapons.update(self._weapons43)
        self._weapon_aliases.update(self._weapon_aliases43)
        self._weapon_groups.update(self._weapon_groups43)

    def registerEvents(self):
        """
        Register events needed
        """
        Poweradminurt42Plugin.registerEvents(self)

    def onLoadConfig(self):
        """
        Load plugin configuration
        """
        Poweradminurt42Plugin.onLoadConfig(self)

    def cmd_pagungame(self, data, client, cmd=None):
        """
        Change game type to Gun Game
        (You can safely use the command without the 'pa' at the beginning)
        """
        self.console.setCvar('g_gametype', '11')
        if client:
            client.message('^7game type changed to ^4Gun Game')
        self.set_configmode('gungame')

    def cmd_painstagib(self, data, client, cmd=None):
        """
        Turn instagib game mode <on/off>
        (You can safely use the command without the 'pa' at the beginning)
        """
        if not data or data.lower() not in ('on', 'off'):
            client.message('^7You must provide an argument of "on" or "off", try !help painstagib')
            return

        if data.lower() == 'on':
            self.console.setCvar('g_instagib', '1')
            self.console.say('^7Instagib mode: ^2ON')
        elif data.lower() == 'off':
            self.console.setCvar('g_instagib', '0')
            self.console.say('^7Instagib mode: ^1OFF')

    def cmd_pahardcore(self, data, client, cmd=None):
        """
        Set the g_hardcore <on/off>
        (You can safely use the command without the 'pa' at the beginning)
        """
        if not data or data.lower() not in ('on', 'off'):
            client.message('^7You must provide an argument of "on" or "off", try !help pahardcore')
            return

        if data.lower() == 'on':
            self.console.setCvar('g_hardcore', 1)
            self.console.say('^7Hardcore: ^2ON')
        elif data.lower() == 'off':
            self.console.setCvar('g_hardcore', 0)
            self.console.say('^7Hardcore: ^1OFF')

    def _gear_contains_sniper(self, gear):
        return 'Z' in gear or 'N' in gear or 'i' in gear
