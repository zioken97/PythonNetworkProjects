import subprocess
import ipaddress
import platform
import threading

subnet = input("Enter subnet (e.g., 192.168.1.0/24): ")
network = ipaddress.ip_network(subnet, strict=False)

param = "-n" if platform.system().lower() == "windows" else "-c"
lock = threading.Lock()

def ping(ip):
    result = subprocess.run(["ping", param, "1", str(ip)], stdout=subprocess.DEVNULL)
    if result.returncode == 0:
        with lock:
            print(f"[+] Host {ip} is UP")
            with open("output/alive_hosts.txt", "a") as f:
                f.write(f"{ip}\n")

def main():
    open("output/alive_hosts.txt", "w").close()
    threads = []
    print(f"Scanning subnet: {subnet}")
    for ip in network.hosts():
        t = threading.Thread(target=ping, args=(ip,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print("Scan complete. See output/alive_hosts.txt for results.")

if __name__ == "__main__":
    main()
