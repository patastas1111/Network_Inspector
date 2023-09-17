"""
Network Inspector
by Charlie Chavez

"""



import argparse
import os
from data_olt import guangda, vsol, richerlink
from checkconnection import icmp


os.system("clear")
data_search = input("Search: ").strip()
areas_input = input("Enter comma-separated areas to search (e.g. R12, R11) or type 'all' to search all areas: ").strip()

filename = "iplist.txt"
devices = []

if areas_input == "all":
    try:
        with open(filename, "r") as file:
            for line in file:
                parts = line.strip().split("::")
                if len(parts) != 3:
                    print(f"Skiping line {line.strip()}")
                    continue
                ip_address = parts[0].strip()
                device_name = parts[1].strip()
                area = parts[2].strip()
                devices.append((ip_address, device_name, area))

    except FileNotFoundError:
        print(f"File not found: {filename}")
else:
    areas = areas_input.split(",")
    try:
        with open(filename, "r") as file:
            for line in file:
                parts = line.strip().split("::")
                if len(parts) != 3:
                    print(f"Skiping line {line.strip()}")
                    continue
                ip_address = parts[0].strip()
                device_name = parts[1].strip()
                area = parts[2].strip()
                if area in areas:
                    devices.append((ip_address, device_name, area))

    except FileNotFoundError:
        print(f"File not found: {filename}")

for device in devices:
    ip_address, device_name, area = device
    print()
    print(f"Scanning {device_name} -> \033[1;36;40m {ip_address} \033[1;37;40m -> {area}")
    send_icmp = icmp(ip_address)
    result_icmp = send_icmp.icmpcheck()
    if "guangda" == device_name:
        guangda(ip_address).search(data_search)
    elif "vsol" == device_name:
        vsol(ip_address).search(data_search)
    elif "richerlink" == device_name:
        richerlink(ip_address).search(data_search)
    else:
        print(f"\033[1;31;40m {device_name} not exist in the script \033[1;37;40m")
