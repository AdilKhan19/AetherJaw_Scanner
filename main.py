from crypto_engine import PentestEngine
from report_generator import create_text_report

def start_application():
    print("==========================================================")
    print("      LAUNCHING AETHERJAW SECURITY MULTI-AGENT MESH       ")
    print("==========================================================")
    print("[Safe Mode Active]: No harmful payloads will be transmitted.\n")
    
    # Ask the user what site they want to safely inspect
    user_target = input("Enter the website address to scan (e.g., example.com): ").strip()
    
    if not user_target:
        print("[x] Error: Website address cannot be blank. Exiting.")
        return

    # Initialize the core engine pipeline
    orchestrator = PentestEngine(user_target)
    
    # 1. Fire Agent 1 to crawl headers safely
    success = orchestrator.run_scout_agent()
    
    if success:
        # 2. Fire Agent 2 to analyze the risks found
        orchestrator.run_analyst_agent()
        
        # 3. Fire Agent 5 to construct the audit document
        create_text_report(orchestrator.target_url, orchestrator.findings)
        
        print("\n==========================================================")
        print("  APPLICATION WORKLOAD COMPLETE. PORTFOLIO DEMO READY.    ")
        print("==========================================================")
    else:
        print("\n[x] Audit aborted due to connection failure.")

if __name__ == "__main__":
    start_application()