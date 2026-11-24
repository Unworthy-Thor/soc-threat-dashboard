import re
from collections import defaultdict

# Patterns that indicate threats
THREAT_PATTERNS = {
    "SQL Injection": [
        r"union\s+select", r"or\s+'1'='1", r"drop\s+table",
        r"insert\s+into", r"select\s+\*", r"--\s*$", r"1=1"
    ],
    "XSS Attack": [
        r"<script>", r"</script>", r"javascript:", r"onerror=",
        r"onload=", r"alert\(", r"document\.cookie"
    ],
    "Directory Traversal": [
        r"\.\./", r"\.\.\\", r"/etc/passwd", r"/etc/shadow",
        r"boot\.ini", r"/proc/self"
    ],
    "Brute Force": [],  # handled separately by counting 401s
    "Admin Panel Scan": [
        r"/admin", r"/phpmyadmin", r"/wp-admin",
        r"/administrator", r"/admin/config", r"/manager"
    ]
}

def analyze_log(filepath):
    threats = []
    ip_401_count = defaultdict(int)
    total_lines = 0

    with open(filepath, "r") as f:
        lines = f.readlines()

    total_lines = len(lines)

    for line in lines:
        line_lower = line.lower()
        ip = line.split(" ")[0]

        # Count 401 responses per IP for brute force detection
        if '"' in line and "401" in line:
            ip_401_count[ip] += 1

        # Check each threat pattern
        for threat_type, patterns in THREAT_PATTERNS.items():
            if threat_type == "Brute Force":
                continue
            for pattern in patterns:
                if re.search(pattern, line_lower):
                    threats.append({
                        "type": threat_type,
                        "ip": ip,
                        "detail": line.strip(),
                        "severity": get_severity(threat_type)
                    })
                    break

    # Add brute force threats
    for ip, count in ip_401_count.items():
        if count >= 3:
            threats.append({
                "type": "Brute Force",
                "ip": ip,
                "detail": f"{count} failed login attempts detected from {ip}",
                "severity": "HIGH"
            })

    # Summary
    summary = {
        "total_lines": total_lines,
        "total_threats": len(threats),
        "threats": threats,
        "threat_counts": count_threats(threats),
        "suspicious_ips": list(set([t["ip"] for t in threats]))
    }

    return summary

def get_severity(threat_type):
    severity_map = {
        "SQL Injection": "CRITICAL",
        "XSS Attack": "HIGH",
        "Directory Traversal": "HIGH",
        "Brute Force": "HIGH",
        "Admin Panel Scan": "MEDIUM"
    }
    return severity_map.get(threat_type, "LOW")

def count_threats(threats):
    counts = defaultdict(int)
    for threat in threats:
        counts[threat["type"]] += 1
    return dict(counts)