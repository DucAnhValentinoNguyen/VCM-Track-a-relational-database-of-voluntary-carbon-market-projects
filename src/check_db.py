import sqlite3
import pandas as pd

def check_database_integrity():
    database_name = 'netzero_data.db'
    conn = sqlite3.connect(database_name)
    
    print("="*50)
    print("NET ZERO LAB: DATABASE INTEGRITY CHECK")
    print("="*50)

    # 1. Check Table: market_news (Market Sentiment)
    print("\n[STREAM 2] Voluntary Carbon Market News (RSS Feed)")
    try:
        df_news = pd.read_sql("SELECT date, category, title FROM market_news", conn)
        print(f" Success: {len(df_news)} recent articles indexed.")
        print(df_news.head(3))
    except Exception as e:
        print(f" Error reading market_news: {e}")

    # 2. Check Table: carbon_pricing (Economic Trends)
    print("\n[STREAM 3] Global Carbon Price Index (Yahoo Finance - KRBN)")
    try:
        df_price = pd.read_sql("SELECT Date, Open, Close, Volume FROM carbon_pricing", conn)
        print(f" Success: {len(df_price)} days of price data available.")
        print(df_price.tail(3)) # Show the most recent prices
    except Exception as e:
        print(f" Error reading carbon_pricing: {e}")

    conn.close()
    print("\n" + "="*50)
    print("CHECK COMPLETE")

if __name__ == "__main__":
    check_database_integrity()