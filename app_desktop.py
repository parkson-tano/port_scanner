import tkinter as tk
from tkinter import ttk
from tkinter import Label, Entry, Button, Text, Scrollbar
from threading import Thread
import socket

class PortScannerGUI:
    def __init__(self, master):
        self.master = master
        master.title("Port Scanner")

        # Set a consistent color style
        ttk.Style().configure('TButton', padding=6, relief="flat", background="#3498db", foreground="white")
        ttk.Style().map('TButton', foreground=[('pressed', 'white'), ('active', 'white')])

        # Create labels and entry widgets
        self.create_labels_and_entries()

        # Create Text widget for displaying results
        self.result_text = Text(master, height=10, width=50, wrap=tk.WORD)
        self.result_text.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        # Create a Progressbar
        self.progress_bar = ttk.Progressbar(
            master,
            orient='horizontal',
            mode='indeterminate',
            length=200,
            style="TProgressbar"
        )
        self.progress_bar.grid(row=4, column=0, columnspan=2, pady=10)

        # Create a Scan button
        self.scan_button = ttk.Button(master, text="Scan", command=self.start_scan, style="TButton")
        self.scan_button.grid(row=5, column=0, columnspan=2, pady=10)

    def create_labels_and_entries(self):
        entries = [
            ("Target IP:", 0, 0),
            ("Start Port:", 1, 0),
            ("End Port:", 2, 0),
        ]

        for label_text, row, column in entries:
            Label(self.master, text=label_text, font=("Helvetica", 12)).grid(row=row, column=column, padx=10, pady=10)

        self.target_ip_entry = Entry(self.master, font=("Helvetica", 12))
        self.target_ip_entry.grid(row=0, column=1, padx=10, pady=10)

        self.start_port_entry = Entry(self.master, font=("Helvetica", 12))
        self.start_port_entry.grid(row=1, column=1, padx=10, pady=10)

        self.end_port_entry = Entry(self.master, font=("Helvetica", 12))
        self.end_port_entry.grid(row=2, column=1, padx=10, pady=10)

    def start_scan(self):
        # Get input values from the entry widgets
        target_ip = self.target_ip_entry.get()
        start_port = int(self.start_port_entry.get())
        end_port = int(self.end_port_entry.get())

        # Clear previous results
        self.result_text.delete(1.0, tk.END)

        # Set the progress bar to indeterminate mode and start it
        self.progress_bar.start()

        # Perform port scanning in a separate thread
        scan_thread = Thread(target=self.scan_ports, args=(target_ip, start_port, end_port))
        scan_thread.start()

    def scan_ports(self, target_ip, start_port, end_port):
        for port in range(start_port, end_port + 1):
            # Check if the port is open
            if self.is_port_open(target_ip, port):
                banner = self.grab_banner(target_ip, port)
                self.display_result(f"Port {port} is open\nBanner: {banner}")

        # Stop the progress bar when scanning is complete
        self.progress_bar.stop()

        # Notify the user that scanning is finished
        self.display_result("\nScanning finished!")

    def is_port_open(self, target_ip, port):
        # Use socket to check if the port is open
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target_ip, port))
        sock.close()
        return result == 0

    def grab_banner(self, target_ip, port, timeout=2):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(timeout)
                sock.connect((target_ip, port))
                banner = sock.recv(1024).decode('utf-8').strip()
                return banner
        except (socket.timeout, socket.error):
            return "Banner not available"

    def display_result(self, result):
        # Display the result in the Text widget
        self.result_text.insert(tk.END, result + "\n")
        self.result_text.see(tk.END)

def main():
    root = tk.Tk()
    app = PortScannerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
