import streamlit as st
st.title("ATTENDANCE")
t=st.number_input("Enter total number of classes",min_value=1)
p=st.number_input("Enter number of classes present",min_value=1)
st.subheader("Present Attendance")
a=round((p/t)*100,2)
st.write(a)
st.subheader("BUNK Meter")
b=st.number_input("Enter number of bunks",min_value=0)
st.subheader("Attendance after Bunking")
t+=b
a=round((p/t)*100,2)
st.write(a)
st.subheader("Enter target attendance")
tg=st.number_input("   ",min_value=0)
x=0
while round(((p+x)/(t+x)*100),2)<tg:
	x+=1
st.write("Attend ",x," more Classes!!😿")
