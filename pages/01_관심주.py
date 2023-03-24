import streamlit as st
from pykrx import stock

st.write('관심주')

chk00=st.sidebar.checkbox('코스피200 보기',value=False)
if chk00:
    티커s=stock.get_index_portfolio_deposit_file('1028')
    st.write(티커s)

    df=stock.get_market_ohlcv('20230324')

    df = df[df.index.isin(티커s)]

    st.write(len(df),'건')
    st.dataframe(df)

