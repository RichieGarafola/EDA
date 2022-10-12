# Initialize Libraries
import pandas as pd
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

# Hide streamlit features
hide_streamlit_style = """
                    <style>
                    #MainMenu {visibility: hidden;}
                    footer {visibility: hidden;}
                    </style>
                    """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Title
st.title("Exploratory Data Analysis Application")

########################
# Sidebar
#######################

# Navigation menu
menu = ["EDA", "About"]
choice = st.sidebar.selectbox("Menu", menu)

# Contact Information
st.sidebar.write("Email : RichieGarafola@hotmail.com ")
col1, col2 = st.columns(2)
with col1:
    st.sidebar.write("[LinkedIn](https://www.linkedin.com/in/RichieGarafola)")
with col2:
    st.sidebar.write("[GitHub](https://github.com/RichieGarafola)")
    
########################
# Exploratory Data Analysis 
########################
if choice == "EDA":
    st.write("Upload your file in csv format and perform Exploratory Data Analysis")
    # st.write("Make sure your columns have correct data types before uploading.")
    st.subheader("Perform Exploratory Data Analysis with Pandas Profiling Library")
    # upload csv file
    data_file= st.file_uploader("Upload csv file", type=["csv"])
    if st.button("Analyze"):
        if data_file is not None:
            # read in csv as a function to use the st.cache feature 
            @st.cache
            def load_csv():
                csv = pd.read_csv(data_file)
                return csv
            df = load_csv()
            # Pandas Profiling Report
            pr = ProfileReport(df, explorative=True)
            st.header('*User Input DataFrame*')
            st.write(df)
            st.write('---')
            st.header('*Exploratory Data Analysis Report Using Pandas Profiling*')
            # print the report on the dashboard
            st_profile_report(pr)
        else:
            st.success("Upload file")
    else:
        pass
        # st.write("Check similarity of Resume and Job Description")
elif choice == "About":
    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.image("./Images/profile-pic.png", width=230)

    with col2:
        st.write("This interactive application is an Exploratory Data Analysis tool, developed by Richie Garafola using the Streamlit Framework and the powerful pandas-profiling library.")
        st.write("If you're on LinkedIn and want to connect, just click on the link in the sidebar and request to connect. Please feel free to email me as well!")
        st.write("If you are interested in seeing more of my work please view my GitHub.")
        st.header(":mailbox: Get In Touch With Me!")

        contact_form = """
        <form action="https://formsubmit.co/8c1144f613c50b43e7ddf63b49e40672" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="your name" required>
            <input type="email" name="email" placeholder="your email" required>
            <textarea name="message" placeholder="Leave your comments"></textarea>
            <button type="submit">Send</button>
        </form>
        """
        st.markdown(contact_form, unsafe_allow_html = True)
        # Use local CSS File
        def local_css(file_name):
            with open(file_name) as f:
                st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)