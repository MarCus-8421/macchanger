#!/usr/bin/env python3

import subprocess

# Mac Changer

NC = input("[+]Enter the Interface: ")    # NC= Network Card
mac = input("[+]Enter the MAC address: ")

print("[+]Changing MAC address for " + NC + "to" + mac )

subprocess.call("ifconfig " + NC + " down", shell=True)
subprocess.call("ifconfig " + NC + " hw ether " + mac,  shell=True)
subprocess.call("ifconfig " + NC + " up", shell=True)

print("[+]Done")
