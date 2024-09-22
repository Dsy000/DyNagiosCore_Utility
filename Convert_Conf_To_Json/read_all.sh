#!/bin/bash

find objects/ -name "*.cfg" -type f  -exec python3 ConfToJson.py {} \;
