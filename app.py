import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")
st.title("🏘️ Real Estate Price Analysis")


df = pd.read_csv("data/analysis_data.csv")


st.sidebar.header("Filter Properties")
locations = st.sidebar.multiselect("Select Location", df["region_name"].unique(), default=df["region_name"].unique())
house_types = st.sidebar.multiselect("Select House Type", df["house_type"].unique(), default=df["house_type"].unique())


filtered_data = df[
    (df["region_name"].isin(locations)) &
    (df["house_type"].isin(house_types))
]


st.subheader("📋 Filtered Listings")
st.dataframe(filtered_data)


st.subheader("📊 Price Distribution by Region")
fig1 = px.box(
    filtered_data,
    x="region_name",
    y="price",
    color="region_name",
    title="Price Distribution by Region",
    labels={"price": "Price (INR)"}
)
st.plotly_chart(fig1, use_container_width=True)


st.subheader("📈 Price vs Area")
fig2 = px.scatter(
    filtered_data,
    x="area",
    y="price",
    color="region_name",
    size="total_rooms",
    hover_data=["locality_name", "house_type", "construction_status"],
    title="Price vs Area (Size in sqft)"
)
st.plotly_chart(fig2, use_container_width=True)


st.subheader("💰 Value per Sqft by Region")
fig3 = px.bar(
    filtered_data.groupby("region_name")["value_per_sqft"].mean().reset_index(),
    x="region_name",
    y="value_per_sqft",
    title="Average Value per Sqft by Region",
    labels={"value_per_sqft": "Value per Sqft (INR)"}
)
st.plotly_chart(fig3, use_container_width=True)
