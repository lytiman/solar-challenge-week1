import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Solar Irradiance Comparison")
country = st.multiselect("Select countries:", ["Benin","SierraLeone","Togo"], default=["Benin"])
dfs = {c: pd.read_csv(f"notebooks/data/{c.lower().replace(' ','_')}_clean.csv") for c in country}
print("Loaded dataframes:", dfs.keys())
combined = pd.concat([df.assign(country=c) for c,df in dfs.items()])
fig = px.box(combined, x="country", y="GHI", title="GHI by Country")
st.plotly_chart(fig)