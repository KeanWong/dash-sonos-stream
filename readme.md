Playing a Streaming Radio source with your Amazon Dash
===
Installation
---
1. Follow the instructions on the [dash-test project](https://github.com/KeanWong/dash-test) to configure your Dash button and install all the other requirements (including _scapy_).
 2. Install the additional requirements for this project using `pip install -r requirements.txt'.`
 3. Make sure your computer is on the same subnet as your Sonos players (usually the same Wifi network is fine). Discover the name of all of the players on the network by running `python ./list_players.py`

    The list will look something like this:

    `"Garage"`  
    `"Kitchen"`  
    `"Study"`  
    `"Dining Room"`  

     The double quotation marks around the player names are inserted to delineate when long payer names with spaces start and end. Do not copy the quotes in the next step.
 4. In _print_current_uri.py_, edit line 26 to set the _sonos_player_name_ to the name of the player you want to steam to.
 5. Using your usual Sonos controller (e.g. the Sonos phone app), manually start the player you selected to play the stream that you want to trigger when you push the Dash button.
 6. Run `python ./print_current_uri.py` to print the uri of the broadcast stream you want to trigger when the Dash button is pressed.  It will look something like:  
  `media_uri:  x-sonosapi-stream:s34804?sid=254&flags=32`
 7. In _play_stream.py_, edit line 13 to point to the name of the Sonos player you want the Dash button to trigger.
 8. Edit line 43 to contain the uri of the media stream (e.g. for KQED enter `sonos.play_uri('x-sonosapi-stream:s34804?sid=254&flags=32', title='KQED)`).  You **must** enter a title, but it can be anything.
 9. Edit line 60 to reference the ethernet MAC address of your Dash button (see the [dash-test project](https://github.com/KeanWong/dash-test) project for instructions on how to discover the MAC ID)
 10. Run `python ./play_stream.py` to play the stream on the target Sonos player when the Dash button is pressed.
 11. CTRL-C exits the program. 