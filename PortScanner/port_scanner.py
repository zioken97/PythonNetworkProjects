import socket
import threading

target = input("Enter target IP address: ")
ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3389]  # Common ports
lock = threading.Lock()

def scan_port(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            with lock:
                print(f"[+] Port {port} is OPEN")

def main():
    threads = []
    print(f"Scanning target: {target}")
    for port in ports:
        t = threading.Thread(target=scan_port, args=(port,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print("Scan complete.")

if __name__ == "__main__":
    main()
