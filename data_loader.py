"""
Load and validate datasets. Handles CSV/Excel and common column name variants.
"""
import pandas as pd
from pathlib import Path
from config import DATA_DIR, SENTIMENT_FILE, TRADER_DATA_FILE


def _find_file(base_name: str, exts=("csv", "xlsx", "parquet")):
    for ext in exts:
        p = DATA_DIR / f"{base_name}.{ext}"
        if p.exists():
            return p
    return DATA_DIR / f"{base_name}.csv"


def load_sentiment():
    path = _find_file("bitcoin_sentiment")
    if not path.exists():
        raise FileNotFoundError(
            f"Sentiment file not found. Place it in {DATA_DIR} as bitcoin_sentiment.csv (or .xlsx). "
            "Download from: https://drive.google.com/file/d/1PgQC0tO8XN-wqkNyghWc_-mnrYv_nhSf/view"
        )
    if path.suffix == ".csv":
        df = pd.read_csv(path)
    else:
        df = pd.read_excel(path)
    # Normalize column names
    df.columns = [c.strip() for c in df.columns]
    col_map = {c: c for c in df.columns}
    for c in df.columns:
        if "date" in c.lower():
            col_map[c] = "Date"
        if "class" in c.lower() or "sentiment" in c.lower():
            col_map[c] = "Classification"
    df = df.rename(columns=col_map)
    if "Date" not in df.columns:
        df["Date"] = pd.to_datetime(df.iloc[:, 0])
    if "Classification" not in df.columns:
        df["Classification"] = df.iloc[:, 1]
    df["Date"] = pd.to_datetime(df["Date"]).dt.normalize()
    df["Classification"] = df["Classification"].astype(str).str.strip()
    return df


def load_trader_data():
    path = _find_file("hyperliquid_trader_data")
    if not path.exists():
        raise FileNotFoundError(
            f"Trader data not found. Place it in {DATA_DIR} as hyperliquid_trader_data.csv (or .xlsx). "
            "Download from: https://drive.google.com/file/d/1IAfLZwu6rJzyWKgBToqwSmmVYU6VbjVs/view"
        )
    if path.suffix == ".csv":
        df = pd.read_csv(path, low_memory=False)
    elif path.suffix == ".parquet":
        df = pd.read_parquet(path)
    else:
        df = pd.read_excel(path)
    df.columns = [str(c).strip() for c in df.columns]
    # Normalize time column
    time_col = next((c for c in df.columns if "time" in c.lower()), None)
    if time_col:
        df["time"] = pd.to_datetime(df[time_col], errors="coerce")
    return df
