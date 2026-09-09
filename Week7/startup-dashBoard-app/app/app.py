import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("../data/startup_funding_cleaned.csv")
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month

def load_investor_details(investor_name):
    # Filter the DataFrame for the selected investor
    st.title(f"Investor Analysis: :violet[{investor_name}]")

    # Display the details of the selected investor

    ## most recent 5 investments
    last_5_df = (
        df[df["Investors"].str.contains(investor_name, na=False)]
        .sort_values(by="Date", ascending=False)
        .head(5)[
            ["Date", "startup", "Industry", "City", "Investors", "round", "Amount"]
        ]
    )
    st.subheader(f":red[Most Recent 5 Investments ]")
    st.dataframe(last_5_df)

    col1, col2 = st.columns(2)
    with col1:

        ## Biggest investments
        biggest_investments_df = (
            df[df["Investors"].str.contains(investor_name, na=False)]
            .groupby("startup")["Amount"]
            .sum()
            .sort_values(ascending=False)
            .head(10)
        )

        st.subheader(f":yellow[Biggest Investments]")
        st.dataframe(biggest_investments_df)
    with col2:
        ## Biggest investments Graph
        st.subheader(f":green[Biggest Investments Graph ]")
        st.bar_chart(biggest_investments_df)

    ## Invested Sectors

    inv_by_sector_df = (
        df[df["Investors"].str.contains(investor_name, na=False)]
        .groupby("Industry")["Amount"]
        .sum()
    )

    fig = px.pie(
        inv_by_sector_df,
        values=inv_by_sector_df.values,
        names=inv_by_sector_df.index,
        title="Invested Sectors",
    )
    st.plotly_chart(fig)

    ## Generally Investes in which Rounds
    inv_by_round_df = (
        df[df["Investors"].str.contains(investor_name, na=False)]
        .groupby("round")["Amount"]
        .sum()
    )
    fig2 = px.pie(
        inv_by_round_df,
        values=inv_by_round_df.values,
        names=inv_by_round_df.index,
        title="Invested Rounds",
    )
    st.plotly_chart(fig2)

    ## Generally Investes in which Cities
    inv_by_city_df = (
        df[df["Investors"].str.contains(investor_name)].groupby("City")["Amount"].sum()
    )
    fig3 = px.pie(
        inv_by_city_df,
        values=inv_by_city_df.values,
        names=inv_by_city_df.index,
        title="Invested Cities",
    )
    st.plotly_chart(fig3)

    ## YOY (year on year) investement total investment amount by year

    

    investment_by_year_df = (
        df[df["Investors"].str.contains(investor_name, na=False)]
        .groupby("Year")["Amount"]
        .sum()
    )

    fig = px.line(
        investment_by_year_df.reset_index(),
        x="Year",
        y="Amount",
        title="Annual Investment Comparison",
        # labels={"Year": "Year", "Amount": "Total Investment Amount in CR"},
    )
    st.plotly_chart(fig)


def over_all_analysis():
    st.title("Overall Analysis")
    st.write("This section provides an overview of the startup funding landscape.")
    # Add your overall analysis code here
    
    ## total amount of funding in india till date 
    total_funding = df["Amount"].sum()
    st.metric(label="Total Funding in India (in CR)", value=f"{total_funding:.2f} Crores" , border=True)
    
    ## highest funded startup in india till date
    highest_funded_startup = df["Amount"].max()
    highest_funded_startup_name = df[df["Amount"] == highest_funded_startup]["startup"].values[0]
    st.metric(label="Highest Funded Startup", value=highest_funded_startup_name, delta=f"{highest_funded_startup:.2f} Crores" , border=True)
    
    
    ## avg amount of funding in given to startups in india
    
    avg_funding = df["Amount"].mean()
    st.metric(label="Average Funding in India (in CR)", value=f"{avg_funding:.2f} Crores" , border=True)
    
    
    ## Total number of startups funded in india till date
    tolal_startups_funded = df["startup"].nunique()
    st.metric(label="Total Startups Funded in India", value=tolal_startups_funded , border=True)
    
    
    ## MOM analysis of funding in india on basis of number of startups funded and total amount of funding in india
    gp_y_m = df.groupby(["Year" , "Month"])

    


st.sidebar.title("Startup Funding Analysis From 2015 to 2020")

option = st.sidebar.selectbox(
    "Select the analysis type",
    ["Overall Analysis", "Startup Analysis", "Investor Analysis", "Location Analysis"],
)


if option == "Overall Analysis":
    over_all_analysis()


if option == "Startup Analysis":
    startup = st.sidebar.selectbox("Select a startup", df["startup"].unique().tolist())

    st.title(f"Startup Analysis: :red[{startup}]")

    # Add your startup analysis code here


if option == "Investor Analysis":
    selected_investor = st.sidebar.selectbox(
        "Select an investor", list(set(set(df["Investors"].str.split(",").sum())))
    )
    btn = st.sidebar.button("Load Investor Details")
    if btn:
        load_investor_details(selected_investor)
    # Add your investor analysis code here


if option == "Location Analysis":
    st.title("Location Analysis")
    st.write("This section provides insights into funding based on location.")
    # Add your location analysis code here
