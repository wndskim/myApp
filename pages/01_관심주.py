import streamlit as st
from pykrx import stock
import pandas as pd
from datetime import date, datetime
import GetData, Share, Chart
import plotly.graph_objs as go

st.write('관심주')

종료일=date.today()
시작일=Share.get_date(종료일,260*3) #3년전 날짜
종료일=종료일.strftime('%Y%m%d')

chk00=st.sidebar.checkbox('코스피200 보기',value=False)
if chk00:
    종목s=[]
    티커s=stock.get_index_portfolio_deposit_file('1028')
    for 티커 in 티커s:
        종목s.append(stock.get_market_ticker_name(티커))
    _df1=pd.DataFrame(list(zip(티커s, 종목s)), columns=['티커', '종목'])
    _dict=dict(zip(종목s,티커s))

    col1,col2,col3=st.columns([1,5,3])
    with col1:
        조회일=st.date_input('조회일', date.today())
        조회일=str(조회일).replace('-','')
        container=st.container()
    with col2:
        _df2=GetData.load_from_pykrx_해당일전체(조회일)
        _df2=_df2[_df2.index.isin(티커s)]

        df=pd.merge(_df1, _df2, on='티커')
        df.sort_values(by='등락률', ascending=False, inplace=True)

        df.reset_index(inplace=True)
        df.drop('index', axis=1, inplace=True)
        _종목s=df.종목.tolist()

        st.write('코스피200',len(df),'건')
        st.dataframe(df)

        _종목=container.selectbox('선택', _종목s)
        _티커=_dict[_종목]

    with col3:
        # _종목=st.selectbox('선택', _종목s)
        # _티커=_dict[_종목]
        # st.write(_종목, _티커)

        Share.참조링크보기(_티커,_종목)

    # 개별종목 일/주/월 차트 그리기
    df_개별종목=GetData.load_from_pykrx_개별종목(시작일,종료일,_티커)
    df_w=df_개별종목.resample('W').agg({'시가':'first','고가':'max','저가':'min','종가':'last','거래량':'sum','거래대금':'sum'})
    df_m=df_개별종목.resample('M',closed='right',label='right').agg({'시가':'first','고가':'max','저가':'min','종가':'last','거래량':'sum','거래대금':'sum'})

    df_개별종목=GetData.set_indicator(df_개별종목)
    df_개별종목.reset_index(inplace=True)
    df_w=GetData.set_indicator(df_w)
    df_w.reset_index(inplace=True)
    df_m=GetData.set_indicator(df_m)
    df_m.reset_index(inplace=True)

    Chart.차트_일봉(df_개별종목,_종목)
    Chart.차트_주봉(df_w,_종목)
    Chart.차트_월봉(df_m,_종목)








