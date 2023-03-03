#!/bin/bash
MYPATH=$1

echo "USAGE: count_island.sh [input_file_path]"

# check input parameters
if [ -z "$MYPATH" ]; then
    echo "Error: Input file path is not set. Use .txt file"
    exit
fi

python3 main.py --input_file_path=$MYPATH
