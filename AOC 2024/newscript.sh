#!/bin/bash

for i in $(seq -w 1 24); do
    folder="${i}Day"       # Folder name: 01Day, 02Day, ..., 24Day
    file="${folder}/${i}Day.md"  # File name: 01Day/01Day.md, etc.
    
    mkdir -p "$folder"     # Create the folder
    echo -e "# Day ${i} Notes\n\nThis is the content for Day ${i}." > "$file"  # Create the file with content
done

