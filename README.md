# Port Scanner

This Python script is a versatile port scanner that provides three different interfaces for scanning a range of ports on a target IP address. It includes a command-line interface, a web-based UI, and a desktop app. The script utilizes the `socket` library and the `scapy` module for port scanning and banner grabbing. It can be used to scan localhost `127.0. 0.1` of the same machine or any other IP address.

## Usage

Note: Use virtual environment to install the requirements to avoid conflicts with other projects.

```bash
python3 -m venv venv
source venv/bin/activate
```

```bash
pip install -r requirements.txt
```
The port scanner can be used in three different ways:

### Command-Line Interface (CLI)

To use the command-line version, follow the steps below:

1. Open a terminal or command prompt.
2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Navigate to the directory where the `main.py` file is located.
4. Run the script with the following command:

    ```bash
    python3 main.py <target_ip> <start_port> <end_port>
    ```

    Replace `<target_ip>` with the IP address you want to scan, `<start_port>` with the starting port number, and `<end_port>` with the ending port number.
5. The script will scan the specified range of ports on the target IP address and display the results.
![Command-Line Interface](/images/commandline.png)

### Web-Based UI

To use the web-based UI version, follow the steps below:

1. Open a terminal or command prompt.
2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Navigate to the directory where the `app_web.py` file is located.
4. Run the script with the following command:

    ```bash
    python3 app_web.py
    ```

5. Open a web browser and access the application at [http://127.0.0.1:5000/](http://127.0.0.1:5000/).
6. Enter the target IP address, start port, and end port in the provided form and click the "Scan" button.
7. The results will be displayed on the web page.

![Web UI](/images/web_ui.png)

### Desktop App

To use the desktop app version, follow the steps below:

1. Open a terminal or command prompt.
2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Navigate to the directory where the `app_desktop.py` file is located.
4. Run the script with the following command:

    ```bash
    python3 app_desktop.py
    ```

5. The desktop app will open, providing a user-friendly interface for entering the target IP address, start port, and end port.
6. Click the "Scan" button to initiate the scanning process.
7. The results will be displayed within the desktop app.

![Desktop App](/images/desktop_app.png)

## How It Works

The port scanner uses a `scan_ports` function to iterate through the range of ports specified. For each port, it attempts to establish a TCP connection using the `socket` library. If the connection is successful, it performs a banner grab by sending a request to the open port and receiving the response. The banner, if available, is then displayed.

The `grab_banner` function is responsible for establishing a TCP connection to the target IP address and port and retrieving the banner information.

## Why Use a Port Scanner?

Port scanning is a useful technique for network administrators and security professionals to identify open ports on a target system. It can help in identifying potential vulnerabilities or misconfigurations that could be exploited by attackers. By knowing which ports are open, administrators can take appropriate measures to secure their systems.

Please note that port scanning should only be performed on systems that you have permission to scan. Unauthorized port scanning is considered unethical and may be illegal.
