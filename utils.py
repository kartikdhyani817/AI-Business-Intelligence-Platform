import pandas as pd


def load_data(uploaded_file):
    """
    Load CSV file into a pandas DataFrame.
    """

    df = pd.read_csv(uploaded_file)

    return df


def dataset_info(df):
    """
    Return basic dataset information.
    """

    info = {
        "Rows": df.shape[0],
        "Columns": df.shape[1],
        "Missing Values": int(df.isnull().sum().sum()),
        "Duplicate Rows": int(df.duplicated().sum())
    }

    return info


def sales_summary(df):

    return {
        "Total Sales": df["Sales"].sum(),
        "Average Sales": df["Sales"].mean(),
        "Maximum Sale": df["Sales"].max(),
        "Minimum Sale": df["Sales"].min()
    }


def profit_summary(df):

    return {
        "Total Profit": df["Profit"].sum(),
        "Average Profit": df["Profit"].mean(),
        "Maximum Profit": df["Profit"].max(),
        "Minimum Profit": df["Profit"].min()
    }


def top_customers(df, n=10):

    return (
        df.groupby("Customer Name")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(n)
        .reset_index()
    )


def top_products(df, n=10):

    return (
        df.groupby("Product Name")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(n)
        .reset_index()
    )


def sales_by_region(df):

    return (
        df.groupby("Region")["Sales"]
        .sum()
        .reset_index()
    )


def profit_by_region(df):

    return (
        df.groupby("Region")["Profit"]
        .sum()
        .reset_index()
    )


def sales_by_category(df):

    return (
        df.groupby("Category")["Sales"]
        .sum()
        .reset_index()
    )


def profit_by_category(df):

    return (
        df.groupby("Category")["Profit"]
        .sum()
        .reset_index()
    )