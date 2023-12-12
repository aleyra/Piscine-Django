#!/usr/bin/sh

# to call: `source set_env.sh`

python3 -m venv ENV_django
source ENV_django/bin/activate
pip install -r requirements.txt