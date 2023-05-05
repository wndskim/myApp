import streamlit as st
from Codes import Share, GetData


st.text('스크랩 웹 사이트')

df=GetData.DART_재무정보()

df=df[df['fd_nm']=='연결재무제표']

st.dataframe(df)

