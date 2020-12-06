# LiMEaide
# Copyright (c) 2011-2018 Daryl Bennett

# Author:
# Daryl Bennett - kd8bny@gmail.com

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or (at
# your option) any later version.

# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA

import configparser
import os

class Client:
    """All client attributes including the profile.

    The profile format is stored as json as such
    profile = {
        "distro": distro,
        "kver": kver,
        "arch": arch,
        "module": "lime.ko",
        "profile": "vol.zip"
        }
    """

    def __init__(self):
        super(Client, self).__init__()
        # Client specifics
        self.ip = None
        self.port = None
        self.user = None
        self.pass_ = None
        self.key = None

        # LiME options
        self.output = None
        self.format = None
        self.digest = None

        # Profile and options
        self.profile = None
        self.output_dir = None
        self.compress = None
        self.job_name = None

        #Configuration file
        self.config_file = ".client"

    def read_config(self):
        """Read default configuration."""

        if not os.path.isfile(self.config_file):
            self.write_config(True)

        default_config = configparser.ConfigParser()
        default_config.read(self.config_file)

        self.ip = default_config['DEFAULT']['ip']
        self.port = default_config['DEFAULT']['port']
        self.user = default_config['DEFAULT']['user']
        self.output = default_config['DEFAULT']['output']
        self.format = default_config['DEFAULT']['format']
        self.digest = default_config['DEFAULT']['digest']
        self.compress = default_config['DEFAULT']['compress']



    def write_config(self, default):

        default_config = configparser.ConfigParser()

        if default:
            default_config['MANIFEST'] = {}
            default_config['MANIFEST']['version'] = "1"
            default_config.set('DEFAULT', 'ip', '')
            default_config.set('DEFAULT', 'port', '')
            default_config.set('DEFAULT', 'user', '')
            default_config.set('DEFAULT', 'output', 'dump.lime')
            default_config.set('DEFAULT', 'format', 'lime')
            default_config.set('DEFAULT', 'digest', 'sha1')
            default_config.set('DEFAULT', 'compress', 'False')
        else:
            default_config['MANIFEST'] = {}
            default_config['MANIFEST']['version'] = "1"
            default_config.set('DEFAULT', 'ip', str(self.ip))
            default_config.set('DEFAULT', 'port', str(self.port))
            default_config.set('DEFAULT', 'user', str(self.user))
            default_config.set('DEFAULT', 'output', str(self.output))
            default_config.set('DEFAULT', 'format', str(self.format))
            default_config.set('DEFAULT', 'digest', str(self.digest))
            default_config.set('DEFAULT', 'compress', str(self.compress))


        with open(self.config_file, 'w') as configfile:
            default_config.write(configfile)