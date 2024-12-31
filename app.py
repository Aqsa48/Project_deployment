import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder
from sklearn.model_selection import train_test_split

# Title
st.title("Dataset Preprocessing App")

# Sidebar for options
st.sidebar.title("Preprocessing Options")
st.sidebar.subheader("Upload your dataset")

# File upload
uploaded_file = st.sidebar.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file:
    # Debugging: Display file type and size
    st.sidebar.write(f"File uploaded: {uploaded_file.name} ({uploaded_file.size} bytes)")

    # Read the CSV file
    try:
        df = pd.read_csv(uploaded_file)
        st.write("### Uploaded Dataset Preview")
        st.write(df.head())  # Show first few rows of the dataset
    except Exception as e:
        st.sidebar.error(f"Error reading the file: {e}")
        st.stop()  # Stop further execution in case of an error

    # Debugging: Check if DataFrame is loaded correctly
    if df.empty:
        st.sidebar.warning("The dataset is empty.")
    else:
        st.sidebar.success(f"Dataset loaded with {df.shape[0]} rows and {df.shape[1]} columns.")

    # Missing value handling
    st.sidebar.subheader("Handle Missing Values")
    missing_option = st.sidebar.selectbox(
        "Choose a method for missing values",
        ["None", "Drop Rows", "Fill with Mean", "Fill with Median", "Fill with Mode"]
    )

    if missing_option == "Drop Rows":
        df = df.dropna()
    elif missing_option == "Fill with Mean":
        df = df.fillna(df.mean())
    elif missing_option == "Fill with Median":
        df = df.fillna(df.median())
    elif missing_option == "Fill with Mode":
        df = df.fillna(df.mode().iloc[0])

    # Debugging: Show processed dataset after missing value handling
    st.write("### Dataset after Handling Missing Values")
    st.write(df.head())

    # Check for missing values
    st.sidebar.subheader("Check Missing Values")
    if st.sidebar.button("Show Missing Values"):
        missing_values = df.isnull().sum()
        st.write("### Missing Values in Columns")
        st.write(missing_values[missing_values > 0])  # Only show columns with missing values

    # Convert categorical columns to numeric
    st.sidebar.subheader("Convert Categorical to Numeric")
    cat_cols = df.select_dtypes(include='object').columns.tolist()
    encoding_method = st.sidebar.selectbox("Encoding Method", ["Label Encoding", "One-Hot Encoding"])

    if encoding_method == "Label Encoding" and cat_cols:
        le = LabelEncoder()
        for col in cat_cols:
            df[col] = le.fit_transform(df[col])
        st.write("### Dataset after Label Encoding")
        st.write(df.head())

    elif encoding_method == "One-Hot Encoding" and cat_cols:
        df = pd.get_dummies(df, columns=cat_cols)
        st.write("### Dataset after One-Hot Encoding")
        st.write(df.head())

    # Normalize/Standardize Data
    st.sidebar.subheader("Normalize/Standardize Data")
    norm_cols = st.sidebar.multiselect("Select Columns", df.select_dtypes(include=np.number).columns)

    if st.sidebar.button("Normalize"):
        if norm_cols:
            scaler = StandardScaler()
            df[norm_cols] = scaler.fit_transform(df[norm_cols])
            st.write("### Dataset after Normalization")
            st.write(df.head())
        else:
            st.warning("Select columns to normalize.")

    # Data Splitting
    st.sidebar.subheader("Split Dataset")
    test_size = st.sidebar.slider("Test Set Size (%)", min_value=10, max_value=50, value=20)
    if st.sidebar.button("Split Dataset"):
        if df.shape[0] > 1:  # Ensure there are enough rows to split
            train, test = train_test_split(df, test_size=test_size/100, random_state=42)
            st.write("### Training Set", train)
            st.write("### Test Set", test)
        else:
            st.warning("Dataset is too small to split.")

    # Visualization
    st.sidebar.subheader("Visualizations")
    if st.sidebar.checkbox("Show Correlation Heatmap"):
        st.write("### Correlation Heatmap")
        # Handle correlation calculation on numeric columns only
        corr_df = df.select_dtypes(include=np.number)
        plt.figure(figsize=(10, 6))
        sns.heatmap(corr_df.corr(), annot=True, cmap="coolwarm")
        st.pyplot(plt)

    # Download Preprocessed Dataset
    st.sidebar.subheader("Download")
    st.sidebar.markdown("### Download Preprocessed Dataset")
    csv = df.to_csv(index=False)
    st.sidebar.download_button("Download CSV", csv, "processed_data.csv", "text/csv")
else:
    st.write("Please upload a CSV file to begin.")
