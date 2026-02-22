"""
Configuration and paths for Trader Performance vs Market Sentiment project.
"""
from pathlib import Path

# Project paths
PROJECT_ROOT = Path(__file__).resolve().parent
DATA_DIR = PROJECT_ROOT / "data"
OUTPUT_DIR = PROJECT_ROOT / "output"

# Ensure directories exist
DATA_DIR.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)

# Dataset filenames (user places downloaded files here)
SENTIMENT_FILE = DATA_DIR / "bitcoin_sentiment.csv"  # or .xlsx
TRADER_DATA_FILE = DATA_DIR / "hyperliquid_trader_data.csv"  # or .parquet, .xlsx

# Google Drive file IDs for optional download
GDRIVE_SENTIMENT_ID = "1PgQC0tO8XN-wqkNyghWc_-mnrYv_nhSf"
GDRIVE_TRADER_ID = "1IAfLZwu6rJzyWKgBToqwSmmVYU6VbjVs"
