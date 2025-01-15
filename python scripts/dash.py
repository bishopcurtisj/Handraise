import streamlit as st
from canvas_script import *
from mint_coins import *
from read_events import *
import os
import pandas as pd
import base64

@st.cache_resource
def img_to_base64(img_path):
    with open(img_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

# Function to handle Mint Coins
def handle_mint_coins():
    msg = mint_coins("grades.json")
    st.success(f"Coins minted successfully!\n\n{msg}")

# Function to handle Update Grades
def handle_update_grades(grades):
    read_events()
    update_grades(grades)
    st.success("Grades updated successfully!")
    try:
        os.remove("tokens_burned_events.csv")
    except FileNotFoundError:
        st.warning("No tokens_burned_events.csv found to delete.")

# Function to handle Read Events
def handle_read_events(grades):
    st.write("Reading events...")
    read_events()
    test_grades(grades)
    st.success("Events processed and grades tested!")

# Function to handle file upload
def handle_file_upload(uploaded_file):
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        df.to_csv("student.csv", index=False)
        st.success("File uploaded successfully and saved as student.csv")
        st.dataframe(df)
    else:
        try:
            pd.read_csv("student.csv")
        except FileNotFoundError:
            st.warning("Please upload a valid CSV file or place the student.csv file in the working directory.")

# Streamlit App
def main():

    # Display logos
    logo = img_to_base64("../assets/handraise_logo.jpg")

    st.markdown(f"""
    <img src="data:image/png;base64,{logo}" class="logo-left" width="400">
    """, unsafe_allow_html=True)
    st.title("Handraise GUI")

    # File upload section
    st.header("Upload Student Data")
    uploaded_file = st.file_uploader("Upload your student.csv file", type=["csv"])
    if st.button("Upload File"):
        handle_file_upload(uploaded_file)

    # Load grades data
    grades = prepare_data()

    # Buttons for actions
    st.header("Actions")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button("Mint Coins"):
            handle_mint_coins()
    
    with col2:
        if st.button("Update Grades"):
            handle_update_grades(grades)
    
    with col3:
        if st.button("Read Events"):
            handle_read_events(grades)
    
    with col4:
        if st.button("Exit"):
            try:
                os.remove("grades.json")
                st.success("Grades file removed. Exiting...")
            except FileNotFoundError:
                st.warning("No grades.json found to delete.")
            st.stop()

if __name__ == "__main__":
    main()
