import pickle
import streamlit as st
import numpy as np

st.header("Club Recommandation System Using ML")

model = pickle.load(open('artifacts/model.pkl', 'rb'))



#to run the file streamlit run app.py