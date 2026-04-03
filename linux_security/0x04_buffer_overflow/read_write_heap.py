#!/usr/bin/python3
"""
Locates and replaces a string in the heap of a running process.
Usage: ./read_write_heap.py PID SEARCH_STRING REPLACE_STRING
"""

import sys
import os

def print_error_and_exit(msg):
    print(msg, file=sys.stderr)
    sys.exit(1)

def read_write_heap():
    # 1. Validation of arguments
    if len(sys.argv) != 4:
        print_error_and_exit("Usage: {} pid search_string replace_string".format(sys.argv[0]))

    pid = sys.argv[1]
    search_str = sys.argv[2].encode('ascii')
    replace_str = sys.argv[3].encode('ascii')

    if not pid.isdigit():
        print_error_and_exit("Error: PID must be a number.")

    maps_path = "/proc/{}/maps".format(pid)
    mem_path = "/proc/{}/mem".format(pid)

    # 2. Find the heap range in /proc/[pid]/maps
    heap_start = None
    heap_end = None

    try:
        with open(maps_path, 'r') as f_maps:
            for line in f_maps:
                if "[heap]" in line:
                    # Line format: 555e646e0000-555e64701000 rw-p 00000000 00:00 0 [heap]
                    parts = line.split()
                    addr_range = parts[0].split('-')
                    heap_start = int(addr_range[0], 16)
                    heap_end = int(addr_range[1], 16)
                    print("[*] Found heap at {:x} - {:x}".format(heap_start, heap_end))
                    break
    except Exception as e:
        print_error_and_exit("Error opening maps: {}".format(e))

    if heap_start is None:
        print_error_and_exit("Error: Heap not found for this process.")

    # 3. Read/Write to /proc/[pid]/mem
    try:
        with open(mem_path, 'rb+') as f_mem:
            # Move pointer to start of heap
            f_mem.seek(heap_start)
            heap_data = f_mem.read(heap_end - heap_start)

            # Locate the string
            offset = heap_data.find(search_str)
            if offset == -1:
                print_error_and_exit("Error: String '{}' not found in heap.".format(sys.argv[2]))

            print("[*] Found '{}' at offset {:x}".format(sys.argv[2], offset))

            # Move pointer to the exact location of the string and write
            f_mem.seek(heap_start + offset)
            f_mem.write(replace_str + b'\0') # Adding null terminator for C compatibility
            print("[*] Successfully replaced with '{}'".format(sys.argv[3]))

    except PermissionError:
        print_error_and_exit("Error: Run as sudo to access another process's memory.")
    except Exception as e:
        print_error_and_exit("Error accessing memory: {}".format(e))

if __name__ == "__main__":
    read_write_heap()
