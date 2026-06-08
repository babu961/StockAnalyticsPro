import streamlit as st
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Stock Analytics Pro",
    page_icon="📊",
    layout="wide"
)
st.set_page_config(
    page_title="Stock Analytics Pro",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #0f172a, #1e293b);
}

h1 {
    color: #38bdf8 !important;
    text-align: center;
}

h2, h3 {
    color: white !important;
}

.stMetric {
    background-color: rgba(255,255,255,0.05);
    border-radius: 15px;
    padding: 10px;
}

[data-testid="stMetric"] {
    background: linear-gradient(135deg,#2563eb,#7c3aed);
    padding: 15px;
    border-radius: 15px;
    color: white;
}

.block-container {
    padding-top: 2rem;
}

</style>
""", unsafe_allow_html=True)

# Header
st.title("📈 Stock Analytics Pro")

st.markdown("""
### AI Powered Market Intelligence Platform

Analyze stock market trends, visualize financial insights,
forecast future prices, and generate professional reports.
""")

st.divider()

# Upload Dataset
uploaded_file = st.file_uploader(
    "📂 Upload Stock Market CSV Dataset",
    type=["csv"]
)

if uploaded_file:

    try:

        df = pd.read_csv(uploaded_file)

        st.session_state["df"] = df

        st.success("✅ Dataset Uploaded Successfully")

        st.subheader("📋 Dataset Overview")

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                "Rows",
                len(df)
            )

        with col2:
            st.metric(
                "Columns",
                len(df.columns)
            )

        with col3:
            st.metric(
                "Missing Values",
                int(df.isnull().sum().sum())
            )

        with col4:
            st.metric(
                "Features",
                len(df.columns)
            )

        st.divider()

        st.subheader("🔍 Dataset Preview")

        st.dataframe(
            df.head(10),
            use_container_width=True
        )

    except Exception as e:

        st.error(
            f"Error reading file: {e}"
        )

else:

    st.info(
        "Upload a CSV file to begin analysis."
    )

st.divider()

# Features Section

st.subheader("🚀 Platform Features")

col1, col2 = st.columns(2)

with col1:

    st.success("📊 Analytics")

    st.markdown("""
    - KPI Dashboard
    - Trend Analysis
    - Moving Averages
    - Daily Returns
    - Statistical Insights
    """)

with col2:

    st.success("🤖 AI & Forecasting")

    st.markdown("""
    - Stock Predictions
    - Risk Analysis
    - Buy/Sell Signals
    - Reports Export
    - Interactive Charts
    """)

st.divider()

# Workflow

st.subheader("⚙️ Workflow")

st.markdown("""
### Step 1
Upload Stock Market Dataset

### Step 2
Open Analytics Dashboard

### Step 3
Explore Visualizations

### Step 4
Generate Predictions

### Step 5
View AI Insights & Reports
""")

st.divider()

# Footer

st.caption(
    "Stock Analytics Pro | Built using Python, Streamlit, Pandas, Plotly & Scikit-Learn"
)
