import streamlit as st
from Codes import Share, GetData


st.text('스크랩 웹 사이트')

df=GetData.DART_재무정보()

df.sort_values(by='ord',ascending=True,inplace=True)

st.dataframe(df)

