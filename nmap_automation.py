import os
import subprocess
import datetime

def run_nmap_scan(scan_type, target, output_file):
    nmap_command = f"nmap {scan_type} {target} -oN {output_file}"
    subprocess.run(nmap_command, shell=True)

def main():
    target = input("Enter the target IP or hostname: ")
    output_dir = "nmap_scans"
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    
    scans = [
        ("-sV -sC", "version_default"),
        ("-p- -sV", "all_ports_version"),
        ("-sU -p123,161,500", "udp_common"),
        ("-sS -sV -O", "syn_version_os"),
        ("--script vuln", "vulnerability"),
        ("-A", "aggressive"),
    ]
    
    for scan_type, scan_name in scans:
        output_file = f"{output_dir}/{timestamp}_{scan_name}.txt"
        print(f"Running {scan_name} scan...")
        run_nmap_scan(scan_type, target, output_file)
        print(f"Scan completed. Results saved to {output_file}")
    
    print("All scans completed.")

if __name__ == "__main__":
    main()