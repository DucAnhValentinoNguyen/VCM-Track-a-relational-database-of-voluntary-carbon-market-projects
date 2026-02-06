import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def plot_carbon_trends():
    # 1. Path Handling (Parallel folders)
    # Get the directory where THIS script is located (src/)
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Define paths relative to the project root
    db_path = os.path.join(base_dir, '..', 'data', 'netzero_data.db')
    output_path = os.path.join(base_dir, '..', 'outputs', 'carbon_price_trend.png')
    
    # Ensure outputs folder exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # 2. Connect to SQL
    if not os.path.exists(db_path):
        print(f" Error: Database not found at {db_path}")
        return

    conn = sqlite3.connect(db_path)
    
    try:
        # 3. Query & Parse
        df = pd.read_sql("SELECT Date, Close FROM carbon_pricing", conn)
        df['Date'] = pd.to_datetime(df['Date'], utc=True)
        df = df.sort_values('Date')
        
        # 4. Visualization
        plt.figure(figsize=(12, 6))
        sns.set_style("whitegrid")
        plt.plot(df['Date'], df['Close'], color='#2ecc71', linewidth=2)
        
        plt.title('Global Carbon Price Evolution (Innovation Proxy)', fontsize=15)
        plt.xlabel('Year', fontsize=12)
        plt.ylabel('Price (USD)', fontsize=12)
        plt.fill_between(df['Date'], df['Close'], color='#2ecc71', alpha=0.1)
        
        plt.tight_layout()
        plt.savefig(output_path)
        print(f" Chart saved to: {output_path}")
        
    except Exception as e:
        print(f" Error: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    plot_carbon_trends()