import streamlit as st
from utils.helper import load_css

st.set_page_config(
    page_title="AI Salary Intelligence Platform",
    page_icon="💼",
    layout="wide",
)

load_css("assets/styles.css")

st.markdown(
    '<p class="main-title">💼 AI Salary Intelligence Platform</p>',
    unsafe_allow_html=True,
)

st.markdown(
    '<p class="sub-title">AI Powered HR Decision Support System</p>',
    unsafe_allow_html=True,
)

st.divider()

st.header("🚀 Welcome")

st.write("""
This platform helps HR teams analyze employee salary data using Artificial Intelligence.

### Features

- Salary Prediction
- Analytics Dashboard
- Explainable AI
- AI Generated Insights
- PDF Reports
- Interactive Visualizations
""")

st.info("👈 Use the sidebar to navigate through the application.")

st.success("Project setup completed successfully.")