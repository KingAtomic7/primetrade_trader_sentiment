"""
Download datasets from Google Drive if not present locally.
Run: python download_data.py
"""
import gdown
from config import DATA_DIR, GDRIVE_SENTIMENT_ID, GDRIVE_TRADER_ID

def main():
    DATA_DIR.mkdir(exist_ok=True)
    sentiment_path = DATA_DIR / "bitcoin_sentiment.csv"
    trader_path = DATA_DIR / "hyperliquid_trader_data.csv"

    if not sentiment_path.exists():
        print("Downloading Bitcoin Market Sentiment...")
        gdown.download(
            id=GDRIVE_SENTIMENT_ID,
            output=str(sentiment_path),
            quiet=False,
        )
    else:
        print("Sentiment file already exists.")

    if not trader_path.exists():
        print("Downloading Hyperliquid Trader Data...")
        gdown.download(
            id=GDRIVE_TRADER_ID,
            output=str(trader_path),
            quiet=False,
        )
    else:
        print("Trader data file already exists.")

    print("Done. Check the 'data' folder.")

if __name__ == "__main__":
    main()
