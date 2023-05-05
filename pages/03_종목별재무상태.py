import streamlit as st
from Codes import Share, GetData


st.text('종목별 2022년 재무상태')

종목='삼성전자'
df=GetData.DART_재무정보(종목)
st.dataframe(df)

종목='자이에스앤디'
df=GetData.DART_재무정보(종목)
st.dataframe(df)

# df=df[df['fs_nm']=='연결재무제표']


