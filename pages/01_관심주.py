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
    _df1=pd.DataFrame(list(zip(티커s, 종목s)), columns=['티커', '종목'])

    st.dataframe(_df1)

    _df2=stock.get_market_ohlcv('20230324')
    _df2=_df2[_df2.index.isin(티커s)]

    df=pd.merge(_df1, _df2, on='티커')
    df.sort_values(by=등락률, ascending=False, inplace=True)




    st.write(len(df),'건')
    st.dataframe(df)

