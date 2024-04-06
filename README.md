# Penguin Explorer
 This is an interactive web application using Streamlit, aimed at exploring and visualizing the Boston Housing dataset. The application allows users to engage with the data through filters such as average number of rooms and crime rate. It includes interactive charts and map visualizations to uncover trends and insights into the Boston housing market. The app serves as a tool for potential homebuyers, real estate analysts, and students interested in urban planning or economic trends.


## Getting Started

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt 

streamlit run app.py
```

## Lessons Learned
1. The intricacies of Git workflow and the importance of version control for collaborative and individual projects.
2. Mastery of Streamlit's static and dynamic capabilities, learning how to display data and leverage user inputs to create a reactive experience.
3. Deeper understanding of connecting to persistent storage to maintain state across sessions and manage user interactions and data input.
4. Gained insights into state management and how Streamlit's rerun cycle operates in response to user interactions.
5. An appreciation for the balance between static content for instructional purposes and interactive elements for user engagement.


## Questions
1. How can we efficiently manage state in Streamlit when dealing with larger datasets and more complex user interactions?
2. What are the limitations of Streamlit's interactivity, and how can we creatively overcome them?
3. How do we integrate custom CSS for branding and design without compromising the app's performance and maintainability?

## TODO
1. Add User Authentication: To personalize the experience and save user preferences for return visits.
2. Enhance Responsiveness: Optimize the layout and elements for various screen sizes and devices.
3. Expand Data Points: Include more datasets to allow comparative analysis between different regions or time periods.
4. Develop User Guides: Create tutorials or guides within the app to help users understand how to make the most of the available tools and data.