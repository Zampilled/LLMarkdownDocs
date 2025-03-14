#!/usr/bin/env bash
##################
##   Config     ##
##################

PACKAGE_NAME="@rescui/use-glow-hover"
PACKAGE_EXPORTS="useGlowHover GlowHoverHookOptions glowHoverEffect GlowHoverOptions"
MODEL_NAME="deepseek-r1:70b"
TYPESCRIPT=true

########################

cd code || return

echo "Pulling Ollama Model"
ollama pull "$MODEL_NAME"

npm i "$PACKAGE_NAME"

# Did this instead of directly grabbing env variables incase
# script wants to be run independently of docker.
python3 main.py -p "$PACKAGE_NAME" -e "$PACKAGE_EXPORTS" -o "output/output.md" -m "$MODEL_NAME" -t $TYPESCRIPT