import streamlit as st
import os
from Codes import GetData, Share, Chart

st.write('시장상황 확인')
st.write(os.getenv("PATH"))


조회일=st.sidebar.date_input('조회일')
GetData(조회일)


