#!/usr/bin/python3
"""
Finds and replaces a string in the heap of a running process.
"""
import sys


def usage():
    """Print usage message and exit with status code 1."""
    print("Usage: ./read_write_heap.py pid search_string replace_string")
    sys.exit(1)


def read_write_heap(pid, search_string, replace_string):
    """Find and replace a string in the heap of a process."""
    try:
        pid = int(pid)
    except ValueError:
        usage()

    maps_path = "/proc/{}/maps".format(pid)
    mem_path = "/proc/{}/mem".format(pid)

    try:
        # 1. Identify the heap location
        heap_start, heap_end = None, None
        with open(maps_path, "r") as maps_file:
            for line in maps_file:
                if "[heap]" in line:
                    # Parse the address range
                    addr_range = line.split()[0].split("-")
                    heap_start = int(addr_range[0], 16)
                    heap_end = int(addr_range[1], 16)
                    break

        if heap_start is None:
            sys.exit(1)

        # 2. Search and overwrite in the memory file
        with open(mem_path, "r+b") as mem_file:
            mem_file.seek(heap_start)
            heap_data = mem_file.read(heap_end - heap_start)

            s_bytes = search_string.encode()
            r_bytes = replace_string.encode()

            offset = heap_data.find(s_bytes)
            if offset == -1:
                sys.exit(1)

            # Seek to exact string location and overwrite with padding
            mem_file.seek(heap_start + offset)
            mem_file.write(r_bytes.ljust(len(s_bytes), b'\x00'))

    except (PermissionError, FileNotFoundError):
        sys.exit(1)
    except Exception:
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        usage()

    read_write_heap(sys.argv[1], sys.argv[2], sys.argv[3])
