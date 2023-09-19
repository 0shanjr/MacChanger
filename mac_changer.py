#/user/bin/env/python
#by oshanjr

import  subprocess

new_mac = input("Enter your New Mac Address =")

print("*****************************")
print("[+]changing your Eth0 mac address to = " + new_mac)
print("*****************************")

subprocess.run(["ifconfig", "eth0", "down"])
subprocess.run(["ifconfig", "eth0", "hw","ether", new_mac])
subprocess.run(["ifconfig", "eth0", "up"])

