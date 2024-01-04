import sys
import socket
from scapy.all import *

def scan_ports(target, start_port, end_port):
    open_ports = {}
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0 and port not in open_ports:
            banner = grab_banner(target, port)
            open_ports[port] = banner
            print(f"Port {port} is open: {banner}")
        sock.close()
    return open_ports

def grab_banner(target, port, timeout=2):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            sock.connect((target, port))
            banner = sock.recv(1024).decode('utf-8').strip()
            return banner
    except (socket.timeout, socket.error):
        return "Banner not available"

def main():
    if len(sys.argv) != 4:
        print("Usage: python scanner.py <target_ip> <start_port> <end_port>")
        sys.exit(1)

    target_ip = sys.argv[1]
    start_port = int(sys.argv[2])
    end_port = int(sys.argv[3])

    print(f"Scanning ports {start_port} to {end_port} on {target_ip}")

    open_ports = scan_ports(target_ip, start_port, end_port)

    if not open_ports:
        print("No open ports found.")
    else:
        print("Banner grabbing results:")
        for port, banner in open_ports.items():
            print(f"Port {port}: {banner}")

if __name__ == "__main__":
    main()


