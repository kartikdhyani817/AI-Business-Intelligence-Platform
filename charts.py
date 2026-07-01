import pandas as pd
import plotly.express as px


def sales_category_chart(df):

    sales = (
        df.groupby("Category")["Sales"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        sales,
        x="Category",
        y="Sales",
        color="Category",
        title="Sales by Category",
        text_auto=True
    )

    return fig


def profit_category_chart(df):

    profit = (
        df.groupby("Category")["Profit"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        profit,
        x="Category",
        y="Profit",
        color="Category",
        title="Profit by Category",
        text_auto=True
    )

    return fig


def regional_sales_chart(df):

    region = (
        df.groupby("Region")["Sales"]
        .sum()
        .reset_index()
    )

    fig = px.pie(
        region,
        names="Region",
        values="Sales",
        hole=0.45,
        title="Regional Sales"
    )

    return fig


def customer_chart(df):

    customer = (
        df.groupby("Customer Name")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig = px.bar(
        customer,
        x="Sales",
        y="Customer Name",
        orientation="h",
        title="Top Customers"
    )

    return fig


def product_chart(df):

    product = (
        df.groupby("Product Name")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig = px.bar(
        product,
        x="Sales",
        y="Product Name",
        orientation="h",
        title="Top Products"
    )

    return fig


def sales_profit_scatter(df):

    fig = px.scatter(
        df,
        x="Sales",
        y="Profit",
        color="Category",
        hover_data=["Product Name"],
        title="Sales vs Profit"
    )

    return fig


def monthly_sales_chart(df):

    temp = df.copy()

    temp["Order Date"] = pd.to_datetime(temp["Order Date"])

    temp["Month"] = temp["Order Date"].dt.to_period("M").astype(str)

    monthly = (
        temp.groupby("Month")["Sales"]
        .sum()
        .reset_index()
    )

    fig = px.line(
        monthly,
        x="Month",
        y="Sales",
        markers=True,
        title="Monthly Sales Trend"
    )

    return fig