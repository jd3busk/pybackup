# pybackup
## Cloning this repo
git clone https://github.com/jd3busk/pybackup.git\

## Virtual Environment Setup
cd pybackup\
python3 -m venv .venv\
source .venv/bin/activate\
pip install -r requirements.txt\

## Modifying your Inventory
Use **vi** or **nano** and edit the _inventory.txt_ file.
These entries can be IP or FQDN (assuming DNS works).

## Set creds as local environmental variables (optional)
export NETMIKO_USERNAME="cisco"
export NETMIKO_PASSWORD="cisco"
