import streamlit as st
import plotly.express as px

st.set_page_config(
    page_title="AI Insights",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Market Insights")

# Dataset Check
if "df" not in st.session_state:
    st.warning("Please upload a dataset from Home Page.")
    st.stop()

df = st.session_state["df"]

required_cols = ["Close"]

missing_cols = [
    col for col in required_cols
    if col not in df.columns
]

if missing_cols:
    st.error(f"Missing columns: {missing_cols}")
    st.stop()

# -------------------------
# Technical Indicators
# -------------------------

df["MA20"] = df["Close"].rolling(20).mean()
df["MA50"] = df["Close"].rolling(50).mean()

latest_close = df["Close"].iloc[-1]
latest_ma20 = df["MA20"].iloc[-1]
latest_ma50 = df["MA50"].iloc[-1]

# Trend Detection

if latest_close > latest_ma20 > latest_ma50:
    trend = "Bullish 📈"
    recommendation = "BUY 🟢"
elif latest_close < latest_ma20 < latest_ma50:
    trend = "Bearish 📉"
    recommendation = "SELL 🔴"
else:
    trend = "Sideways ➖"
    recommendation = "HOLD 🟡"

# Risk Score

df["Daily Return"] = df["Close"].pct_change()

risk_score = round(
    df["Daily Return"].std() * 100,
    2
)

# Market Strength

price_change = round(
    (
        (df["Close"].iloc[-1] -
         df["Close"].iloc[0])
        /
        df["Close"].iloc[0]
    ) * 100,
    2
)

# -------------------------
# KPI Cards
# -------------------------

st.subheader("📊 AI Summary")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Trend",
        trend
    )

with col2:
    st.metric(
        "Recommendation",
        recommendation
    )

with col3:
    st.metric(
        "Risk Score",
        f"{risk_score}%"
    )

with col4:
    st.metric(
        "Market Strength",
        f"{price_change}%"
    )

st.divider()

# -------------------------
# Buy Hold Sell Signal
# -------------------------

st.subheader("🎯 Trading Signal")

if recommendation.startswith("BUY"):

    st.success("""
    BUY SIGNAL DETECTED

    Current trend indicates strong upward momentum.
    Moving averages support bullish continuation.
    """)

elif recommendation.startswith("SELL"):

    st.error("""
    SELL SIGNAL DETECTED

    Current trend indicates downward pressure.
    Consider risk management strategies.
    """)

else:

    st.warning("""
    HOLD SIGNAL DETECTED

    Market is consolidating.
    Wait for stronger confirmation.
    """)

st.divider()

# -------------------------
# Trend Visualization
# -------------------------

st.subheader("📈 Trend Strength")

fig = px.line(
    df,
    y="Close",
    title="Closing Price Trend"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# -------------------------
# Risk Analysis
# -------------------------

st.subheader("⚠️ Risk Analysis")

if risk_score < 1:
    st.success("Low Risk Market")
elif risk_score < 3:
    st.warning("Moderate Risk Market")
else:
    st.error("High Risk Market")

st.progress(
    min(int(risk_score * 10), 100)
)

st.divider()

# -------------------------
# AI Generated Insights
# -------------------------

st.subheader("🧠 AI Generated Insights")

insights = []

if trend.startswith("Bullish"):
    insights.append(
        "Price is trading above major moving averages."
    )

if trend.startswith("Bearish"):
    insights.append(
        "Price is trading below major moving averages."
    )

if risk_score > 3:
    insights.append(
        "Market volatility is elevated."
    )

if price_change > 10:
    insights.append(
        "Strong positive market performance observed."
    )

if price_change < -10:
    insights.append(
        "Significant downward market pressure detected."
    )

if len(insights) == 0:
    insights.append(
        "Market conditions appear neutral."
    )

for item in insights:
    st.write("✅", item)

st.divider()

# -------------------------
# Confidence Score
# -------------------------

st.subheader("📌 Confidence Score")

confidence = min(
    95,
    max(
        55,
        int(abs(price_change))
    )
)

st.metric(
    "AI Confidence",
    f"{confidence}%"
)

st.progress(confidence)

st.divider()

st.success(
    "AI Analysis Completed Successfully"
)

st.caption(
    "Stock Analytics Pro | AI Insights Module"
)