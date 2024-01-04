import sys
import socket
from flask import Flask, render_template, request
from scapy.all import *

app = Flask(__name__)

def scan_ports(target, start_port, end_port):
    open_ports = {}
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0 and port not in open_ports:
            banner = grab_banner(target, port)
            open_ports[port] = banner
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

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        target_ip = request.form['target_ip']
        start_port = int(request.form['start_port'])
        end_port = int(request.form['end_port'])

        open_ports = scan_ports(target_ip, start_port, end_port)

        if not open_ports:
            result = "No open ports found."
        else:
            result = "Banner grabbing results:\n"
            for port, banner in open_ports.items():
                result += f"Port {port}: {banner}\n"

        return render_template('index.html', result=result)

    return render_template('index.html', result=None)

if __name__ == '__main__':
    app.run(debug=True)
