# Port Scanner

This Python script is a simple port scanner that allows you to scan a range of ports on a target IP address. It utilizes the `socket` library and the `scapy` module to perform the port scanning and banner grabbing.

## Usage

To use the port scanner, follow the steps below:

1. Open a terminal or command prompt.
2. Navigate to the directory where the `index.py` file is located.
3. Run the script with the following command:

    ```
    python index.py <target_ip> <start_port> <end_port>
    ```

    Replace `<target_ip>` with the IP address you want to scan, `<start_port>` with the starting port number, and `<end_port>` with the ending port number.

4. The script will scan the specified range of ports on the target IP address and display the results.

## How It Works

The port scanner uses a `scan_ports` function to iterate through the range of ports specified. For each port, it attempts to establish a TCP connection using the `socket` library. If the connection is successful, it performs a banner grab by sending a request to the open port and receiving the response. The banner, if available, is then displayed.

The `grab_banner` function is responsible for establishing a TCP connection to the target IP address and port, and retrieving the banner information.

## Why Use a Port Scanner?

Port scanning is a useful technique for network administrators and security professionals to identify open ports on a target system. It can help in identifying potential vulnerabilities or misconfigurations that could be exploited by attackers. By knowing which ports are open, administrators can take appropriate measures to secure their systems.

Please note that port scanning should only be performed on systems that you have permission to scan. Unauthorized port scanning is considered unethical and may be illegal.
