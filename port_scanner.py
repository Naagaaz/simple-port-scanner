import socket

target = input("Enter target IP (example: 127.0.0.1): ")

print("Scanning started...\n")

for port in range(1, 101):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)

    if s.connect_ex((target, port)) == 0:
        print(f"Port {port} is OPEN")

    s.close()

print("\nScanning finished.")
