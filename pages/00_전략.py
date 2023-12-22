import streamlit as st
from Codes import Display,GetData

chk00=st.checkbox('전략 내용 보기')
chk01=st.checkbox('전략 상태 확인')
if chk00: Display.전략보기()

df=GetData.load_from_yfinance()

st.dataframe(df)
# if chk01: Display.전략상태확인()

