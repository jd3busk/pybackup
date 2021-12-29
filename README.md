# pybackup
## Description
This script utilizes the netmiko library to SSH to clients and backup their configurations. The script assumes a shared SSH username and password will be used for authentication.

## Cloning this repo
```
git clone https://github.com/jd3busk/pybackup.git
```

## Virtual Environment Setup
```
cd pybackup
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

## Modifying your Inventory
Use **vi** or **nano** and edit the _inventory.txt_ file.\
These entries can be IP or FQDN (assuming DNS works).

## Running the script
```
python backup.py
```

## (Optional) Set creds as local environmental variables
If you don't wish to be prompted for credentials everytime the script is ran you can optionally set the following environmental variables.
```
export NETMIKO_USERNAME="cisco"
export NETMIKO_PASSWORD="cisco"
```
