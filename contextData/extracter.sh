#!/bin/bash
echo $1
sed -r '/^\s*$/d;/^\[.*\]/d;s/^\s*//;/^\..*/d' $1 >  input