import soco
import sys

zones = soco.discover()
if zones == None:
    print "No Sonos players discovered on this network."
else:
    for zone in zones:
        print "\"" + zone.player_name + "\""

sys.exit(0)


if __name__ == "__main__":
    main()