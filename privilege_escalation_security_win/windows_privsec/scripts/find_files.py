#!/usr/bin/python3

# Import os for using useful os classes
import os

# Lets first find the files passed in fun main.
# Also let's pass two arguments to this function to determine targets, and starting directory. Add 2 '\\' instead of 1, because it escapes the next character.
def find_files(targets, base_dir=""):

    # Create an empty list to add target files
    targets_found = list()
    # os.walk gives the result in 3 pieces, the starting root dir, found folders and subfolders, and files inside:
    print(f'Starting search for {targets}...\n')
    for root, dirs, files in os.walk(base_dir):
        # Now we iterate 1 file through all files to see if we hit a target
        for file in files:
            if file in targets:
                # we show a complete path of the file
                path = os.path.join(root, file)
                print(f'[+] Found file: {file} in {path}')
                # Now let's append all the found files to a list we created
                targets_found.append(file)
    print("\n[!] File search is complete")

    # Create a list of missed targets
    missed_targets = set(targets) - set(targets_found)

    # Print the missing targets if missed_targets list is not empty.
    if missed_targets:
        print(f' [-] Target(s) not found: {list(missed_targets)}')
        print(f'\n[?] Are you sure you typed them correctly?')

# Now, let's pass the arguments, like the target files we look for.
if __name__ == '__main__':
    target_files = ["sysprep.inf", "autounattend.xml", "Unattend.xml"]
    find_files(targets=target_files, base_dir="C:\\")
