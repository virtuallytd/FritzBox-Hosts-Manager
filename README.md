
# Fritz!Box Hosts List Script

This script connects to a Fritz!Box router and retrieves a list of all connected devices, displaying their hostnames, IP addresses, and MAC addresses. It allows sorting of the output and the option to save the data to a file.

## Features

- Retrieve connected device information from Fritz!Box.
- Sort the list by IP address, hostname, or MAC address.
- Output the information to the console or save it to a file.

## Requirements

- Python 3
- `fritzconnection` Python library
- `tabulate` Python library

To install the required libraries, run:

```bash
pip install fritzconnection tabulate
```

## Configuration

Before running the script, update the following variables in the script with your Fritz!Box credentials:

- `FRITZ_IP`: IP address of your Fritz!Box.
- `FRITZ_USER`: Username for Fritz!Box access.
- `FRITZ_PASSWORD`: Password for Fritz!Box access.

## Usage

Run the script with Python 3. Command-line arguments can be used for sorting and output options:

- `-s/--sort [ip|hostname|mac]`: Sort the list by IP address, hostname, or MAC address.
- `-o/--output [file_path]`: Write the output to a specified file.

Example:

```bash
python fritz_hosts_list.py -s ip -o ./output.txt
```

This command sorts the devices by IP address and saves the output to `output.txt`.

## Note

- Ensure that your Fritz!Box credentials are correctly set in the script.
- The script must be run in an environment where `fritzconnection` and `tabulate` are installed.
- The output and behavior might vary depending on the Fritz!Box model and firmware version.
