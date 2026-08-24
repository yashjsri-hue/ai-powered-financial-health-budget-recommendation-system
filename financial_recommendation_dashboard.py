# ============================================================
# PROJECT #6
# AI-POWERED PERSONAL FINANCE & BUDGET RECOMMENDATION SYSTEM
# ============================================================
# STEP 5 — FINANCIAL RECOMMENDATION DASHBOARD
# ============================================================

import streamlit as st
import pandas as pd
import plotly.express as px


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AI Financial Recommendation Dashboard",
    page_icon="💰",
    layout="wide"
)


# ============================================================
# TITLE
# ============================================================

st.title("💰 AI-Powered Financial Health & Budget Recommendation System")
st.subheader("Financial Recommendation Dashboard")

st.markdown(
    """
    This dashboard provides interactive financial health analysis,
    recommendation insights, priority analysis and personalized
    AI-generated financial recommendations.
    """
)


# ============================================================
# LOAD DATA
# ============================================================

FILE_NAME = "financial_recommendations_v2.csv"

try:
    df = pd.read_csv(FILE_NAME)

except FileNotFoundError:
    st.error(
        f"File '{FILE_NAME}' was not found. "
        "Place the CSV file in the same folder as this Python file."
    )
    st.stop()


# ============================================================
# DATASET INFORMATION
# ============================================================

st.success("Financial recommendation dataset loaded successfully.")

# Remove accidental spaces from column names
df.columns = df.columns.str.strip()


# ============================================================
# SIDEBAR FILTERS
# ============================================================

st.sidebar.header("🔎 Dashboard Filters")


# Financial Health Filter
if "predicted_financial_health" in df.columns:

    health_options = sorted(
        df["predicted_financial_health"]
        .dropna()
        .unique()
        .tolist()
    )

    selected_health = st.sidebar.multiselect(
        "Financial Health",
        health_options,
        default=health_options
    )

else:
    selected_health = []


# Recommendation Category Filter
if "recommendation_category" in df.columns:

    category_options = sorted(
        df["recommendation_category"]
        .dropna()
        .unique()
        .tolist()
    )

    selected_category = st.sidebar.multiselect(
        "Recommendation Category",
        category_options,
        default=category_options
    )

else:
    selected_category = []


# Priority Filter
if "recommendation_priority" in df.columns:

    priority_options = sorted(
        df["recommendation_priority"]
        .dropna()
        .unique()
        .tolist()
    )

    selected_priority = st.sidebar.multiselect(
        "Recommendation Priority",
        priority_options,
        default=priority_options
    )

else:
    selected_priority = []


# ============================================================
# APPLY FILTERS
# ============================================================

filtered_df = df.copy()


if selected_health:
    filtered_df = filtered_df[
        filtered_df["predicted_financial_health"].isin(selected_health)
    ]


if selected_category:
    filtered_df = filtered_df[
        filtered_df["recommendation_category"].isin(selected_category)
    ]


if selected_priority:
    filtered_df = filtered_df[
        filtered_df["recommendation_priority"].isin(selected_priority)
    ]


# ============================================================
# DASHBOARD SUMMARY
# ============================================================

st.header("📊 Financial Overview")


total_users = len(filtered_df)


if "predicted_financial_health" in filtered_df.columns:
    healthy_users = (
        filtered_df["predicted_financial_health"]
        .eq("Healthy")
        .sum()
    )

    moderate_users = (
        filtered_df["predicted_financial_health"]
        .eq("Moderate")
        .sum()
    )

    attention_users = (
        filtered_df["predicted_financial_health"]
        .eq("Needs Attention")
        .sum()
    )

else:
    healthy_users = moderate_users = attention_users = 0


if "recommendation_score" in filtered_df.columns:
    average_score = filtered_df["recommendation_score"].mean()
else:
    average_score = 0


if "recommendation_priority" in filtered_df.columns:
    high_priority_users = (
        filtered_df["recommendation_priority"]
        .eq("High")
        .sum()
    )
else:
    high_priority_users = 0


# ============================================================
# KPI CARDS
# ============================================================

col1, col2, col3, col4, col5, col6 = st.columns(6)


with col1:
    st.metric(
        "Total Users",
        f"{total_users:,}"
    )


with col2:
    st.metric(
        "Healthy",
        f"{healthy_users:,}"
    )


with col3:
    st.metric(
        "Moderate",
        f"{moderate_users:,}"
    )


with col4:
    st.metric(
        "Needs Attention",
        f"{attention_users:,}"
    )


with col5:
    st.metric(
        "Avg Recommendation Score",
        f"{average_score:.1f}"
    )


with col6:
    st.metric(
        "High Priority",
        f"{high_priority_users:,}"
    )


# ============================================================
# FINANCIAL HEALTH ANALYSIS
# ============================================================

st.header("🏦 Financial Health Analysis")


col1, col2 = st.columns(2)


# Financial Health Distribution
with col1:

    if "predicted_financial_health" in filtered_df.columns:

        health_count = (
            filtered_df["predicted_financial_health"]
            .value_counts()
            .reset_index()
        )

        health_count.columns = [
            "Financial Health",
            "Users"
        ]

        fig_health = px.pie(
            health_count,
            names="Financial Health",
            values="Users",
            title="Financial Health Distribution",
            hole=0.4
        )

        st.plotly_chart(
            fig_health,
            use_container_width=True
        )


