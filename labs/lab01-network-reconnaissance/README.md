# Lab 1: Network Reconnaissance and Scanning

## Objective
Learn fundamental network reconnaissance techniques and tools to identify network assets, services, and potential security vulnerabilities in a controlled environment.

## Prerequisites
- Basic understanding of TCP/IP networking
- Familiarity with command line interfaces
- Virtual machine with Kali Linux or similar security distribution
- Access to test network environment

## Lab Environment
- Target Network: 192.168.1.0/24 (or as provided by instructor)
- Testing VM: Kali Linux with network access
- **IMPORTANT**: Only scan networks you own or have explicit permission to test

## Learning Outcomes
By the end of this lab, you will be able to:
1. Perform network discovery using various techniques
2. Identify live hosts on a network
3. Enumerate services and versions on target systems
4. Analyze scan results for security assessment
5. Document findings in a professional format

## Tools Required
- Nmap (Network Mapper)
- Ping
- Netdiscover
- Masscan (optional)

## Lab Instructions

### Phase 1: Network Discovery

#### Step 1: Basic Network Connectivity
```bash
# Test basic connectivity to the network
ping -c 4 192.168.1.1
ping -c 4 192.168.1.254
```

#### Step 2: Host Discovery
```bash
# Discover live hosts using ICMP ping sweep
nmap -sn 192.168.1.0/24

# Alternative: ARP discovery (for local network)
nmap -PR 192.168.1.0/24

# Using netdiscover for ARP-based discovery
netdiscover -r 192.168.1.0/24
```

### Phase 2: Port Scanning

#### Step 3: Basic Port Scanning
```bash
# TCP SYN scan of common ports
nmap -sS 192.168.1.100

# Scan specific ports
nmap -p 22,80,443,3389 192.168.1.100

# Scan port ranges
nmap -p 1-1000 192.168.1.100
```

#### Step 4: Service Detection
```bash
# Service version detection
nmap -sV 192.168.1.100

# OS detection
nmap -O 192.168.1.100

# Comprehensive scan
nmap -A 192.168.1.100
```

### Phase 3: Advanced Scanning Techniques

#### Step 5: Stealth Scanning
```bash
# TCP FIN scan
nmap -sF 192.168.1.100

# TCP NULL scan
nmap -sN 192.168.1.100

# Timing options for stealth
nmap -T2 192.168.1.100
```

#### Step 6: UDP Scanning
```bash
# UDP port scan (slower but important)
nmap -sU --top-ports 100 192.168.1.100
```

## Deliverables

### Report Requirements
Create a lab report including:

1. **Executive Summary** (1 paragraph)
   - Brief overview of the reconnaissance performed
   - Key findings and recommendations

2. **Methodology** (1-2 paragraphs)
   - Tools and techniques used
   - Scanning approach and rationale

3. **Findings** (detailed section)
   - Live hosts discovered
   - Open ports and services identified
   - Operating system information
   - Potential vulnerabilities noted

4. **Analysis** (1-2 paragraphs)
   - Security implications of findings
   - Risk assessment of discovered services

5. **Recommendations** (bullet points)
   - Security improvements suggested
   - Further testing recommendations

### Technical Documentation
- Command outputs (screenshots or text)
- Nmap scan results
- Network diagram (if applicable)

## Assessment Criteria
- **Technical Accuracy** (40%): Correct tool usage and valid results
- **Analysis Quality** (30%): Depth of security analysis and insights
- **Documentation** (20%): Clear, professional report formatting
- **Methodology** (10%): Logical approach and proper techniques

## Safety and Legal Considerations
- **NEVER** scan networks you don't own or lack permission to test
- Use only designated lab networks
- Follow responsible disclosure for any real vulnerabilities found
- Respect system resources and avoid disruptive scanning

## Additional Resources
- Nmap Official Documentation: https://nmap.org/docs.html
- Network reconnaissance best practices
- Legal and ethical considerations in security testing

## Troubleshooting
**Common Issues:**
- No hosts found: Check network connectivity and subnet
- Permission denied: Ensure proper privileges for raw socket access
- Slow scans: Adjust timing parameters or reduce scan scope

**Solutions:**
- Use `sudo` for privileged operations
- Verify target network is accessible
- Check firewall settings on scanning system