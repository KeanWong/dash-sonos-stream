import soco
from soco.snapshot import Snapshot
import sys


class UndiscoverablePlayerError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)


def discover_target_sonos_player(target_name):
    zones = soco.discover()
    if zones == None:
        print "No Sonos players discovered on this network."
    else:
        for zone in zones:
            if zone.player_name == target_name:
                return zone

    raise UndiscoverablePlayerError(target_name)



sonos_player_name = "Kitchen"
try:
    player = discover_target_sonos_player(sonos_player_name)
except UndiscoverablePlayerError as e:
    print "Can't find the target Sonos player " + e.value
    sys.exit(0)

sonos = soco.SoCo(player.ip_address)
snap = Snapshot(sonos)    # create snapshot class
snap.snapshot()    # take a snapshot of current state

if snap.media_uri == "":
    print "No media uri found - is the Sonos player playing something?"
else:
    print 'media_uri: ', snap.media_uri
sys.exit(0)

if __name__ == "__main__":
    main()