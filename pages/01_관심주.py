import streamlit as st
from pykrx import stock

st.write('관심주')

chk00=st.sidebar.checkbox('코스피200 보기',value=False)
if chk00:
    티커s=stock.get_index_portfolio_deposit_file('1028')
    st.write(티커s)

