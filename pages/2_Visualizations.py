import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(layout="wide")

st.title("📈 Advanced Visualizations")

# Dataset Check
if "df" not in st.session_state:
    st.warning("Please upload a dataset from Home Page.")
    st.stop()

df = st.session_state["df"]

required_cols = [
    "Date",
    "Open",
    "High",
    "Low",
    "Close",
    "Volume"
]

missing_cols = [
    col for col in required_cols
    if col not in df.columns
]

if missing_cols:
    st.error(f"Missing columns: {missing_cols}")
    st.stop()

df["Date"] = pd.to_datetime(df["Date"])

# -------------------------
# Candlestick Chart
# -------------------------

st.subheader("🕯️ Candlestick Chart")

fig_candle = go.Figure(
    data=[
        go.Candlestick(
            x=df["Date"],
            open=df["Open"],
            high=df["High"],
            low=df["Low"],
            close=df["Close"]
        )
    ]
)

fig_candle.update_layout(
    height=650,
    xaxis_title="Date",
    yaxis_title="Price"
)

st.plotly_chart(
    fig_candle,
    use_container_width=True
)

st.divider()

# -------------------------
# Volume Analysis
# -------------------------

st.subheader("📊 Volume Analysis")

fig_volume = px.bar(
    df,
    x="Date",
    y="Volume",
    title="Trading Volume"
)

st.plotly_chart(
    fig_volume,
    use_container_width=True
)

st.divider()

# -------------------------
# OHLC Comparison
# -------------------------

st.subheader("📈 OHLC Comparison")

fig_ohlc = px.line(
    df,
    x="Date",
    y=[
        "Open",
        "High",
        "Low",
        "Close"
    ],
    title="OHLC Trend Analysis"
)

st.plotly_chart(
    fig_ohlc,
    use_container_width=True
)

st.divider()

# -------------------------
# Correlation Heatmap
# -------------------------

st.subheader("🔥 Correlation Heatmap")

corr = df[
    [
        "Open",
        "High",
        "Low",
        "Close",
        "Volume"
    ]
].corr()

fig_heat = px.imshow(
    corr,
    text_auto=True,
    aspect="auto",
    title="Feature Correlation Matrix"
)

st.plotly_chart(
    fig_heat,
    use_container_width=True
)

st.divider()

# -------------------------
# Price Distribution
# -------------------------

st.subheader("📉 Closing Price Distribution")

fig_hist = px.histogram(
    df,
    x="Close",
    nbins=40,
    title="Distribution of Closing Prices"
)

st.plotly_chart(
    fig_hist,
    use_container_width=True
)

st.divider()

# -------------------------
# Scatter Analysis
# -------------------------

st.subheader("🎯 Volume vs Close Price")

fig_scatter = px.scatter(
    df,
    x="Volume",
    y="Close",
    title="Volume vs Close Price Relationship"
)

st.plotly_chart(
    fig_scatter,
    use_container_width=True
)

st.divider()

# -------------------------
# Box Plot
# -------------------------

st.subheader("📦 OHLC Box Plot")

fig_box = px.box(
    df,
    y=[
        "Open",
        "High",
        "Low",
        "Close"
    ],
    title="Price Spread Analysis"
)

st.plotly_chart(
    fig_box,
    use_container_width=True
)

st.caption(
    "Stock Analytics Pro | Visualizations Module"
)