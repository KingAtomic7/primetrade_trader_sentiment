# Trader Performance vs Market Sentiment

Data Science Intern (Round-0) assignment: analyze how Bitcoin Fear/Greed sentiment relates to trader behavior and performance on Hyperliquid.

## Setup

1. **Clone or download** this repo and open a terminal in the project folder.

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   venv\Scripts\activate   # Windows
   # source venv/bin/activate  # macOS/Linux
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Get the datasets:**
   - **Option A:** Run the download script (uses `gdown` for Google Drive):
     ```bash
     python download_data.py
     ```
   - **Option B:** Download manually and place in the `data/` folder:
     - [Bitcoin Market Sentiment (Fear/Greed)](https://drive.google.com/file/d/1PgQC0tO8XN-wqkNyghWc_-mnrYv_nhSf/view?usp=sharing) → save as `data/bitcoin_sentiment.csv`
     - [Hyperliquid Historical Trader Data](https://drive.google.com/file/d/1IAfLZwu6rJzyWKgBToqwSmmVYU6VbjVs/view?usp=sharing) → save as `data/hyperliquid_trader_data.csv`

## How to run

- **Notebook (recommended):** Open `analysis.ipynb` in Jupyter or VS Code and run all cells. This performs:
  - **Part A:** Data preparation (load, document, align, create metrics)
  - **Part B:** Analysis (Fear vs Greed performance, behavior, segments, insights)
  - **Part C:** Actionable strategy recommendations
  - **Bonus:** Predictive model (next-day PnL bucket), trader clustering, and chart exports



## Project structure

```
primetrade_trader_sentiment/
├── analysis.ipynb          # Main analysis (run this)
├── config.py                # Paths and config
├── data_loader.py           # Load sentiment + trader data
├── download_data.py         # Download datasets from Google Drive
├── dashboard.py             # Streamlit dashboard (bonus)
├── requirements.txt
├── README.md
├── SUMMARY.md               # Methodology, insights, recommendations
├── data/                    # Put CSV files here
└── output/                  # Charts and tables (created by notebook)
```

## Outputs

- `output/daily_metrics_by_sentiment.csv` — daily aggregates by sentiment
- `output/performance_by_sentiment.png` — performance boxplots
- `output/behavior_by_sentiment.png` — behavior by sentiment
- `output/insight_*.png` — insight charts

## Summary

See **SUMMARY.md** for a one-page write-up of methodology, insights, and strategy recommendations.
