#!/bin/python

import sys
import os
import json


class Profiler(object):
    """Maintain and impliment built profiles. Call main to init the profiles."""

    def __init__(self):
        super(Profiler, self).__init__()
        self.profiles = []
        self.profiles_dir = './profiles/'
        self.manifest = 'manifest.json'

    def load_profiles(self):
        try:
            self.profiles = json.load(
                open(self.profiles_dir + self.manifest, 'r').close())
        except FileNotFoundError as e:
            pass

    def create_profile(self, lsb_release, uname):
        """Looks through the output of uname and lsb_release to determine
        versions"""
        distro, kver, arch = '', '', ''
        kver, arch = uname[0].split()
        for info in lsb_release:
            if "Distributor" in info:
                distro = info[16:].lower()

        profile = {
            "distro": distro,
            "kver": kver,
            "arch": arch,
            "module": "lime-{0}-{1}-{2}.ko".format(distro, kver, arch),
            "profile": "vol-{0}-{1}-{2}.zip".format(distro, kver, arch)
            }
        self.profiles.append(profile)
        json.dump(self.profiles, open(self.profiles_dir + self.manifest, 'w'))

        return profile

    def interactive_chooser(self):
        """Interactive CLI mode for choosing pre-compiled modules. The profiles
        are a list of dicts."""
        profile_dict = None
        if len(self.profiles) > 0:
            while True:
                for i, profile in enumerate(self.profiles):
                    print(
                        "%i) %s, %s, %s\t" %
                        (i, profile['distro'], profile['kver'], profile['arch']))
                profile_val = input(
                    "Please select a profile. Press [q] to exit: ")
                if profile_val > 1 or profile_val < len(self.profiles):
                    return profile

                else:
                    if distro_val == 'q':
                        return None
                    else:
                        print("Please select a correct value and try agin")

    def select_profile(self, distro, kver, arch):
        """Select a profile to have the client use."""
        if len(self.profiles) > 0:
            for i, profile in enumerate(self.profiles):
                if profile['distro'] is distro and profile['kver'] is kver and profile['arch'] is arch:
                    return profile

                else:
                    return None

    def main(self):
        self.load_profiles()

if __name__ == '__main__':
    Profiler().main()