#!/usr/bin/env bash

# Did this instead of directly grabbing env variables incase
# script wants to be run independently of docker.
python3 main.py -p "$PACKAGENAME" -e "$PACKAGEEXPORTS" -o "output/$PACKAGENAME.md" -m "$MODELNAME"