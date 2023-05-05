import streamlit as st
from Codes import Share, GetData


st.text('삼성전자 2022년 재무상태')

df=GetData.DART_재무정보()

# df=df[df['fs_nm']=='연결재무제표']

st.dataframe(df)

