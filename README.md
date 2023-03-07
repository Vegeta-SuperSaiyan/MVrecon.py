# MVrecon.py

Network Reconnaissance Script
This is a Python script for conducting network reconnaissance on a target IP or URL. The script runs several scans and outputs the results to separate CSV files, which are then combined into a single results file.

Usage
To use the script, run it from the command line with the target IP or URL as the first argument:
python3 network_recon.py <IP/URL>

The script will run the following scans:
-NMAP version, port, and script scan
-NMAP http-enum scan
-NMAP SSL enumeration scan
-Mozilla Observatory CLI scan
-SSLScan
-DIG
-NSLOOKUP
-Traceroute
-Nikto

The results of each scan will be output to a separate CSV file, and the final results will be combined into a single file named ScanResults.csv.

Installation
To use the script, you will need to have Python 3 installed on your system. You can download Python 3 from the official website.

You will also need to install the following packages:
-nmap
-observatory-cli
-sslscan
-traceroute
-nikto

You can install these packages using your system's package manager or using 'pip'. For example, to install nmap and observatory-cli, you can run the following commands:

sudo apt-get install nmap
sudo pip install observatory-cli
