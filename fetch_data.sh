#!/bin/bash

echo "Starting Foxpro Data Fetch..."

VFP_PATH="C:\\Program Files (x86)\\Microsoft Visual FoxPro 9\\vfp9.exe"
USERNAME="your_username"
PASSWORD="your_password"

TEMP_PRG=$(mktemp).prg
cat > "$TEMP_PRG" << EOF
SET DEFAULT TO "D:\BIS"

KEYBOARD '{ENTER}{TAB}$USERNAME{ENTER}$PASSWORD{ENTER}'

DO pp.prg
DO dosummary.prg
QUIT
EOF

"$VFP_PATH" "$TEMP_PRG"
rm -f "$TEMP_PRG"
