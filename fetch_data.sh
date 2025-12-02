#!/bin/bash

echo "Starting Foxpro Data Fetch..."

source .env
DAYS=$1

TEMP_PRG=$(mktemp).prg
cat > "$TEMP_PRG" << EOF
SET DEFAULT TO $DATA_PATH

TODAY = DATE()
OSDT = DATE(2025, 11, 01)
OEDT = TODAY - $DAYS
OUTPUT_PATH = '$OUTPUT_PATH'
DATA_PATH = '$DATA_PATH'

KEYBOARD '{ENTER}{TAB}$USERNAME{ENTER}$PASSWORD{ENTER}'

DO pp.prg
DO dosummary.prg
QUIT
EOF

"$VFP_PATH" "$TEMP_PRG"
rm -f "$TEMP_PRG"
