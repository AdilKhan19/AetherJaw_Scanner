import os

def create_text_report(target_url, findings):
    """AGENT 5: THE AUDITOR - Generates a clean security report card file."""
    report_filename = "Security_Audit_Report.txt"
    print(f"\n[+] [Agent 5: Auditor] Generating clean text report document: {report_filename}...")
    
    try:
        with open(report_filename, "w", encoding="utf-8") as f:
            f.write("====================================================\n")
            f.write("      AETHERJAW MULTI-AGENT SECURITY AUDIT REPORT   \n")
            f.write("====================================================\n")
            f.write(f"Generated On : {os.getenv('CURRENT_TIME', 'Live Session')}\n")
            f.write(f"Target URL   : {target_url}\n")
            f.write(f"Total Risks  : {len(findings)}\n")
            f.write("====================================================\n\n")
            
            if not findings:
                f.write("[✓] SUCCESS: No critical security gaps detected on this domain.\n")
            else:
                f.write("DETAILED SECURITY FINDINGS:\n")
                f.write("---------------------------\n")
                for index, item in enumerate(findings, 1):
                    f.write(f"{index}. SEVERITY LEVEL: [{item['severity']}]\n")
                    f.write(f"   Identified By : {item['agent']}\n")
                    f.write(f"   Target System : {item['component']}\n")
                    f.write(f"   Risk Details  : {item['description']}\n")
                    f.write(f"   Logged Time   : {item['timestamp']}\n")
                    f.write("   -------------------------------------------------\n")
                    
            f.write("\n=== End of Report (AetherJaw Systems Open-Source Secure Auditor) ===\n")
            
        print(f"[✓] [Auditor] Security report compiled perfectly! Open '{report_filename}' to read it.")
    except Exception as e:
        print(f"[x] [Reporting Error] Failed to generate report file: {e}")