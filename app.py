from ai_engine import *
from report_generator import generate_pdf_report
import os
import streamlit as st
import pandas as pd
import plotly.express as px
from utils import load_data

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------

st.set_page_config(
    page_title="AI Business Intelligence Platform",
    page_icon="📊",
    layout="wide"
)

# -------------------------------------------------
# CUSTOM CSS
# -------------------------------------------------

st.markdown("""
<style>

.main{
    background-color:#f5f7fa;
}

h1,h2,h3{
    color:#003366;
}

.stMetric{
    background-color:white;
    padding:15px;
    border-radius:12px;
    box-shadow:0px 2px 8px rgba(0,0,0,0.1);
}

.sidebar .sidebar-content{
    background:#003366;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# HEADER
# -------------------------------------------------

st.title("📊 AI Business Intelligence Platform")

st.markdown(
"""
Upload your business dataset and generate interactive
dashboards, KPI metrics and AI-ready insights.
"""
)

# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go To",
    [
        "🏠 Home",
        "📊 Dashboard",
        "📈 Sales Analysis",
        "💰 Profit Analysis",
        "🌍 Regional Analysis",
        "👥 Customer Analysis",
        "🤖 AI Chat",
        "📄 Reports",
        "ℹ About"
    ]
)
st.sidebar.divider()

api_key = st.sidebar.text_input(
    "Gemini API Key",
    type="password"
)

# -------------------------------------------------
# HOME PAGE
# -------------------------------------------------

if page=="🏠 Home":

    st.header("Upload Dataset")

    uploaded_file = st.file_uploader(
        "Upload CSV File",
        type="csv"
    )

    if uploaded_file:

        df = load_data(uploaded_file)

        st.success("Dataset Loaded Successfully!")

        st.subheader("Dataset Preview")

        st.dataframe(df.head(10))

        st.subheader("Dataset Information")

        c1,c2,c3 = st.columns(3)

        c1.metric("Rows",df.shape[0])

        c2.metric("Columns",df.shape[1])

        c3.metric(
            "Missing Values",
            df.isnull().sum().sum()
        )

# -------------------------------------------------
# DASHBOARD
# -------------------------------------------------

elif page=="📊 Dashboard":

    uploaded_file = st.file_uploader(
        "Upload CSV",
        type="csv"
    )

    if uploaded_file:

        df=load_data(uploaded_file)

        st.header("Business Dashboard")

        total_sales=df["Sales"].sum()

        total_profit=df["Profit"].sum()

        total_orders=df["Order ID"].nunique()

        total_customers=df["Customer ID"].nunique()

        c1,c2,c3,c4=st.columns(4)

        c1.metric(
            "Sales",
            f"${total_sales:,.2f}"
        )

        c2.metric(
            "Profit",
            f"${total_profit:,.2f}"
        )

        c3.metric(
            "Orders",
            total_orders
        )

        c4.metric(
            "Customers",
            total_customers
        )

        st.divider()

        st.subheader("Sales by Category")

        sales=df.groupby("Category")["Sales"].sum().reset_index()

        fig=px.bar(
            sales,
            x="Category",
            y="Sales",
            color="Category",
            text_auto=True
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        st.subheader("Profit by Category")

        profit=df.groupby("Category")["Profit"].sum().reset_index()

        fig=px.bar(
            profit,
            x="Category",
            y="Profit",
            color="Category",
            text_auto=True
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

# -------------------------------------------------
# SALES PAGE
# -------------------------------------------------

elif page=="📈 Sales Analysis":

    uploaded_file=st.file_uploader(
        "Upload CSV",
        type="csv"
    )

    if uploaded_file:

        df=load_data(uploaded_file)

        st.header("Sales Analysis")

        sales_region=df.groupby("Region")["Sales"].sum().reset_index()

        fig=px.pie(
            sales_region,
            names="Region",
            values="Sales",
            hole=0.4
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        st.subheader("Top 10 Products")

        top_products=(
            df.groupby("Product Name")["Sales"]
            .sum()
            .sort_values(ascending=False)
            .head(10)
            .reset_index()
        )

        fig=px.bar(
            top_products,
            x="Sales",
            y="Product Name",
            orientation="h"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

# -------------------------------------------------
# PROFIT PAGE
# -------------------------------------------------

elif page=="💰 Profit Analysis":

    uploaded_file=st.file_uploader(
        "Upload CSV",
        type="csv"
    )

    if uploaded_file:

        df=load_data(uploaded_file)

        st.header("Profit Analysis")

        fig=px.histogram(
            df,
            x="Profit",
            nbins=40
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        st.subheader("Profit by Region")

        region=df.groupby("Region")["Profit"].sum().reset_index()

        fig=px.bar(
            region,
            x="Region",
            y="Profit",
            color="Region"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

# -------------------------------------------------
# REGION PAGE
# -------------------------------------------------

elif page=="🌍 Regional Analysis":

    uploaded_file=st.file_uploader(
        "Upload CSV",
        type="csv"
    )

    if uploaded_file:

        df=load_data(uploaded_file)

        st.header("Regional Performance")

        regional=df.groupby("Region")[["Sales","Profit"]].sum().reset_index()

        st.dataframe(regional)

        fig=px.bar(
            regional,
            x="Region",
            y="Sales",
            color="Profit"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

# -------------------------------------------------
# CUSTOMER PAGE
# -------------------------------------------------

elif page=="👥 Customer Analysis":

    uploaded_file=st.file_uploader(
        "Upload CSV",
        type="csv"
    )

    if uploaded_file:

        df=load_data(uploaded_file)

        st.header("Top Customers")

        customer=(
            df.groupby("Customer Name")["Sales"]
            .sum()
            .sort_values(ascending=False)
            .head(15)
            .reset_index()
        )

        st.dataframe(customer)

        fig=px.bar(
            customer,
            x="Sales",
            y="Customer Name",
            orientation="h"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

# -------------------------------------------------
# NEW
# -------------------------------------------------

elif page == "🤖 AI Chat":
    st.header("🤖 AI Chat")
    st.info("This page will connect to Gemini AI. We'll complete it in the next step.")

elif page == "📄 Reports":
    st.header("📄 Reports")
    st.info("This page will generate and download PDF reports. We'll complete it in the next step.")



# -------------------------------------------------
# ABOUT
# -------------------------------------------------

elif page=="ℹ About":

    st.header("About")

    st.markdown("""
### AI Business Intelligence Platform

This project demonstrates:

- Business Intelligence

- Data Analytics

- Interactive Dashboards

- Plotly Visualization

- AI Powered Analytics

---

Developed by

**Kartik Dhyani**

Data Analytics Portfolio Project
""")