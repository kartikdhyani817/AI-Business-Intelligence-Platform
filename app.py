import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="AI Business Intelligence Platform",
    layout="wide"
)

st.title("📊 AI Business Intelligence Platform")

uploaded_file = st.file_uploader(
    "Upload CSV Dataset",
    type=["csv"]
)

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    st.success("Dataset Loaded Successfully")

    st.subheader("Dataset Preview")

    st.dataframe(df.head())

    st.subheader("Dataset Shape")

    col1, col2 = st.columns(2)

    col1.metric("Rows", df.shape[0])

    col2.metric("Columns", df.shape[1])

    st.subheader("Business KPIs")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Sales",
        f"${df['Sales'].sum():,.2f}"
    )

    c2.metric(
        "Profit",
        f"${df['Profit'].sum():,.2f}"
    )

    c3.metric(
        "Orders",
        df["Order ID"].nunique()
    )

    c4.metric(
        "Customers",
        df["Customer ID"].nunique()
    )

    st.subheader("Sales by Category")

    sales = (
        df.groupby("Category")["Sales"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        sales,
        x="Category",
        y="Sales"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.subheader("Profit by Category")

    profit = (
        df.groupby("Category")["Profit"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        profit,
        x="Category",
        y="Profit"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.subheader("Sales by Region")

    region = (
        df.groupby("Region")["Sales"]
        .sum()
        .reset_index()
    )

    fig = px.pie(
        region,
        names="Region",
        values="Sales"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )