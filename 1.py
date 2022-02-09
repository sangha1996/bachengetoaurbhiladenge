
import streamlit as st
import ttg
a = st.text_input("Enter probability value, (p) :","'p','q'")


st.write(type(a))
st.write(type(['p','q','p and q']))
table=ttg.Truths(['p','q'])
st.table(table.as_pandas())











