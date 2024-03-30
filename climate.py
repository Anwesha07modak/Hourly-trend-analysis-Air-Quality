import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
@st.cache_data
def load_data():
    df = pd.read_csv("delhiaqi.csv")  # Replace "your_dataset.csv" with the path to your dataset
    return df

df = load_data()

# Perform data preprocessing if needed (e.g., convert date column to datetime)
df['date'] = pd.to_datetime(df['date'])

# Perform trend analysis
# For example, you can calculate the mean values for each parameter across all dates
trends = df.groupby(df['date'].dt.hour).mean()  # Group by hour and calculate mean

# Create Streamlit app
st.title('Air Quality Trend Analysis')
st.write('## Hourly Trends')

# Plot trends
fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(data=trends, ax=ax, markers=True, dashes=False)
plt.xlabel('Hour of the Day')
plt.ylabel('Average Value')
plt.title('Hourly Trends for Air Quality Parameters')
st.pyplot(fig)
