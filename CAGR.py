# computing CAGR
# first app using streamlit
# june 2020
# subu sangameswar

import streamlit as st

beginning_balance=65000
ending_balance=175000
number_of_years = 3


beginning_balance = st.sidebar.number_input("What is the beginning balance?", min_value=100.0,  step=100.0)

ending_balance = st.sidebar.number_input("What is the ending balance?", min_value=200.0,  step=100.0)


number_of_years = st.sidebar.slider(
    'number of years',
    1, 10, 5
)

CAGR = ((ending_balance / beginning_balance)**(1/number_of_years) - 1)*100

st.subheader("Compound Growth Rate - CAGR")
md_results = f"The compound growth is **{CAGR:.2f}**%."
st.markdown(md_results)

#st.markdown("# CAGR")
#st.write("CAGR", CAGR)



