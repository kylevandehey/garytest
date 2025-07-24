import streamlit as st
import pandas as pd

st.title("P/L by Day of Week")

# File uploader accepts only CSVs
uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])
if uploaded_file is not None:
    # Read CSV, expecting columns "Date" and "P/L"
    df = pd.read_csv(uploaded_file, parse_dates=['Date'])
    
    # Add a weekday name column
    df['Weekday'] = df['Date'].dt.day_name()
    
    # Define weekday order
    order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    # Sum P/L per weekday and reindex to ensure consistent order
    pl_by_day = df.groupby('Weekday')['P/L'].sum().reindex(order).fillna(0)

    # Display bar chart
    st.write("### Total P/L by Day of Week")
    st.bar_chart(pl_by_day)
