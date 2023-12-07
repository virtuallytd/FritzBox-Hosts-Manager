import argparse
from fritzconnection.lib.fritzhosts import FritzHosts
from tabulate import tabulate
import sys

# Set your Fritz!Box credentials here.
FRITZ_IP = '192.168.1.1'  # Replace with your Fritz!Box IP address
FRITZ_USER = 'admin'      # Replace with your Fritz!Box username
FRITZ_PASSWORD = 'password'  # Replace with your Fritz!Box password

def get_hosts_info():
    # Establishes a connection to the Fritz!Box.
    print("Connecting to Fritz!Box...")
    fritz_hosts = FritzHosts(address=FRITZ_IP, user=FRITZ_USER, password=FRITZ_PASSWORD)

    # Retrieve information about connected hosts.
    print("Gathering host data...")
    hosts_info = []
    for index in range(fritz_hosts.host_numbers):
        host = fritz_hosts.get_generic_host_entry(index)
        hosts_info.append([host['NewHostName'], host['NewIPAddress'], host['NewMACAddress']])
        # Print the progress on the same line.
        sys.stdout.write(f"\rRetrieved data for host {index + 1} of {fritz_hosts.host_numbers}")
        sys.stdout.flush()
    print()  # Move to the next line after the loop
    return hosts_info

def sort_hosts_info(hosts_info, sort_key):
    # Sort the hosts information based on the given key
    sort_options = {'ip': 1, 'hostname': 0, 'mac': 2}
    if sort_key in sort_options:
        return sorted(hosts_info, key=lambda x: x[sort_options[sort_key]])
    return hosts_info

# Set up argument parsing for command line options.
parser = argparse.ArgumentParser(description="List and sort Fritz!Box hosts.")
parser.add_argument("-s", "--sort", choices=['ip', 'hostname', 'mac'], help="Sort by: 'ip', 'hostname', or 'mac'")
parser.add_argument("-o", "--output", help="Output to a file (e.g., -o ./out.txt)")
args = parser.parse_args()

# Retrieve and optionally sort hosts information.
hosts_info = get_hosts_info()
if args.sort:
    hosts_info = sort_hosts_info(hosts_info, args.sort)

print("\nSorting and displaying data...")
# Handle output: either print to console or write to a file.
if args.output:
    with open(args.output, 'w') as file:
        file.write(tabulate(hosts_info, headers=['Hostname', 'IP', 'MAC']))
    print(f"Data written to {args.output}")
else:
    print(tabulate(hosts_info, headers=['Hostname', 'IP', 'MAC']))

print("Operation completed.")