#!/usr/bin/sh

# MEMO : This script must be called using :
# source my_scipt.sh

python3 -m venv django_venv
source django_venv/bin/activate
pip install -r requirement.txt