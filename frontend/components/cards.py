# frontend/components/cards.py

import streamlit as st

def course_card(title, description, progress=0, image_url=None):
    """
    Create a custom card component for displaying course information.

    Args:
    title (str): The title of the course
    description (str): A brief description of the course
    progress (int): The user's progress in the course (0-100)
    image_url (str): URL of the course image (optional)

    Returns:
    None: Displays the card directly in the Streamlit app
    """
    with st.container():
        st.markdown(
            f"""
            <div style="
                border: 1px solid #ddd;
                border-radius: 5px;
                padding: 1rem;
                margin-bottom: 1rem;
            ">
            """, 
            unsafe_allow_html=True
        )
        if image_url:
            st.image(image_url, use_column_width=True)
        st.markdown(f"### {title}")
        st.write(description)
        st.progress(progress / 100.0)
        st.write(f"Progress: {progress}%")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("Start Course", key=f"start_{title}"):
                st.write("Starting course...")
        with col2:
            if st.button("More Info", key=f"info_{title}"):
                st.write("Showing more information...")

        st.markdown("</div>", unsafe_allow_html=True)

def achievement_card(title, description, icon="🏆"):
    """
    Create a custom card component for displaying achievements.

    Args:
    title (str): The title of the achievement
    description (str): A brief description of the achievement
    icon (str): An emoji or icon to represent the achievement

    Returns:
    None: Displays the card directly in the Streamlit app
    """
    with st.container():
        st.markdown(
            f"""
            <div style="
                border: 1px solid #ddd;
                border-radius: 5px;
                padding: 1rem;
                margin-bottom: 1rem;
                background-color: #f0f0f0;
            ">
            """, 
            unsafe_allow_html=True
        )

        st.markdown(f"## {icon} {title}")
        st.write(description)
        st.markdown("</div>", unsafe_allow_html=True)
