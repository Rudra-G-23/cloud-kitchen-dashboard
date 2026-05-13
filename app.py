import streamlit as st
import pandas as pd

# Page
st.set_page_config(
    page_icon="🧑‍🍳",
    page_title="Cloud Kitchen Dashboard",
    layout="wide"
)

# Load
@st.cache_data
def load_data():

    try:
        path = r"C:\Users\Rudra\Desktop\cloud-kitchen-dashboard\kittchen-pnl-data.xlsx"
        df = pd.read_excel(path, header=1)

    except:
        path = r"https://raw.githubusercontent.com/Rudra-G-23/cloud-kitchen-dashboard/main/kittchen-pnl-data.xlsx"
        df = pd.read_excel(path, header=1)

    df.columns = ( df.columns.str.strip().str.upper().str.replace(" ", "_"))

    df["GM"] = df["GROSS_MARGIN"]

    df["GM%"] = ( df["GROSS_MARGIN"] / df["NET_REVENUE"] ) * 100

    df["CM"] = df["KITCHEN_EBITDA"]

    df["CM_%"] = ( df["CM"] / df["NET_REVENUE"] ) * 100

    df["EBITDA"] = df["KITCHEN_EBITDA"].astype("int")
    
    df[['MONTH_NAME', 'YEAR']]= df['MONTH'].str.split("-", expand=True)
    
    return df

def kitchen_filter(df):
    # Sidebar
    with st.expander(label="⚙️ Filters for Kitchen Dashboard", expanded=True):
            
        col1, col2 = st.columns([3, 1])

        with col1:

            month_filter = st.multiselect(
                "Month",
                sorted(df["MONTH_NAME"].unique()),
                default=sorted(df["MONTH_NAME"].unique())
            )

            year_filter = st.multiselect(
                "Year",
                sorted(df['YEAR'].unique()),
                default=sorted(df['YEAR'].unique())
            )
            
            store_filter = st.multiselect(
                "Store",
                sorted(df["STORE"].unique()),
                default=sorted(df["STORE"].unique())
            )

            city_filter = st.multiselect(
                "City",
                sorted(df["CITY"].unique()),
                default=sorted(df["CITY"].unique())
            )
            
            min_ebitda = int(df['EBITDA'].min())
            max_ebitda = int(df['EBITDA'].max())

            ebitda_range = st.slider(
                label='Select EBITDA range in ₹',
                min_value=min_ebitda,
                max_value=max_ebitda,
                value=(min_ebitda, max_ebitda),
                step=10
            )

            
        with col2:
            
            revenue_filter = st.multiselect(
                "Revenue Cohort",
                sorted(df["REVENUE_COHORT"].dropna().unique()),
                default=sorted(df["REVENUE_COHORT"].dropna().unique())
            )

            cm_filter = st.multiselect(
                "CM Cohort",
                sorted(df["CM_COHORT"].dropna().unique()),
                default=sorted(df["CM_COHORT"].dropna().unique())
            )

            ebitda_cat_filter = st.multiselect(
                "EBITDA Category",
                sorted(df["EBITDA_CATEGORY"].dropna().unique()),
                default=sorted(df["EBITDA_CATEGORY"].dropna().unique())
            )

            ebitda_filter = st.multiselect(
                "EBITDA Cohort",
                sorted(df["EBITDA_COHORT"].dropna().unique()),
                default=sorted(df["EBITDA_COHORT"].dropna().unique())
            )
            
            zone_filter = st.multiselect(
                "Zone",
                sorted(df['ZONE_MAPPING'].dropna().unique()),
                default=sorted(df['ZONE_MAPPING'].dropna().unique())
            )
            
            status_filter = st.multiselect(
                "Status",
                sorted(df['STATUS'].dropna().unique()),
                default=sorted(df['STATUS'].dropna().unique())
            )

        # Filter df
        filtered_df = df[
            (df['YEAR'].isin(year_filter)) &
            (df["MONTH_NAME"].isin(month_filter)) &
            (df["STORE"].isin(store_filter)) &
            (df["CITY"].isin(city_filter)) &
            (df["REVENUE_COHORT"].isin(revenue_filter)) &
            (df["CM_COHORT"].isin(cm_filter)) &
            (df["EBITDA_CATEGORY"].isin(ebitda_cat_filter)) &
            (df["EBITDA_COHORT"].isin(ebitda_filter)) &
            (df['EBITDA'].between(ebitda_range[0], ebitda_range[1])) &
            (df['ZONE_MAPPING'].isin(zone_filter)) & 
            (df['STATUS'].isin(status_filter))
        ]
            
        return filtered_df

st.title("Cloud Kitchen Dashboard")

df = load_data()
filtered_df = kitchen_filter(df)

st.markdown("---")

revenue = filtered_df["NET_REVENUE"].sum()
gm = filtered_df["GM"].sum()
cm = filtered_df["CM"].sum()
# ebitda = filtered_df["EBITDA"].sum()

gm_percent = (gm / revenue * 100) if revenue != 0 else 0
cm_percent = (cm / revenue * 100) if revenue != 0 else 0

c1, c2, c3, c4, c5 = st.columns(5)

c1.metric("Revenue", f"₹ {revenue:,.0f}")
c2.metric("GM", f"₹ {gm:,.0f}")
c3.metric("GM%", f"{gm_percent:.2f}%")
c4.metric("CM", f"₹ {cm:,.0f}")
c5.metric("CM%", f"{cm_percent:.2f}%")

st.markdown(
    """
    <style>
    button[data-baseweb="tab"] > div[data-testid="stMarkdownContainer"] > p {
        font-size: 25px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
   
tab1, tab2, tab3 = st.tabs([
    "All Filter Data",
    "Store Wise",
    "Month Wise"
])

# Data
with tab1:

    st.dataframe(
        filtered_df,
        use_container_width=True,
        height=600
    )

# Store
with tab2:

    store_summary = (
        filtered_df
        .groupby("STORE")
        .agg({
            "NET_REVENUE": "sum",
            "GM": "sum",
            "CM": "sum",
            "EBITDA": "sum",
            "ORDER_COUNT": "sum"
        })
        .reset_index()
    )

    store_summary["GM%"] = ( store_summary["GM"] / store_summary["NET_REVENUE"] ) * 100

    store_summary["CM_%"] = ( store_summary["CM"] / store_summary["NET_REVENUE"] ) * 100

    st.dataframe( store_summary, use_container_width=True )

# Month
with tab3:

    month_summary = (
        filtered_df
        .groupby(["YEAR", "MONTH_NAME"])
        .agg({
            "NET_REVENUE": "sum",
            "GM": "sum",
            "CM": "sum",
            "EBITDA": "sum",
            "ORDER_COUNT": "sum"
        })
        .reset_index()
    )

    month_summary["GM%"] = ( month_summary["GM"] / month_summary["NET_REVENUE"] ) * 100

    month_summary["CM_%"] = ( month_summary["CM"] / month_summary["NET_REVENUE"] ) * 100

    st.dataframe( month_summary, use_container_width=True )

# Download
csv = filtered_df.to_csv(index=False)

st.download_button(
    "Download CSV",
    csv,
    "filtered_kitchen_data.csv",
    "text/csv"
)