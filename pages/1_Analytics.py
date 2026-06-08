import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

st.title("📊 Analytics Dashboard")

# Check Dataset
if "df" not in st.session_state:
    st.warning("Please upload a dataset from Home Page.")
    st.stop()

df = st.session_state["df"]

# Required Columns Check
required_cols = ["Date", "Open", "High", "Low", "Close", "Volume"]

missing_cols = [
    col for col in required_cols
    if col not in df.columns
]

if missing_cols:
    st.error(f"Missing columns: {missing_cols}")
    st.stop()

# Date Conversion
df["Date"] = pd.to_datetime(df["Date"])

# Sidebar Filters
st.sidebar.header("📅 Filters")

start_date = st.sidebar.date_input(
    "Start Date",
    df["Date"].min()
)

end_date = st.sidebar.date_input(
    "End Date",
    df["Date"].max()
)

df = df[
    (df["Date"] >= pd.to_datetime(start_date))
    &
    (df["Date"] <= pd.to_datetime(end_date))
]

# KPI Section
st.subheader("📈 Market Summary")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Latest Close",
        f"{df['Close'].iloc[-1]:.2f}"
    )

with col2:
    st.metric(
        "Highest High",
        f"{df['High'].max():.2f}"
    )

with col3:
    st.metric(
        "Lowest Low",
        f"{df['Low'].min():.2f}"
    )

with col4:
    st.metric(
        "Total Volume",
        f"{df['Volume'].sum():,.0f}"
    )

st.divider()

# Dataset Preview
st.subheader("📋 Dataset Preview")

st.dataframe(
    df.head(10),
    use_container_width=True
)

st.divider()

# Trend Analysis
st.subheader("📈 Trend Analysis")

numeric_cols = df.select_dtypes(
    include="number"
).columns

metric = st.selectbox(
    "Select Metric",
    numeric_cols
)

fig = px.line(
    df,
    x="Date",
    y=metric,
    title=f"{metric} Trend"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# Moving Averages
st.subheader("📊 Moving Average Analysis")

df["MA20"] = df["Close"].rolling(20).mean()
df["MA50"] = df["Close"].rolling(50).mean()
df["MA100"] = df["Close"].rolling(100).mean()

fig_ma = px.line(
    df,
    x="Date",
    y=[
        "Close",
        "MA20",
        "MA50",
        "MA100"
    ],
    title="Close Price vs Moving Averages"
)

st.plotly_chart(
    fig_ma,
    use_container_width=True
)

st.divider()

# Daily Returns
st.subheader("📉 Daily Return Analysis")

df["Daily Return %"] = (
    df["Close"].pct_change() * 100
)

fig_return = px.line(
    df,
    x="Date",
    y="Daily Return %",
    title="Daily Return Percentage"
)

st.plotly_chart(
    fig_return,
    use_container_width=True
)

st.divider()

# Volatility
st.subheader("⚡ Volatility Analysis")

volatility = (
    df["Daily Return %"]
    .std()
)

st.metric(
    "Volatility %",
    round(volatility, 2)
)

st.divider()

# Statistical Summary
st.subheader("📑 Statistical Summary")

st.dataframe(
    df.describe(),
    use_container_width=True
)

st.divider()

# Download
csv = df.to_csv(index=False)

st.download_button(
    label="📥 Download Processed Dataset",
    data=csv,
    file_name="processed_stock_data.csv",
    mime="text/csv"
)

st.caption(
    "Stock Analytics Pro | Analytics Module"
)