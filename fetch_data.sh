#!/bin/bash

echo "Starting Foxpro Data Fetch..."

source .env
YEAR=$1
MONTH=$2
DAY=$3

TEMP_PRG=$(mktemp).prg
cat > "$TEMP_PRG" << EOF
SET DEFAULT TO $DATA_PATH

TODAY = DATE()
OSDT = DATE($YEAR, $MONTH, $DAY)
OEDT = TODAY - 1
OUTPUT_PATH = '$OUTPUT_PATH'
DATA_PATH = '$DATA_PATH'

KEYBOARD '{ENTER}{TAB}$USERNAME{ENTER}$PASSWORD{ENTER}'

DO pp.prg
DO dosummary.prg
QUIT
EOF

"$VFP_PATH" "$TEMP_PRG"
rm -f "$TEMP_PRG"
