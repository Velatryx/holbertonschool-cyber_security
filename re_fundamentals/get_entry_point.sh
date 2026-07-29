#!/bin/bash

# Source the messages.sh script from the current directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
if [[ -f "$SCRIPT_DIR/messages.sh" ]]; then
    source "$SCRIPT_DIR/messages.sh"
else
    echo "Error: messages.sh not found."
    exit 1
fi

target_file="$1"

# 1. Check if argument was provided, file exists, and is a valid ELF file
if [[ -z "$target_file" || ! -f "$target_file" ]] || ! readelf -h "$target_file" &>/dev/null; then
    echo "The specified file either does not exist, or is not an ELF file."
    exit 1
fi

# 2. Extract specific variables required by display_elf_header_info
file_name="$target_file"

# Extract Magic Number (strip leading whitespace)
magic_number=$(readelf -h "$target_file" | awk -F':' '/Magic:/ {print $2}' | xargs)

# Extract Class (e.g., ELF32 or ELF64)
class=$(readelf -h "$target_file" | awk -F':' '/Class:/ {print $2}' | xargs)

# Extract Byte Order (Data field in readelf, e.g., 2's complement, little endian)
byte_order=$(readelf -h "$target_file" | awk -F':' '/Data:/ {print $2}' | xargs)

# Extract Entry Point Address
entry_point_address=$(readelf -h "$target_file" | awk -F':' '/Entry point address:/ {print $2}' | xargs -0)

# 3. Call the function from messages.sh
display_elf_header_info
