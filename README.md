# PythonNetworkProjects

A collection of Python-based tools designed to demonstrate practical scripting in a networking environment. Each folder contains a self-contained script or utility with its own purpose and logic.

NetworkSweeper

Multi-threaded subnet scanner that pings all hosts in a given CIDR range and logs alive IPs.
- Language: Python
- Dependencies: `subprocess`, `threading`, `ipaddress`, `platform`
- Output: `output/alive_hosts.txt`

Port Scanner

Description: A threaded TCP port scanner that checks a set of common ports against a target IP.

Ports Scanned: 21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3389

*****LEGAL NOTICE*****
Use these tools only on networks and systems you own or have explicit permission to test. Unauthorized scanning may be illegal.


