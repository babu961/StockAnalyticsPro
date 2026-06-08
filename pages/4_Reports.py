import streamlit as st
import pandas as pd
from fpdf import FPDF
import tempfile

st.set_page_config(layout="wide")

st.title("📄 Reports Center")

# Dataset Check
if "df" not in st.session_state:
    st.warning("Please upload a dataset from Home Page.")
    st.stop()

df = st.session_state["df"]

st.subheader("📊 Executive Summary")

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

# Statistics

st.subheader("📈 Statistical Summary")

st.dataframe(
    df.describe(),
    use_container_width=True
)

st.divider()

# Missing Values

st.subheader("🔍 Data Quality Report")

missing_df = pd.DataFrame({
    "Column": df.columns,
    "Missing Values": df.isnull().sum().values
})

st.dataframe(
    missing_df,
    use_container_width=True
)

st.divider()

# Business Insights

st.subheader("💡 Key Insights")

if "Close" in df.columns:

    latest_close = df["Close"].iloc[-1]

    avg_close = df["Close"].mean()

    highest_close = df["Close"].max()

    lowest_close = df["Close"].min()

    st.success(
        f"Latest Close Price: {latest_close:.2f}"
    )

    st.info(
        f"Average Close Price: {avg_close:.2f}"
    )

    st.warning(
        f"Highest Close Price: {highest_close:.2f}"
    )

    st.error(
        f"Lowest Close Price: {lowest_close:.2f}"
    )

st.divider()

# CSV Export

st.subheader("📥 Export CSV")

csv = df.to_csv(index=False)

st.download_button(
    label="Download Dataset CSV",
    data=csv,
    file_name="stock_report.csv",
    mime="text/csv"
)

st.divider()

# PDF Export

st.subheader("📑 Export PDF Report")

if st.button("Generate PDF Report"):

    pdf = FPDF()

    pdf.add_page()

    pdf.set_font(
        "Arial",
        "B",
        16
    )

    pdf.cell(
        200,
        10,
        txt="Stock Analytics Pro Report",
        ln=True,
        align="C"
    )

    pdf.ln(10)

    pdf.set_font(
        "Arial",
        "",
        12
    )

    pdf.cell(
        200,
        10,
        txt=f"Rows: {len(df)}",
        ln=True
    )

    pdf.cell(
        200,
        10,
        txt=f"Columns: {len(df.columns)}",
        ln=True
    )

    pdf.cell(
        200,
        10,
        txt=f"Missing Values: {df.isnull().sum().sum()}",
        ln=True
    )

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    ) as tmp:

        pdf.output(tmp.name)

        with open(
            tmp.name,
            "rb"
        ) as f:

            st.download_button(
                "📥 Download PDF Report",
                f,
                "Stock_Report.pdf",
                "application/pdf"
            )

st.caption(
    "Stock Analytics Pro | Reports Module"
)