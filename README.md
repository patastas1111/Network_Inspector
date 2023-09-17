# Network_Inspector

NetScan Pro is a powerful network management tool designed to streamline the process of locating clients, identifying OLT (Optical Line Terminal) placements, and efficiently assigning PON (Passive Optical Network) connections.

**Compatibility:**
- This code is compatible with Linux operating systems only.
- It only supports VSOL and Guangda.
- It supports Richerlink devices, specifically the Alpha version.

### Need to Install Library for Python
- configparser
  
## Getting Started
1. To start the Network Inspector, run the `start.py` script.
2. Input the MAC address you want to find.
3. Input the area you want to search, following this format: `(dataconnect1,dataconnect2)` after the comma, without spaces.
4. Wait for the code to find the device. If the device is not connected, it will search for existing records.
