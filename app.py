import streamlit as st
from utils.helper import load_css

st.set_page_config(
    page_title="AI Salary Intelligence Platform",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

load_css("assets/styles.css")

st.sidebar.title("Navigation")
st.sidebar.success("Select a page from the sidebar.")

st.markdown(
    '<p class="main-title">AI Salary Intelligence Platform</p>',
    unsafe_allow_html=True,
)

st.markdown(
    '<p class="sub-title">AI Powered HR Decision Support System</p>',
    unsafe_allow_html=True,
)

st.divider()

left, right = st.columns([2, 1])

with left:

    st.header("Project Overview")

    st.write("""
The AI Salary Intelligence Platform helps HR teams analyze employee information,
predict salary classes, understand prediction factors, and generate AI-powered insights.

This project demonstrates production-ready machine learning deployment using
Streamlit and Scikit-Learn.
""")

with right:

    st.metric("Project Version", "1.0")
    st.metric("Status", "Development")

st.divider()

st.header("Modules")

col1, col2 = st.columns(2)

with col1:

    st.markdown("""
<div class="feature-card">

### Salary Prediction

Predict employee salary category using Machine Learning.

</div>
""", unsafe_allow_html=True)

    st.markdown("""
<div class="feature-card">

### Dashboard

Interactive HR analytics dashboard.

</div>
""", unsafe_allow_html=True)

    st.markdown("""
<div class="feature-card">

### Explainable AI

Understand why predictions were made.

</div>
""", unsafe_allow_html=True)

with col2:

    st.markdown("""
<div class="feature-card">

### AI Insights

Generate intelligent summaries from employee data.

</div>
""", unsafe_allow_html=True)

    st.markdown("""
<div class="feature-card">

### Reports

Download professional PDF reports.

</div>
""", unsafe_allow_html=True)

    st.markdown("""
<div class="feature-card">

### Docker Ready

Production deployment support.

</div>
""", unsafe_allow_html=True)

st.divider()

st.markdown(
    '<p class="footer">AI Salary Intelligence Platform | Built with Python, Streamlit and Scikit-Learn</p>',
    unsafe_allow_html=True,
)