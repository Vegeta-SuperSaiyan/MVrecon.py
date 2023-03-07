#!/usr/bin/env python

import sys
import os

if len(sys.argv) < 2:
    print('''
------------------- HOW TO USE --------------------
----------- sudo ./MVrecon.py <IP/URL> ------------
''')
    sys.exit()

print('\nDeleting Previous Scan Logs....\n')

if os.path.exists('nmap_version_port_script_scan.csv'):
    os.remove('nmap_version_port_script_scan.csv')

if os.path.exists('nmap_http-enum_scan.csv'):
    os.remove('nmap_http-enum_scan.csv')

if os.path.exists('nmap_ssl-enum_scan.csv'):
    os.remove('nmap_ssl-enum_scan.csv')

if os.path.exists('mozilla_observatory_cli.csv'):
    os.remove('mozilla_observatory_cli.csv')

if os.path.exists('sslscan.csv'):
    os.remove('sslscan.csv')

if os.path.exists('dig.csv'):
    os.remove('dig.csv')

if os.path.exists('nslookup.csv'):
    os.remove('nslookup.csv')

if os.path.exists('traceroute.csv'):
    os.remove('traceroute.csv')

if os.path.exists('nikto.csv'):
    os.remove('nikto.csv')

if os.path.exists('ScanResults.csv'):
    os.remove('ScanResults.csv')

with open('nmap_version_port_script_scan.csv', 'w') as f:
    f.write('-NMAP version, port and script scan-\n\n')
    f.flush()

print('Running NMAP version, port and script scan...\n')

os.system('nmap -Pn -sV -sC {} | tee -a nmap_version_port_script_scan.csv'.format(sys.argv[1]))

with open('nmap_http-enum_scan.csv', 'w') as f:
    f.write('\nNMAP http-enum_scan\n\n')
    f.flush()

print('Running NMAP http enum scan...\n')

os.system('nmap -sV --script=http-enum {} -p 80,443 | tee -a nmap_http-enum_scan.csv'.format(sys.argv[1]))

with open('ScanResults.csv', 'w') as f:
    f.write('\nRESULTS\n\n')
    f.flush()

print('Combining scan results...\n')

os.system('cat nmap_version_port_script_scan.csv nmap_http-enum_scan.csv > ScanResults.csv')

print('\nAll scans completed successfully! Scan Results are saved in ScanResults.csv\n')
