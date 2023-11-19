## Port scanning

### IPSEC's scan
mkdir nmap && nmap -sC -sV -oA nmap/scan 10.10.11.230

### Fast scan
nmap -F IP

### Agressive scan and timing template 4 (aggressive)
nmap -A -T4 IP

### Scan all ports (or -p-)
nmap -p '*' IP

### Detect service/daemon versions
nmap -sV IP

### Scan for vulnerabilities
nmap -Pn --script vuln IP

### without ping
nmap -Pn IP

### script scan using a default set of scripts
nmap -sC IP

### good general aggressive call
nmap -p- -A -sV -sC -Pn -T4 IP

### check tls an ssl on https port
nmap -p 443 --script ssl-enum-ciphers host

### it's always a good thing to turn on -v (verbose) to see what is happening

### to speed up the first scan --min-rate=10000
