import socket
import threading
from datetime import datetime

# Define the target (127.0.0.1 is your own local computer for safe testing)
TARGET = "scanme.nmap.org"


# Define the port range you want to scan (e.g., standard web/system ports)
PORTS_TO_SCAN = [21, 22, 23, 25, 53, 80, 110, 135, 139, 443, 445, 3389]

print("-" * 50)
print(f"Scanning Target: {TARGET}")
print(f"Scanning started at: {str(datetime.now())}")
print("-" * 50)

def scan_port(port):
    try:
        # Create a socket object
        # AF_INET = IPv4, SOCK_STREAM = TCP Connection
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Set a timeout so the script doesn't hang forever on closed ports
        s.settimeout(1.0)
        
        # Attempt to connect to the target IP and port
        result = s.connect_ex((TARGET, port))
        
        # connect_ex returns 0 if the connection was successful
        if result == 0:
            print(f"[+] Port {port} is OPEN")
            
        s.close()
        
    except Exception as e:
        pass

# Use threading to scan multiple ports simultaneously (much faster)
threads = []
for port in PORTS_TO_SCAN:
    t = threading.Thread(target=scan_port, args=(port,))
    threads.append(t)
    t.start()

# Wait for all threads to finish before exiting the script
for t in threads:
    t.join()

print("\nScanning complete.")
