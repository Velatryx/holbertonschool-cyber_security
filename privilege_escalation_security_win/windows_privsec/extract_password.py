#!/usr/bin/python3

# Import os for using useful os classes
import os
import re  # Import the regular expressions module
import base64

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



def find_files(targets, base_dir=""):
    
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
                
                targets_found.append(file)
            
                extracted_val = extract_password(path)
                if extracted_val:
                    print(f'[*] Extracted Password: {extracted_val}')
                    try:
                        # FIXED: Calling base64 directly and using utf-8 to be safe
                        ascii_string = base64.b64decode(extracted_val).decode('utf-8')
                        print(f'[+] Decoded Password: {ascii_string}')
                    except Exception as decode_error:
                        print(f'[-] Failed to decode base64 value: {decode_error}')
                else:
                    print(f'[-] No matching password tags found in this file.')

    print("\n[!] File search is complete")

    # Create a list of missed targets
    missed_targets = set(targets) - set(targets_found)

    # Print the missing targets if missed_targets list is not empty.
    if missed_targets:
        print(f' [-] Target(s) not found: {list(missed_targets)}')
        print(f'\n[?] Are you sure you typed them correctly?')



if __name__ == '__main__':
    target_files = ["sysprep.inf", "autounattend.xml", "Unattend.xml"]
    find_files(targets=target_files, base_dir="C:\\")
