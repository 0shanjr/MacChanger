#/user/bin/env/python

import  subprocess

new_mac = input("Enter your New Mac Address =")

# subprocess.call("ifconfig",shell=True)
print("*****************************")
print("[+]changing your Eth0 mac address to = " + new_mac)
print("*****************************")

# subprocess.call("ifconfig eth0 down",shell=True)
# subprocess.call("ifconfig eth0 hw ether " + new_mac ,shell=True)
# subprocess.call("ifconfig eth0 up",shell=True)

subprocess.run(["ifconfig", "eth0", "down"])
subprocess.run(["ifconfig", "eth0", "hw","ether", new_mac])
subprocess.run(["ifconfig", "eth0", "up"])

