"""
Lightweight Streamlit dashboard to explore Trader Performance vs Market Sentiment results.
Run: streamlit run dashboard.py
"""
import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="Trader vs Sentiment", layout="wide")

PROJECT_ROOT = Path(__file__).resolve().parent
DATA_DIR = PROJECT_ROOT / "data"
OUTPUT_DIR = PROJECT_ROOT / "output"

st.title("Trader Performance vs Market Sentiment")
st.caption("Hyperliquid trader behavior and Bitcoin Fear/Greed sentiment")

# Load outputs if available
daily_path = OUTPUT_DIR / "daily_metrics_by_sentiment.csv"
if daily_path.exists():
    day_agg = pd.read_csv(daily_path)
    day_agg["date"] = pd.to_datetime(day_agg["date"])
    st.subheader("Daily metrics by sentiment")
    st.dataframe(day_agg.head(100), use_container_width=True)
    sent = day_agg["sentiment"].unique()
    if len(sent) >= 2:
        c1, c2 = st.columns(2)
        with c1:
            st.metric("Mean PnL (Fear)", day_agg[day_agg["sentiment"] == "Fear"]["mean_pnl"].mean().round(2))
        with c2:
            st.metric("Mean PnL (Greed)", day_agg[day_agg["sentiment"] == "Greed"]["mean_pnl"].mean().round(2))
else:
    st.info("Run the analysis notebook first to generate output files. Place data in the `data/` folder and run all cells in `analysis.ipynb`.")

# Show saved charts if present
for name, fname in [
    ("Performance by sentiment", "performance_by_sentiment.png"),
    ("Behavior by sentiment", "behavior_by_sentiment.png"),
    ("Sentiment × Leverage heatmap", "insight_sentiment_leverage_heatmap.png"),
]:
    p = OUTPUT_DIR / fname
    if p.exists():
        st.subheader(name)
        st.image(str(p), use_container_width=True)

st.sidebar.markdown("### How to run")
st.sidebar.markdown("1. Put sentiment and trader CSVs in `data/`")
st.sidebar.markdown("2. Run `analysis.ipynb`")
st.sidebar.markdown("3. Refresh this dashboard")
