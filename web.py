import streamlit as st 
import pandas as pd 


st.title("Welcome to Python")
dataset = pd.read_csv("AAPL.csv")
st.dataframe(dataset)

st.subheader("Login Form")
name = st.text_input("enter Your Name")
fathername = st.text_input("enter Your father Name")
adr = st.text_area("enter Your address :")
classdata = st.selectbox("enter your class : ",(1,2,3,4,5,6,7,8,9,))



button = st.button("submit")
if button :
    st.markdown(f"""
                Name : {name}
                Father Name : {fathername}
                address : {adr}
                class : {classdata}
                
                """)