# Project_deployment

# Dataset Preprocessing with Streamlit

This project is a Streamlit-based web application that provides a simple and interactive interface for preprocessing datasets in CSV format. The app enables users to perform common data preprocessing tasks, such as handling missing values, converting categorical variables to numeric values, normalizing or standardizing data, splitting datasets into training and testing sets, and visualizing correlations through heatmaps.

## Features

- **Handle Missing Values**: Choose to drop rows with missing values or fill them using the mean, median, or mode of the respective columns.
- **Categorical to Numeric Conversion**: Convert categorical columns to numeric using Label Encoding or One-Hot Encoding.
- **Data Normalization and Standardization**: Normalize or standardize numerical columns to ensure they fit within an optimal range for machine learning models.
- **Train-Test Split**: Split the dataset into training and testing sets for machine learning model evaluation.
- **Correlation Heatmap**: Visualize the correlation between numerical features in the dataset with a heatmap.
- **Markdown Guide**: Download a detailed markdown guide explaining each preprocessing step.

## Installation

### 1. Clone the repository:
```bash
git clone https://github.com/yourusername/streamlit-data-preprocessing.git
cd streamlit-data-preprocessing
```
## 2. Install Dependencies

Before running the application, you need to install the required dependencies. Follow these steps:

### 2.1. Create a Virtual Environment (Optional but Recommended)
To keep your project dependencies isolated, it's recommended to create a virtual environment. You can do this using `venv` (Python's built-in module) or a tool like `conda` if you're using Anaconda.


### 2.2. Install Required Python Packages
Once the virtual environment is activated, install the necessary dependencies from the `requirements.txt` file by running the following command:

```bash
pip install -r requirements.txt
```
## 3. Run the Application

Once the dependencies are installed, you can run the Streamlit application on your local machine. To do so, follow these steps:

### 3.1. Run Streamlit

Execute the following command in your terminal:

```bash
streamlit run app.py
```

### 3.2. Interact with the App

- **Upload your CSV file**: 
    - Use the file uploader in the Streamlit interface to upload your dataset.
    - Once the file is uploaded, the app will display the contents of the CSV file for preview.

- **Perform Data Preprocessing**: 
    - The app allows you to perform several preprocessing tasks:
        - **Handle Missing Values**: Choose to drop rows with missing values or fill them using strategies like mean, median, or mode.
        - **Encode Categorical Variables**: Convert categorical columns into numeric values using techniques such as Label Encoding or One-Hot Encoding.
        - **Normalize or Standardize Data**: You can scale your numerical columns using normalization (Min-Max scaling) or standardization (Z-score scaling).
        - **Split Data**: The app provides an option to split the dataset into training and testing sets for machine learning model training and evaluation.

- **Visualize Correlation**: 
    - You can visualize the correlation between numerical columns in your dataset using a heatmap, which helps in understanding relationships between features.
    - The heatmap will display the correlation coefficients, making it easier to identify strong positive or negative relationships between variables.

![Deploy](https://raw.githubusercontent.com/Aqsa48/Project_deployment/refs/heads/main/images/working1.png)





