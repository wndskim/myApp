import streamlit as st
import os
from Codes import GetData, Share, Chart


st.text(os.getenv('PATH'))

st.write('시장상황 확인')
조회일=st.sidebar.date_input('조회일')
GetData.금감원_공시내역_보기(조회일)


