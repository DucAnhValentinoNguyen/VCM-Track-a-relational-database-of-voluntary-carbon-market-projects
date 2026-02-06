import os
import subprocess

def run_pipeline():
    print("--- Starting VCM-Track Research Pipeline ---")
    
    # 1. Ensure the data directory exists
    if not os.path.exists('../data'):
        os.makedirs('../data')
        print("Created '../data' directory.")

    # 2. Run the scrapers in order
    scripts = ['scrape_news.py', 'scrape_yahoo.py', 'visualisation.py']
    
    for script in scripts:
        print(f"\nExecuting: {script}...")
        try:
            # Run each script as a subprocess
            subprocess.run(['python', script], check=True)
        except subprocess.CalledProcessError as e:
            print(f" Error in {script}: {e}")
            return

    print("\n--- Pipeline Complete! Check 'outputs/' for results. ---")

if __name__ == "__main__":
    run_pipeline()