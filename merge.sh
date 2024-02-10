#!/bin/bash

# Check if there are at least two arguments
if [ $# -lt 2 ]; then
    echo "Usage: $0 <output_file> <input_file1> [<input_file2> ...]"
    exit 1
fi

# Output file name is the first argument
output_file=$1

# Shift the arguments to skip the output file name
shift

# Concatenate input files into the output file
cat "$@" > "$output_file"

echo "Merged files into $output_file"
