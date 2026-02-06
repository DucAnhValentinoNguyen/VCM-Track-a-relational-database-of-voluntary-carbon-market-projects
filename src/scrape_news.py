import requests
import sqlite3
import xml.etree.ElementTree as ET
import pandas as pd

def scrape_carbon_news():
    # Target: Google News RSS Feed for "Carbon Credits"
    # This is reliable, real-time, and doesn't block simple scripts.
    url = "https://news.google.com/rss/search?q=carbon+credits+market&hl=en-US&gl=US&ceid=US:en"
    
    print(f"Fetching news from {url}...")
    response = requests.get(url)
    
    # Parse XML (Common in data research)
    root = ET.fromstring(response.content)
    
    news_items = []
    
    # Iterate through <item> tags in the XML
    for item in root.findall('./channel/item'):
        title = item.find('title').text
        pub_date = item.find('pubDate').text
        link = item.find('link').text
        
        # Simple Sentiment/Category Check (The "Research" part)
        category = "General"
        if "price" in title.lower() or "soar" in title.lower() or "drop" in title.lower():
            category = "Market Price"
        elif "fraud" in title.lower() or "scam" in title.lower():
            category = "Integrity Risk"
            
        news_items.append({
            "title": title,
            "date": pub_date,
            "category": category,
            "link": link
        })
    
    # Convert to DataFrame
    df = pd.DataFrame(news_items)
    
    # SAVE TO SQL
    conn = sqlite3.connect('../data/netzero_data.db')
    df.to_sql('market_news', conn, if_exists='replace', index=False)
    conn.close()
    
    print(f" Success! Scraped {len(df)} recent news articles.")
    print(df[['date', 'category', 'title']].head())

if __name__ == "__main__":
    scrape_carbon_news()