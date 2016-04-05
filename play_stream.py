import datetime
import soco
from soco.snapshot import Snapshot
import sys
import requests

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *


target_volume = 30
sonos_player_name = "Master Bedroom"


class UndiscoverablePlayerError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)


def discover_target_sonos_player(target_name):
    for zone in soco.discover():
        if zone.player_name == target_name:
            return zone

    raise UndiscoverablePlayerError(target_name)


def button_pressed_npr():
    try:
        player = discover_target_sonos_player(sonos_player_name)
    except UndiscoverablePlayerError as e:
        print "Can't find the target Sonos player "+e.value
        sys.exit(0)

    sonos = soco.SoCo(player.ip_address)
    sonos.volume = target_volume

    print "Playing KQED on the " + player.player_name + " player at " + player.ip_address
    # The title is needed, oddly...
    sonos.play_uri('x-sonosapi-stream:s34804?sid=254&flags=32', title='KQED')

    # Just in case...
    sonos.volume = target_volume


def udp_filter(pkt):
    options = pkt[DHCP].options
    for option in options:
        if isinstance(option, tuple):
            if 'requested_addr' in option:
                # we've found the IP address, which means its the second and final UDP request, so we can trigger our action
                mac_to_action[pkt.src]()
                break



mac_to_action = {'74:c2:46:4a:52:af' : button_pressed_npr}
mac_id_list = list(mac_to_action.keys())
print "Listening for Dash button presses..."
sniff(prn=udp_filter, store=0, filter="udp", lfilter=lambda d: d.src in mac_id_list)



if __name__ == "__main__":
    main()