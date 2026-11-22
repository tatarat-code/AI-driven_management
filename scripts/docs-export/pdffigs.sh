#!/bin/bash
# usage: pdffigs.sh <saved-result-file> <volNN>  … PDF を復号し、図を public/images/guidebook/<volNN>-figN.png に置く
set -e
cd /home/claude/export
python3 decode.py "$1" pdf/$2.pdf
python3 -c "
import json,sys
" 
rm -rf /tmp/figs_$2 && mkdir -p /tmp/figs_$2
pdfimages -png pdf/$2.pdf /tmp/figs_$2/f
out=/home/claude/AI-driven_management/public/images/guidebook; mkdir -p $out
i=0; for f in $(ls /tmp/figs_$2/*.png | sort); do i=$((i+1)); cp $f $out/$2-fig$i.png; done
echo "$2: $i images"
