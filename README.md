## Key Updates

### 1. **Reverse DNS Lookup**
The script can now resolve an IP address back to its corresponding domain name or hostname.

- **Functionality**: Queries the DNS server for a PTR record to determine the hostname associated with an IP.
- **Usage**: Automatically invoked when the script resolves an IP address.
- **Output**:
  - If a hostname exists: Displays the associated hostname.
  - If no record exists: Outputs `No reverse DNS record found`.

**Example**:
```text
Enter a website URL (e.g., example.com): 8.8.8.8
[+] Reverse DNS: dns.google
```

---

### 2. **Port Scanning**
Checks for open ports on the resolved IP address.

- **Ports Scanned**: Common ports like 80 (HTTP), 443 (HTTPS), 22 (SSH), etc.
- **Functionality**: Attempts to establish a connection to each port. If successful, the port is marked as open.
- **Customization**: Add or modify the list of ports in the `ports` tuple.

**Example**:
```text
Scanning common ports...
[+] Open Ports: 80, 443
```

---

### 3. **IP Geolocation**
Fetches geolocation data for the resolved IP address using the [ipinfo.io API](https://ipinfo.io).

- **Data Retrieved**:
  - City
  - Region
  - Country
  - Organization (e.g., ISP or company)
  - GPS coordinates (latitude and longitude)
- **API**: Uses a free-tier API for basic geolocation information.

**Example**:
```text
Fetching geolocation information...
[+] City: Los Angeles
[+] Region: California
[+] Country: US
[+] Organization: AS15133 Edgecast Inc.
[+] Location: 34.0522,-118.2437
```

---

## How to Use
1. Clone or pull the repository containing the script.
2. Install all required module:
   ```bash
   pip install requests
   ```
3. Run the script:
   ```bash
   python script_name.py
   ```
4. Enter a website URL or IP address when prompted.
