
import streamlit as st
import pandas as pd

# Load the Excel file and its sheets
file_path = '120924_QAM_Magazines Content Description v.2 - Copy.xlsx'
xls = pd.ExcelFile(file_path)

# Display a title for the app
st.title('Interactive Content Viewer')

# Display the list of available sheets
sheet_name = st.selectbox('Select the sheet you want to explore:', xls.sheet_names)

# Load the selected sheet into a DataFrame
df = pd.read_excel(file_path, sheet_name=sheet_name)

# Display available columns except for Content Description
available_columns = [col for col in df.columns if 'Content Description' not in col]
selected_column = st.selectbox('Choose a column to filter by:', available_columns)

# Show unique values from the selected column
unique_values = df[selected_column].dropna().unique()
selected_value = st.selectbox('Select a value:', unique_values)

# Filter and display the content from the Content Description column
filtered_content = df[df[selected_column] == selected_value]['Content Description'].dropna()

st.write('### Content Description:')
st.write(filtered_content if not filtered_content.empty else 'No content available for this selection.')
