#!/usr/bin/sh

pip -V
python3 -m pip install -t local_lib git+https://github.com/jaraco/path --log log_file.log -I -U
python3 my_program.py