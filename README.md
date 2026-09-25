# Amazon-Style Web Scraper

A Python web scraping and data analytics project that collects book
product information from Books to Scrape, cleans the data, performs
price analysis, and tracks historical price changes.

## Features

- Scrapes 50 pages of product data
- Extracts product title, price, availability, rating, and URL
- Adds scraping date
- Cleans scraped data using Pandas
- Saves product data to CSV
- Performs price and rating analysis
- Maintains historical price data
- Detects price increases and decreases

## Tech Stack

- Python
- Requests
- BeautifulSoup
- Pandas
- CSV
- Git & GitHub

## Project Structure

```text
amazon-web-scraper/
│
├── main.py
│
├── scraper/
│   ├── scraper.py
│   └── cleaner.py
│
├── analysis/
│   └── analysis.py
│
├── storage/
│   └── storage.py
│
├── data/
├── requirements.txt
└── README.md