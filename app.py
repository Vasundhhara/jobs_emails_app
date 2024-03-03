import streamlit as st
import pandas as pd 
import numpy as np 
import requests




st.title('Hushh-emails')


gmail_query= st.text_input("Enter your Gmail Query")

if 'clicked' not in st.session_state:
     st.session_state.clicked = False

def login_button():
        requests.get(url= "http://127.0.0.1:8000/login/google")
        st.session_state.clicked=True
        

if st.button('Login using google',on_click=login_button):
        st.success('Login Successful !!')
        st.success('Proceed to download the resumes ...')


if st.session_state.clicked:
          if st.button('Download Resumes'):
                 requests.get(url=f"http://127.0.0.1:8000/download/google?q={gmail_query}")
                
            
#requests.get(url="https://hushh-hushh-jobs.hf.space/login/google")
#requests.get(url=f"https://hushh-hushh-jobs.hf.space/download/google?q={gmail_query}")

