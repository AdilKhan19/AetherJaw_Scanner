import urllib.request
import re
from datetime import datetime

class PentestEngine:
    def __init__(self, target_url):
        # Clean up the URL format if the user forgot to add http/https
        if not target_url.startswith("http://") and not target_url.startswith("https://"):
            target_url = "https://" + target_url
        self.target_url = target_url
        self.findings = []

    def run_scout_agent(self):
        """AGENT 1: THE SCOUT - Inspects website settings safely without doing damage."""
        print(f"\n[+] [Agent 1: Scout] Launching Passive Audit on {self.target_url}...")
        try:
            # Create a safe web request configuration
            req = urllib.request.Request(
                self.target_url, 
                headers={'User-Agent': 'AetherJaw Safe Security Auditor/1.0'}
            )
            
            # Contact the server and read its responses
            with urllib.request.urlopen(req, timeout=7) as response:
                headers = response.info()
                html_content = response.read().decode('utf-8', errors='ignore')
            
            # 1. Look for missing secure configurations in the web headers
            if 'X-Frame-Options' not in headers:
                self.log_finding("Scout_Agent", "Security Headers", "Missing_Security_Layer", 
                                 "X-Frame-Options header is missing. The site could be vulnerable to Clickjacking.", "Low")
                
            if 'Content-Security-Policy' not in headers:
                self.log_finding("Scout_Agent", "Security Headers", "Missing_Security_Layer", 
                                 "Content-Security-Policy (CSP) is not enforced. Vulnerable to script injection.", "Medium")

            if 'Strict-Transport-Security' not in headers:
                self.log_finding("Scout_Agent", "Encryption Headers", "Missing_SSL_Enforcement", 
                                 "Strict-Transport-Security (HSTS) is missing. Traffic could be sniffed.", "High")

            # 2. Safely scan the webpage layout structure for input vulnerabilities
            forms = re.findall(r'<form\s+.*?>', html_content, re.IGNORECASE)
            for form in forms:
                self.log_finding("Scout_Agent", "Web Forms", "Data_Input_Detected", 
                                 f"Data entry form located: {form}. Needs strict validation checks.", "Info")
                
            print(f"[✓] [Scout] Finished scanning. Found {len(self.findings)} configuration spots.")
            return True
        except Exception as e:
            print(f"[x] [Scout Error] Cannot reach the target website safely: {e}")
            return False

    def run_analyst_agent(self):
        """AGENT 2: THE ANALYST - Organizes the risks into a prioritized breakdown."""
        print("\n[+] [Agent 2: Analyst] Sorting risks into prioritization queue...")
        if not self.findings:
            print(" |-- [Notice] No major security configuration gaps found.")
            return
            
        for finding in self.findings:
            print(f"  |-- [{finding['severity']}] Matrix Spot at {finding['component']}: {finding['description']}")

    def log_finding(self, agent_name, component, error_type, description, severity):
        """The Shared Memory Bus - Keeps track of everything found."""
        self.findings.append({
            "agent": agent_name,
            "component": component,
            "type": error_type,
            "description": description,
            "severity": severity,
            "timestamp": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        })