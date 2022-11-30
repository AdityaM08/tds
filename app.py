import streamlit as st
st.write("TDS Assignment  8")
p=st.integer_input("Enter first number")
q=st.integer_input("Enter second number")
r=st.integer_input("Enter third number") 
if (p >= q) and (p >= r):
   largest = p
elif (q >= p) and (q >= r):
   largest = q
else:
   largest = r
st.write("The largest number is", largest)
st.write("By Aditya Malik")
