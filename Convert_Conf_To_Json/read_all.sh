#!/bin/bash

find objects/ -name "*.cfg" -type f  -exec python3 final_nagio_conf_jsone_convert.py {} \;