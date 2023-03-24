import streamlit as st
from datetime import date, timedelta

def get_date(기준일, delta):
    return (기준일 - timedelta(days=delta)).strftime("%Y-%m-%d")

조회일=date.today()

st.write(조회일)

시작일=str(get_date(조회일, 20)).replace('-','')  # 조회일로부터 20일전 부터 데이타 가져오기
종료일=str(조회일).replace('-','')

st.write(시작일,종료일)

