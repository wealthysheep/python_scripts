import socket

def scan_ports(target, port):
    """Attempts to connect to a target on a specific port."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Use settimeout on the socket, not globally
        result = sock.connect_ex((target, port))
        sock.close()

        if result == 0:
            print(f"[+] Port {port} is open")
          
    except Exception as e:
        print(f"Error scanning port {port}: {e}")

def main():
    target = input("What is your target IP Address: ")
    for port in range(1, 65536):  # Scan from port 1 to 65535
        scan_ports(target, port)

if __name__ == "__main__":
    main()
