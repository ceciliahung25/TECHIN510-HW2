import streamlit as st
import pandas as pd
import plotly.express as px

# Streamlit page configuration
st.set_page_config(
    page_title="Boston Housing Explorer", 
    page_icon="🏠", 
    layout="centered",
)

# Page title and introduction
st.title("🏠 Boston Housing Explorer")
st.markdown("""
## Welcome to the Boston Housing Explorer!

This interactive web application provides a comprehensive exploration of the Boston Housing dataset, a collection of data about various housing attributes in the Boston area. The dataset includes information on aspects like crime rates, property tax rates, average number of rooms per dwelling, and more. It's an invaluable tool for understanding housing trends and characteristics in Boston.

### Dataset Overview:
- **CRIM**: Per capita crime rate by town.
- **ZN**: Proportion of residential land zoned for lots over 25,000 sq. ft.
- **INDUS**: Proportion of non-retail business acres per town.
- **CHAS**: Charles River dummy variable (1 if tract bounds river; 0 otherwise).
- **NOX**: Nitrogen oxides concentration (parts per 10 million).
- **RM**: Average number of rooms per dwelling.
- **AGE**: Proportion of owner-occupied units built before 1940.
- **DIS**: Weighted distances to five Boston employment centers.
- **RAD**: Index of accessibility to radial highways.
- **TAX**: Full-value property tax rate per $10,000.
- **PTRATIO**: Pupil-teacher ratio by town.
- **B**: 1000(Bk - 0.63)^2, where Bk is the proportion of Black residents.
- **LSTAT**: Percentage of lower status of the population.
- **MEDV**: Median value of owner-occupied homes in $1000s.

### How to Use This Website:
1. **Adjust the Filters**: Use the sliders and selectors in the sidebar to filter the data based on various housing attributes, such as the average number of rooms, crime rate, or whether the property is close to the Charles River.
2. **View the Data**: After adjusting the filters, observe how the data table in the main section updates in real-time to reflect your selections.
3. **Explore the Visualizations**: Interactive plots will display the relationships between different housing attributes. Hover over the points in the scatter plots for more detailed information.
4. **Gain Insights**: Use this app to uncover trends, patterns, and relationships within the Boston housing market.

### Purpose:
This tool is designed for realtors, data analysts, students, and anyone interested in the Boston real estate market. It aims to provide an intuitive and interactive way to explore and understand the dynamics of housing in Boston.

Enjoy exploring the Boston Housing dataset, and discover the insights that lie within!
""")

# Divider
st.divider()

# Load dataset
df = pd.read_csv("https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv")

# Mock latitude and longitude data (for demonstration)
# In practice, replace these with actual coordinates
df['latitude'] = df['crim'].apply(lambda x: 42.3601 + x/100)
df['longitude'] = df['crim'].apply(lambda x: -71.0589 - x/100)

# Sidebar filters
with st.sidebar:
    # Sidebar widgets - make sure these are indented
    rm_slider = st.slider("🚪 Average Number of Rooms", float(df["rm"].min()), float(df["rm"].max()))
    crim_slider = st.slider("🚨 Per Capita Crime Rate", float(df["crim"].min()), float(df["crim"].max()))
    chas_filter = st.selectbox("Charles River Dummy Variable (1 if tract bounds river; 0 otherwise)", df["chas"].unique(), index=None)

# Data filtering
df = df[df["rm"] > rm_slider]
df = df[df["crim"] < crim_slider]
if chas_filter is not None:
    df = df[df["chas"] == chas_filter]

# Display raw data
with st.expander("RAW Data"):
    st.write(df)  # This line should be indented as it's inside the 'with' block


# Scatter plots
st.header("I. Analysis of Housing Attributes and Median Home Values")
fig = px.scatter(
    df, 
    x="rm", 
    y="medv",
    title="Relationship between Number of Rooms and Median Value"
)
st.plotly_chart(fig)

fig2 = px.scatter(
    df, 
    x="crim", 
    y="medv",
    title="Crime Rate vs. Median Value"
)
st.plotly_chart(fig2)

# Map visualization
st.header("II. Geographical Distribution of Properties")
fig3 = px.scatter_mapbox(
    df, lat="latitude", lon="longitude", 
    hover_name="crim", hover_data=["rm", "medv"],
    color_discrete_sequence=["fuchsia"], zoom=10,
    title="Map of Property Locations"
)
fig3.update_layout(mapbox_style="open-street-map")
st.plotly_chart(fig3)
