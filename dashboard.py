import streamlit as st
import pandas as pd

st.title("P/L by Day of Week")

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])
if uploaded_file is not None:
    # Read CSV without parse_dates, then parse the correct column
    df = pd.read_csv(uploaded_file)

    # Pick the close date column for your P/L
    if 'Date Closed' in df.columns:
        date_col = 'Date Closed'
    else:
        st.error("CSV must contain a 'Date Closed' column.")
        st.stop()

    # Convert to datetime and get weekday names
    df[date_col] = pd.to_datetime(df[date_col])
    df['Weekday'] = df[date_col].dt.day_name()

    # Define week order
    order = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

    # Sum P/L by weekday
    pl_by_day = (
        df
        .groupby('Weekday')['P/L']
        .sum()
        .reindex(order)
        .fillna(0)
    )

    st.write("### Total Realized P/L by Day of Week")
    st.bar_chart(pl_by_day)
