# Trader Performance vs Market Sentiment — Summary (≤1 page)

## Methodology

- **Data:** Bitcoin Fear/Greed sentiment (date, classification) and Hyperliquid historical trader data (account, symbol, execution price, size, side, time, closedPnL, leverage, etc.).
- **Preparation:** Loaded both datasets; documented rows/columns, missing values, and duplicates; converted timestamps and aligned at daily level; merged sentiment onto trades by date.
- **Metrics:** Daily PnL per trader, win rate (share of trades with PnL > 0), average trade size, average leverage, number of trades per day, long/short ratio. Aggregated to day level and by sentiment for Fear vs Greed comparison.
- **Segments:** (1) High vs low leverage (by median leverage per account), (2) Frequent vs infrequent (by median trades per day), (3) Consistent winners vs inconsistent (mean win rate ≥ 50% and stable).
- **Analysis:** Compared performance (PnL, win rate, drawdown proxy) and behavior (trade frequency, leverage, long/short bias, position size) between Fear and Greed days; cross-tabulated sentiment × segments; produced multiple charts and tables.
- **Bonus:** Random Forest classifier to predict next-day PnL bucket (low/mid/high) from sentiment + behavior features; K-means clustering of traders into behavioral archetypes; Streamlit dashboard to explore outputs.

## Insights

1. **Performance by sentiment:** Mean/median daily PnL and win rate differ between Fear and Greed days; drawdown proxy (worst daily PnL) is often more negative on Fear days, suggesting higher tail risk in Fear regimes.
2. **Behavior by sentiment:** Trade frequency, average leverage, long/short ratio, and average position size vary by sentiment; traders tend to adjust activity and risk in response to Fear vs Greed.
3. **Segments:** High-leverage and low-leverage (and frequent vs infrequent, consistent vs inconsistent) segments show different mean PnL and win rates; cross-tabs (e.g., sentiment × leverage segment) reveal which segments perform better in which regime.
4. **Leverage distribution:** Leverage distribution differs between Fear and Greed days (e.g., KDE plot), supporting the finding that traders change risk-taking by sentiment.
5. **Time series:** Where sufficient dates exist, daily trade volume by sentiment over time illustrates regime-specific activity.

## Strategy recommendations

1. **During Fear days, reduce leverage for the high-leverage segment.** High-leverage traders show larger drawdowns on Fear days; lowering leverage in Fear regimes can reduce tail risk for this segment.
2. **Increase trade frequency only for consistent winners on Greed days.** Consistent winners tend to perform better on Greed days; scaling activity in Greed for this segment may improve overall PnL while avoiding overtrading for inconsistent traders.

---

*Primetrade.ai Data Science Intern – Round-0 Assignment*
