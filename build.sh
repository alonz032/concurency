#!/bin/bash

# Utility to find and run/compile files regardless of which folder they are in
TARGET=$1

if [ -z "$TARGET" ]; then
    echo "Usage: ./build.sh {filename.py | filename.cpp}"
    exit 1
fi

# 1. Handle Python Files
if [[ "$TARGET" == *.py ]]; then
    FILE_PATH=$(find . -name "$TARGET" -not -path "*/.*")
    if [ -z "$FILE_PATH" ]; then
        echo "Error: Could not find $TARGET"
        exit 1
    fi
    echo "Running Python script: $FILE_PATH"
    python3 "$FILE_PATH"

# 2. Handle C++ Files (Compile and Run)
elif [[ "$TARGET" == *.cpp ]]; then
    FILE_PATH=$(find . -name "$TARGET" -not -path "*/.*")
    if [ -z "$FILE_PATH" ]; then
        echo "Error: Could not find $TARGET"
        exit 1
    fi
    
    # Strip extension for binary name
    BIN_NAME="${FILE_PATH%.cpp}.bin"
    
    echo "Compiling C++: $FILE_PATH -> $BIN_NAME"
    g++ -std=c++20 -pthread "$FILE_PATH" -o "$BIN_NAME"
    
    if [ $? -eq 0 ]; then
        echo "Running: $BIN_NAME"
        ./"$BIN_NAME"
    else
        echo "Compilation failed."
        exit 1
    fi

else
    echo "Unsupported file type. Please provide a .py or .cpp file."
    exit 1
fi
