import nmap

def scan_site(target):
    # Initialize the Nmap PortScanner
    nm = nmap.PortScanner()

    try:
        # Perform a simple ping scan to determine if the host is up
        nm.scan(hosts=target, arguments='-sn')

        # Check if the host is up
        if nm.all_hosts():
            print(f"Host {target} is up. Starting port scan...\n")
            
            # Perform a more detailed scan to enumerate open ports and services
            nm.scan(hosts=target, arguments='-p 1-65535 -sV')

            # Print the scan results
            for host in nm.all_hosts():
                print(f"Host: {host}")
                for proto in nm[host].all_protocols():
                    print(f"Protocol: {proto}")
                    ports = nm[host][proto].keys()
                    for port in ports:
                        print(f"Port: {port}\tState: {nm[host][proto][port]['state']}\tService: {nm[host][proto][port]['name']}")

        else:
            print(f"Host {target} is not reachable.")

    except nmap.PortScannerError as e:
        print(f"Nmap error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    target_site = input("Enter the target site or IP address: ")
    scan_site(target_site)