# Recommendation Priority
with col2:

    if "recommendation_priority" in filtered_df.columns:

        priority_count = (
            filtered_df["recommendation_priority"]
            .value_counts()
            .reset_index()
        )

        priority_count.columns = [
            "Priority",
            "Users"
        ]

        fig_priority = px.bar(
            priority_count,
            x="Priority",
            y="Users",
            title="Recommendation Priority Distribution",
            text="Users"
        )

        fig_priority.update_traces(
            textposition="outside"
        )

        st.plotly_chart(
            fig_priority,
            use_container_width=True
        )


# ============================================================
# RECOMMENDATION CATEGORY ANALYSIS
# ============================================================

st.header("🎯 Recommendation Analysis")


if "recommendation_category" in filtered_df.columns:

    category_count = (
        filtered_df["recommendation_category"]
        .value_counts()
        .reset_index()
    )

    category_count.columns = [
        "Recommendation Category",
        "Users"
    ]

    fig_category = px.bar(
        category_count,
        x="Recommendation Category",
        y="Users",
        title="Recommendation Category Distribution",
        text="Users"
    )

    fig_category.update_traces(
        textposition="outside"
    )

    fig_category.update_layout(
        xaxis_tickangle=-30
    )

    st.plotly_chart(
        fig_category,
        use_container_width=True
    )


# ============================================================
# SAVINGS RATE ANALYSIS
# ============================================================

st.header("💵 Savings & Expense Analysis")


col1, col2 = st.columns(2)


# Savings Rate
with col1:

    if "savings_rate" in filtered_df.columns:

        fig_savings = px.histogram(
            filtered_df,
            x="savings_rate",
            nbins=30,
            title="Savings Rate Distribution",
            labels={
                "savings_rate": "Savings Rate"
            }
        )

        st.plotly_chart(
            fig_savings,
            use_container_width=True
        )


# Expense-to-Income Ratio
with col2:

    if "expense_to_income_ratio" in filtered_df.columns:

        fig_expense = px.histogram(
            filtered_df,
            x="expense_to_income_ratio",
            nbins=30,
            title="Expense-to-Income Ratio Distribution",
            labels={
                "expense_to_income_ratio":
                "Expense-to-Income Ratio"
            }
        )

        st.plotly_chart(
            fig_expense,
            use_container_width=True
        )


# ============================================================
# RECOMMENDATION SCORE ANALYSIS
# ============================================================

st.header("⭐ Recommendation Score Analysis")


if "recommendation_score" in filtered_df.columns:

    fig_score = px.histogram(
        filtered_df,
        x="recommendation_score",
        nbins=20,
        title="AI Recommendation Score Distribution",
        labels={
            "recommendation_score":
            "Recommendation Score"
        }
    )

    st.plotly_chart(
        fig_score,
        use_container_width=True
    )


# ============================================================
# HEALTH VS RECOMMENDATION CATEGORY
# ============================================================

st.header("🔗 Financial Health vs Recommendation Category")


if (
    "predicted_financial_health" in filtered_df.columns
    and
    "recommendation_category" in filtered_df.columns
):

    cross_data = (
        filtered_df.groupby(
            [
                "predicted_financial_health",
                "recommendation_category"
            ]
        )
        .size()
        .reset_index(name="Users")
    )

    fig_cross = px.bar(
        cross_data,
        x="predicted_financial_health",
        y="Users",
        color="recommendation_category",
        title="Financial Health vs Recommendation Category",
        barmode="group"
    )

    st.plotly_chart(
        fig_cross,
        use_container_width=True
    )


# ============================================================
# TOP PRIORITY USERS
# ============================================================

st.header("🚨 High-Priority Financial Cases")


if "recommendation_priority" in filtered_df.columns:

    high_priority_df = filtered_df[
        filtered_df["recommendation_priority"] == "High"
    ].copy()

    if not high_priority_df.empty:

        display_columns = [
            "user_id",
            "savings_rate",
            "expense_to_income_ratio",
            "predicted_financial_health",
            "recommendation_category",
            "recommendation_priority",
            "recommendation_score"
        ]

        display_columns = [
            col for col in display_columns
            if col in high_priority_df.columns
        ]

        st.dataframe(
            high_priority_df[
                display_columns
            ].sort_values(
                "recommendation_score",
                ascending=True
            ),
            use_container_width=True
        )

    else:
        st.info("No high-priority users found for the selected filters.")


# ============================================================
# PERSONALIZED AI RECOMMENDATIONS
# ============================================================

st.header("🤖 Personalized AI Financial Recommendations")


if "ai_recommendation" in filtered_df.columns:

    recommendation_columns = [
        "user_id",
        "predicted_financial_health",
        "recommendation_category",
        "recommendation_priority",
        "recommendation_score",
        "ai_recommendation"
    ]

    recommendation_columns = [
        col for col in recommendation_columns
        if col in filtered_df.columns
    ]

    recommendation_df = filtered_df[
        recommendation_columns
    ].copy()

    st.dataframe(
        recommendation_df,
        use_container_width=True,
        height=450
    )


# ============================================================
# DATASET PREVIEW
# ============================================================

with st.expander("📋 View Filtered Dataset"):

    st.write(
        f"Filtered Records: {len(filtered_df):,}"
    )

    st.dataframe(
        filtered_df,
        use_container_width=True
    )


# ============================================================
# DOWNLOAD FILTERED DATA
# ============================================================

st.header("⬇️ Export")


csv_data = filtered_df.to_csv(index=False).encode("utf-8")


st.download_button(
    label="Download Filtered Recommendations",
    data=csv_data,
    file_name="filtered_financial_recommendations.csv",
    mime="text/csv"
)


# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.caption(
    "AI-Powered Personal Finance & Budget Recommendation System | "
    "Step 5 — Financial Recommendation Dashboard"
)
