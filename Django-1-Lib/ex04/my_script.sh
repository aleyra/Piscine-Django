#!/usr/bin/sh

# to call: `source my_script.sh`

python3 -m venv django_venv
source django_venv/bin/activate
pip install -r requirement.txt