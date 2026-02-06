import yfinance as yf
import sqlite3
import pandas as pd

def scrape_carbon_prices():
    # KRBN is the KraneShares Global Carbon Strategy ETF
    ticker_symbol = "KRBN"
    
    print(f"Fetching Carbon Price History for {ticker_symbol} using yfinance...")
    
    try:
        # 1. Download data (period='max' gets all historical data)
        ticker = yf.Ticker(ticker_symbol)
        df = ticker.history(period="max")
        
        if df.empty:
            print(" No data found. Yahoo might be blocking the request.")
            return

        # 2. Flatten the index (Date is usually the index in yfinance)
        df.reset_index(inplace=True)
        
        # Clean column names for SQL (remove spaces)
        df.columns = [str(c).replace(' ', '_') for c in df.columns]

        print(f" Successfully fetched {len(df)} days of carbon price data.")
        
        # 3. Save to SQL
        conn = sqlite3.connect('../data/netzero_data.db')
        df.to_sql('carbon_pricing', conn, if_exists='replace', index=False)
        conn.close()
        
        print(" Data saved to table 'carbon_pricing' in netzero_data.db")
        print(df[['Date', 'Close']].tail()) # Show most recent prices
        
    except Exception as e:
        print(f" An error occurred: {e}")

if __name__ == "__main__":
    scrape_carbon_prices()