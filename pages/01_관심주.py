import streamlit as st
from pykrx import stock
import pandas as pd
from datetime import date, datetime
import GetData, Share

import plotly.graph_objs as go

st.write('관심주')


종료일=date.today()
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
        _dict=dict(zip(종목s,티커s))
        _df2=GetData.load_from_pykrx_해당일전체(조회일)
        _df2=_df2[_df2.index.isin(티커s)]

        df=pd.merge(_df1, _df2, on='티커')
        df.sort_values(by='등락률', ascending=False, inplace=True)

        df.reset_index(inplace=True)
        df.drop('index', axis=1, inplace=True)

        st.write('코스피200',len(df),'건')
        st.dataframe(df)

        종목s=df.종목.tolist()


    종목=container.selectbox('선택', 종목s)
    _티커=_dict[종목]

    df_개별종목=GetData.load_from_pykrx_개별종목(시작일,종료일,_티커,)
    df_개별종목=GetData.set_indicator(df_개별종목)

    st.write(종목, _dict[종목],_티커)
    # st.dataframe(df_개별종목)


    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df_개별종목['날짜'], y=df_개별종목['종가'], name=종목+' stock price'))
    fig.add_trace(go.Scatter(x=df_개별종목['날짜'], y=df_개별종목['sma5'], name='sma5'))
    fig.add_trace(go.Scatter(x=df_개별종목['날짜'], y=df_개별종목['sma10'], name='sma10'))
    fig.add_trace(go.Scatter(x=df_개별종목['날짜'], y=df_개별종목['sma20'], name='sma20'))
    fig.add_trace(go.Scatter(x=df_개별종목['날짜'], y=df_개별종목['sma60'], name='sma60'))
    fig.add_trace(go.Scatter(x=df_개별종목['날짜'], y=df_개별종목['sma120'], name='sma120'))
    fig.add_trace(go.Scatter(x=df_개별종목['날짜'], y=df_개별종목['sma240'], name='sma240'))
    fig.add_trace(go.Scatter(x=df_개별종목['날짜'], y=df_개별종목['sma480'], name='sma480'))

    fig.update_layout(title=종목+' 차트',
                    xaxis_title='년월',
                    yaxis_title='가격',
                    width=1500,
                    height=700,                      
                    # xaxis_rangeslider_visible = False
                    )

    st.plotly_chart(fig)
    # fig.show()





