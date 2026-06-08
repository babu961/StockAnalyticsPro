import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.linear_model import LinearRegression

st.set_page_config(layout="wide")

st.title("🔮 Stock Price Prediction")

# Dataset Check
if "df" not in st.session_state:
    st.warning("Please upload a dataset from Home Page.")
    st.stop()

df = st.session_state["df"]

required_cols = [
    "Date",
    "Close"
]

missing_cols = [
    col for col in required_cols
    if col not in df.columns
]

if missing_cols:
    st.error(f"Missing columns: {missing_cols}")
    st.stop()

# Data Preparation

df["Date"] = pd.to_datetime(df["Date"])

df = df.sort_values("Date")

df["Day"] = np.arange(len(df))

X = df[["Day"]]
y = df["Close"]

# Train Model

model = LinearRegression()
model.fit(X, y)

st.subheader("⚙️ Forecast Settings")

future_days = st.slider(
    "Select Forecast Days",
    min_value=7,
    max_value=90,
    value=30
)

# Future Prediction

future_x = np.arange(
    len(df),
    len(df) + future_days
).reshape(-1, 1)

predictions = model.predict(
    future_x
)

future_dates = pd.date_range(
    start=df["Date"].iloc[-1],
    periods=future_days + 1,
    freq="D"
)[1:]

forecast_df = pd.DataFrame({
    "Date": future_dates,
    "Predicted Close": predictions
})

# KPI Cards

st.subheader("📊 Forecast Summary")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Current Close",
        round(df["Close"].iloc[-1], 2)
    )

with col2:
    st.metric(
        "Forecast Days",
        future_days
    )

with col3:
    st.metric(
        "Predicted Final Price",
        round(predictions[-1], 2)
    )

st.divider()

# Historical vs Forecast

st.subheader("📈 Historical vs Forecast")

historical = df[
    ["Date", "Close"]
].copy()

historical.columns = [
    "Date",
    "Price"
]

forecast = forecast_df.copy()

forecast.columns = [
    "Date",
    "Price"
]

historical["Type"] = "Historical"
forecast["Type"] = "Forecast"

combined = pd.concat(
    [historical, forecast]
)

fig = px.line(
    combined,
    x="Date",
    y="Price",
    color="Type",
    title="Stock Forecast"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# Forecast Table

st.subheader("📅 Forecast Data")

st.dataframe(
    forecast_df,
    use_container_width=True
)

st.divider()

# Download Forecast

csv = forecast_df.to_csv(
    index=False
)

st.download_button(
    label="📥 Download Forecast",
    data=csv,
    file_name="forecast.csv",
    mime="text/csv"
)

# Basic Model Information

st.subheader("🤖 Model Information")

st.info("""
Current model uses Linear Regression for trend forecasting.

For future upgrades:
- LSTM Forecasting
- ARIMA Models
- Prophet Forecasting
- AI Sentiment Analysis
""")

st.caption(
    "Stock Analytics Pro | Prediction Module"
)