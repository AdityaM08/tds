import streamlit as st
st.write("TDS MODULE 8")
a=st.number_input("Enter first number")
b=st.number_input("Enter second number")
c=st.number_input("Enter second number") 
if (a >= b) and (a >= c):
   largest = a
elif (b >= a) and (b >= c):
   largest = b
else:
   largest = c
st.write("The largest number is", largest)
st.write("By Aditya Malik")
