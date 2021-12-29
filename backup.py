#!/usr/bin/env python

import os
from netmiko import ConnectHandler
from datetime import datetime
from getpass import getpass



print("# CREATING BACKUP DIRECTORY")
time = datetime.now()

backup_dir = time.strftime("%Y-%m-%d_%H-%M-%S")

exists = os.path.exists(backup_dir)

if not exists:

    os.makedirs(backup_dir)



print("# IMPORTING INVENTORY")
with open("inventory.txt", "r") as raw:

    hosts_raw = raw.read()

    hosts_list = hosts_raw.splitlines()



print("# GETTING CREDENTIALS")
if os.environ.get("NETMIKO_USERNAME") is None:

    username = input("\tUsername: ")

else:

    username = os.environ.get("NETMIKO_USERNAME")

if os.environ.get("NETMIKO_PASSWORD") is None:

    password = getpass("\tPassword: ")

else:

    password = os.environ.get("NETMIKO_PASSWORD")




device = {

    'device_type': 'cisco_ios',

    'username': username,

    'password': password

    }

print("# BEGGINING BACKUPS")

for host in hosts_list:
    
    device['host'] = host

    connection = ConnectHandler(**device)

    hostname = connection.base_prompt

    config = connection.send_command("show run")

    backup_path = "{}/{}_config.txt".format(backup_dir, hostname)

    with open(backup_path, "w") as file:
        file.write(config)
    
    print("\tBacked up {} to {}".format(hostname, backup_path))
