import streamlit as st
import pandas as pd
import plotly.express as px

# Title
st.title("Interactive Data Explorer with Plotly and Streamlit")

# Upload Excel file
uploaded_file = st.file_uploader("Upload Excel File", type=["xlsx"])
if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    st.success("File uploaded successfully!")

    # Display raw data
    if st.checkbox("Show raw data"):
        st.write(df)

    # Select columns for plotting
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
    if len(numeric_columns) < 2:
        st.warning("Need at least two numeric columns for plotting.")
    else:
        x_axis = st.selectbox("Select X-axis", options=numeric_columns)
        y_axis = st.selectbox("Select Y-axis", options=numeric_columns, index=1 if len(numeric_columns) > 1 else 0)

        # Plot
        fig = px.line(df, x=x_axis, y=y_axis, title=f"{y_axis} vs {x_axis}")
        st.plotly_chart(fig)
else:
    st.info("Please upload an Excel file to begin.")





 