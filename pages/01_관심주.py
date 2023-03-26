import streamlit as st
from pykrx import stock
import pandas as pd
from datetime import date, datetime
import GetData, Share

st.write('관심주')


종료일=datetime.date.today()
시작일=Share.get_date(종료일,260*3) #3년전 날짜
종료일=종료일.strftime('%Y%m%d')

chk00=st.sidebar.checkbox('코스피200 보기',value=False)
if chk00:
    col1,col2=st.columns([1,5])
    with col1:
        조회일=st.date_input('조회일', date.today())
        조회일=str(조회일).replace('-','')
        container=st.container()
    with col2:
        종목s=[]
        티커s=stock.get_index_portfolio_deposit_file('1028')
        for 티커 in 티커s:
            종목s.append(stock.get_market_ticker_name(티커))
        _df1=pd.DataFrame(list(zip(티커s, 종목s)), columns=['티커', '종목'])
        _df2=GetData.load_from_pykrx_해당일전체(조회일)
        _df2=_df2[_df2.index.isin(티커s)]

        df=pd.merge(_df1, _df2, on='티커')
        df.sort_values(by='등락률', ascending=False, inplace=True)

        df.reset_index(inplace=True)
        df.drop('index', axis=1, inplace=True)

        st.write('코스피200',len(df),'건')
        st.dataframe(df)

        종목s=df.종목.tolist()


    _dict=dict(zip(종목s,티커s))
    종목=container.selectbox('선택', 종목s)
    _티커=_dict[종목]

    df_개별종목=GetData.load_from_pykrx_개별종목(시작일,종료일,_티커,)

    st.dataframe(df_개별종목)




    # st.write(종목, _dict[종목])
