# VCM-Track: Voluntary Carbon Market Data Pipeline

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![SQL](https://img.shields.io/badge/SQL-SQLite-green)
![Status](https://img.shields.io/badge/Status-Research%20Prototype-orange)

### 📋 Project Overview
**VCM-Track** is an automated data pipeline designed to aggregate and analyze economic indicators for the Voluntary Carbon Market (VCM).

The goal of this project is to demonstrate a reproducible workflow for **Green Innovation Research**. It automates the acquisition of financial time-series data (Carbon ETF prices) and unstructured market sentiment (news feeds), normalizing them into a relational SQL database for downstream econometric analysis.

This repository serves as a portfolio project demonstrating competencies in **Data Acquisition**, **SQL Maintenance**, and **Statistical Visualisation**, aligned with the research focus of the **Net Zero Lab**.

---

### 📂 Repository Structure
The project follows a modular research architecture to ensure separation of concerns between source code, raw data, and analytical outputs.

```text
VCM-Track/
├── src/                # Modular Python scripts for acquisition & analysis
│   ├── scrape_news.py  # ETL for Google News RSS (Market Sentiment)
│   ├── scrape_yahoo.py # ETL for Yahoo Finance (KRBN Price Index)
│   ├── visualisation.py# Generates trend analysis charts
│   └── main.py         # Runs the full pipeline
├── data/               # Persistent Data Storage
│   └── netzero_data.db # Relational SQLite database
├── outputs/           
│   └── carbon_price_trend.png
├── setup_env.sh        # Environment automation script
└── requirements.txt    # Project dependencies
```
