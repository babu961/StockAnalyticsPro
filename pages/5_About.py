import streamlit as st

st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide"
)

st.title("ℹ️ About Stock Analytics Pro")

st.markdown("""
# 📈 Stock Analytics Pro

An AI-Powered Market Intelligence Platform built using Python, Streamlit,
Pandas, Plotly, and Machine Learning.

The platform helps investors, analysts, and researchers understand
market trends through advanced analytics, forecasting, reporting,
and AI-driven insights.
""")

st.divider()

# Developer Section

st.subheader("👨‍💻 Developer")

col1, col2 = st.columns([1, 2])

with col1:
    st.image(
        "https://cdn-icons-png.flaticon.com/512/3135/3135715.png",
        width=150
    )

with col2:

    st.markdown("""
### Yashwanth

B.Tech – Full Stack Development

Passionate about:

- Data Analytics
- Artificial Intelligence
- Machine Learning
- Full Stack Development
- Financial Technology

Focused on building scalable and intelligent software solutions.
""")

st.divider()

# Technologies

st.subheader("🛠 Technologies Used")

col1, col2, col3 = st.columns(3)

with col1:

    st.success("Frontend")

    st.markdown("""
- Streamlit
- HTML/CSS
- Plotly
""")

with col2:

    st.success("Backend")

    st.markdown("""
- Python
- Pandas
- NumPy
""")

with col3:

    st.success("Machine Learning")

    st.markdown("""
- Scikit-Learn
- Linear Regression
- Predictive Analytics
""")

st.divider()

# Features

st.subheader("🚀 Key Features")

st.markdown("""
### 📊 Analytics Dashboard
- KPI Monitoring
- Trend Analysis
- Moving Averages
- Daily Returns

### 📈 Visualizations
- Candlestick Charts
- Correlation Heatmaps
- Volume Analysis
- OHLC Comparison

### 🔮 Predictions
- Future Stock Forecasting
- Trend Estimation
- Prediction Reports

### 📄 Reports
- Statistical Summaries
- Data Quality Reports
- CSV & PDF Export

### 🤖 AI Insights
- Bullish/Bearish Detection
- Buy/Sell Signals
- Risk Analysis
""")

st.divider()

# Project Architecture

st.subheader("🏗 Project Architecture")

st.code("""
Stock Analytics Pro

│
├── Home
├── Analytics
├── Visualizations
├── Predictions
├── Reports
├── AI Insights
└── About
""")

st.divider()

# Resume Description

st.subheader("💼 Resume Project Description")

st.info("""
Developed a multi-page Stock Analytics Pro web application using Python,
Streamlit, Pandas, Plotly, and Scikit-Learn.

Implemented KPI dashboards, financial visualizations,
machine learning-based forecasting, AI-driven insights,
interactive reports, and downloadable analytics features.

Designed a professional SaaS-style user interface
with real-time data exploration capabilities.
""")

st.divider()

# Future Enhancements

st.subheader("🔮 Future Enhancements")

st.markdown("""
- LSTM Deep Learning Forecasting
- News Sentiment Analysis
- Real-Time Market APIs
- Portfolio Optimization
- Risk Prediction Engine
- Automated Trading Signals
""")

st.divider()

st.success(
    "Thank you for exploring Stock Analytics Pro 🚀"
)

st.caption(
    "Version 1.0 | Built with Python, Streamlit & Machine Learning"
)