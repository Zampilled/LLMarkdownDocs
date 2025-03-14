#!/usr/bin/env bash
##################
##   Config     ##
##################

PACKAGE_NAME="@rescui/use-glow-hover"
PACKAGE_EXPORTS="useGlowHover GlowHoverHookOptions glowHoverEffect GlowHoverOptions"
MODEL_NAME="llama3.1:8b"
TYPESCRIPT=true

########################

cd code || return

echo "Pulling Ollama Model"
ollama pull "$MODEL_NAME"

echo "Adding NPM Package"
npm i "$PACKAGE_NAME"

echo "Running Main Script"
python3 main.py -p "$PACKAGE_NAME" -e "$PACKAGE_EXPORTS" -o "output/output.md" -m "$MODEL_NAME" -t $TYPESCRIPT