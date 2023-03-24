import streamlit as st
from pykrx import stock
import pandas as pd

st.write('관심주')

chk00=st.sidebar.checkbox('코스피200 보기',value=False)
if chk00:
    종목s=[]
    티커s=stock.get_index_portfolio_deposit_file('1028')
    for 티커 in 티커s:
        종목s.append(stock.get_market_ticker_name(티커))
    st.write(티커s)
    st.write(종목s)

    _df=pd.DataFrame(list(zip(티커s, 종목s)), columns=['티커', '종목'])

    st.dataframe(_df)

    # df=stock.get_market_ohlcv('20230324')

    # df = df[df.index.isin(티커s)]

    # st.write(len(df),'건')
    # st.dataframe(df)

