import streamlit as st 
import pickle 
import pandas as pd

movies_list=pickle.load(open('movie_recommand_system_model.pkl','rb'))


st.title("Movie Recommander System")
