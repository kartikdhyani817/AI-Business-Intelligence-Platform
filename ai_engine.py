import google.generativeai as genai

# ---------------------------------------------------
# CONFIGURE GEMINI
# ---------------------------------------------------

def configure_gemini(api_key):
    """
    Configure Gemini API.
    """

    genai.configure(api_key=api_key)

    model = genai.GenerativeModel(
        "gemini-2.5-flash"
    )

    return model


# ---------------------------------------------------
# DATASET SUMMARY
# ---------------------------------------------------

def create_dataset_summary(df):

    summary = f"""

Business Dataset Summary

Rows:
{df.shape[0]}

Columns:
{df.shape[1]}

Total Sales:
{df['Sales'].sum():,.2f}

Total Profit:
{df['Profit'].sum():,.2f}

Total Orders:
{df['Order ID'].nunique()}

Total Customers:
{df['Customer ID'].nunique()}

Categories:

{list(df['Category'].unique())}

Regions:

{list(df['Region'].unique())}

Customer Segments:

{list(df['Segment'].unique())}

"""

    return summary


# ---------------------------------------------------
# BUSINESS INSIGHTS
# ---------------------------------------------------

def generate_business_insights(model, summary):

    prompt = f"""

You are an experienced Business Intelligence Consultant.

Analyze the following dataset summary.

Provide:

1. Executive Summary

2. Key Business Insights

3. Risks

4. Growth Opportunities

5. Recommendations

Dataset

{summary}

"""

    response = model.generate_content(prompt)

    return response.text


# ---------------------------------------------------
# SWOT ANALYSIS
# ---------------------------------------------------

def generate_swot(model, summary):

    prompt = f"""

Perform a SWOT Analysis.

Dataset

{summary}

"""

    response = model.generate_content(prompt)

    return response.text


# ---------------------------------------------------
# EXECUTIVE SUMMARY
# ---------------------------------------------------

def executive_summary(model, summary):

    prompt = f"""

Generate a one-page Executive Summary.

Dataset

{summary}

"""

    response = model.generate_content(prompt)

    return response.text


# ---------------------------------------------------
# DATASET CHAT
# ---------------------------------------------------

def ask_ai(model, summary, question):

    prompt = f"""

You are a Senior Data Analyst.

Dataset Summary

{summary}

User Question

{question}

Answer professionally.

"""

    response = model.generate_content(prompt)

    return response.text


# ---------------------------------------------------
# BUSINESS HEALTH SCORE
# ---------------------------------------------------

def business_health(model, summary):

    prompt = f"""

Give this company a Business Health Score out of 100.

Explain your reasoning.

Dataset

{summary}

"""

    response = model.generate_content(prompt)

    return response.text


# ---------------------------------------------------
# COST REDUCTION
# ---------------------------------------------------

def cost_reduction(model, summary):

    prompt = f"""

Suggest 10 ways to reduce operational cost.

Dataset

{summary}

"""

    response = model.generate_content(prompt)

    return response.text


# ---------------------------------------------------
# SALES IMPROVEMENT
# ---------------------------------------------------

def sales_strategy(model, summary):

    prompt = f"""

Suggest 10 strategies to increase revenue.

Dataset

{summary}

"""

    response = model.generate_content(prompt)

    return response.text


# ---------------------------------------------------
# CUSTOMER RETENTION
# ---------------------------------------------------

def customer_retention(model, summary):

    prompt = f"""

Suggest customer retention strategies.

Dataset

{summary}

"""

    response = model.generate_content(prompt)

    return response.text