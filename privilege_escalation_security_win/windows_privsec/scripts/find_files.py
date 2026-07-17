#!/usr/bin/python3
import os

def find_files(targets, base_dir=""):
    targets_found = list()

    print(f'Starting search for {targets} in {base_dir}...\n')

    for root, dirs, files in os.walk(base_dir):
        # If we found all unique targets, stop scanning completely
        if set(targets_found) == set(targets):
            break

        for dir in dirs:
            if dir in targets:
                path = os.path.join(root, dir)
                print(f'[+] Found folder: {dir} in {path}')
                targets_found.append(dir)

        for file in files:
            if file in targets:
                path = os.path.join(root, file)
                print(f'[+] Found file: {file} in {path}')
                targets_found.append(file)

    print("\n[!] File search is complete")

    # Create a list of missed targets
    missed_targets = set(targets) - set(targets_found)

    if missed_targets:
        print(f' [-] Target(s) not found: {list(missed_targets)}')
        print(f'\n[?] Are you sure you typed them correctly?')


if __name__ == '__main__':
    target_files = ["back"]
    find_files(targets=target_files, base_dir="C:\\")

    input("\nPress Enter to exit...")
