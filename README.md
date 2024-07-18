1. It prompts you to enter the target IP or hostname.
2. It creates a directory called "nmap_scans" to store the scan results.
3. It performs six different types of Nmap scans:
   - Version and default script scan
   - All ports version scan
   - UDP scan on common ports
   - SYN scan with version detection and OS fingerprinting
   - Vulnerability scan using Nmap scripts
   - Aggressive scan

4. Each scan result is saved to a separate file with a timestamp and scan type in the filename.

To use this script:

1. Save it as a .py file (e.g., `nmap_automation.py`).
2. Ensure you have Python and Nmap installed on your system.
3. Run the script with administrative privileges (as Nmap requires root/admin access for many scan types).

Remember to use this script responsibly and only on networks and systems you have permission to scan.

