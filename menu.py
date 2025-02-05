import socket
import random

def scan_ports(target, ports):
    print(f"Scanning {target} on ports {ports}")
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is open")
        sock.close()

def generate_ip():
    ip = ".".join(str(random.randint(1, 255)) for _ in range(4))
    print(f"Generated IP: {ip}")

print("Choose an option:")
print("1 - Scan Ports")
print("2 - Generate IP")
choice = input("> ")

if choice == "1":
    target_ip = input("Enter target IP: ")
    ports = input("Enter ports (comma separated): ")
    port_list = [int(p) for p in ports.split(",")]
    scan_ports(target_ip, port_list)
elif choice == "2":
    generate_ip()
else:
    print("Invalid choice.")
