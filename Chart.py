import streamlit as st
import plotly.graph_objs as go
# from pykrx import stock
# import pandas as pd
# from datetime import date, datetime
# import GetData, Share

def 차트_일봉(df,종목):

    fig = go.Figure(data=[go.Candlestick(x=df['날짜'],
                        open=df["시가"],
                        high=df["고가"],
                        low=df["저가"],
                        close=df["종가"],
                        name='연봉',
                        increasing_line_color='red',
                        increasing_fillcolor='red',
                        decreasing_line_color='blue',
                        decreasing_fillcolor='blue'
                    ),
                        go.Scatter(x=df['날짜'], y=df['sma5'], name='sma5')
                        go.Scatter(x=df['날짜'], y=df['sma10'], name='sma10')
                        go.Scatter(x=df['날짜'], y=df['sma20'], name='sma20')
                        go.Scatter(x=df['날짜'], y=df['sma60'], name='sma60')
                        go.Scatter(x=df['날짜'], y=df['sma120'], name='sma120')
                        go.Scatter(x=df['날짜'], y=df['sma240'], name='sma240')
                        go.Scatter(x=df['날짜'], y=df['sma480'], name='sma480')
            ])

    fig.update_layout(title=종목+' 차트(일)',
                    xaxis_title='날짜',
                    yaxis_title='가격',
                    width=1500,
                    height=700,                     
                    xaxis_rangeslider_visible = False)

    st.plotly_chart(fig)




    # fig = go.Figure()
    # fig.add_trace(go.Scatter(x=df['날짜'], y=df['종가'], name='종가'))
    # fig.add_trace(go.Scatter(x=df['날짜'], y=df['sma5'], name='sma5'))
    # fig.add_trace(go.Scatter(x=df['날짜'], y=df['sma10'], name='sma10'))
    # fig.add_trace(go.Scatter(x=df['날짜'], y=df['sma20'], name='sma20'))
    # fig.add_trace(go.Scatter(x=df['날짜'], y=df['sma60'], name='sma60'))
    # fig.add_trace(go.Scatter(x=df['날짜'], y=df['sma120'], name='sma120'))
    # fig.add_trace(go.Scatter(x=df['날짜'], y=df['sma240'], name='sma240'))
    # fig.add_trace(go.Scatter(x=df['날짜'], y=df['sma480'], name='sma480'))

    # fig.update_layout(title=종목+' 차트(일)',
    #                 xaxis_title='년월',
    #                 yaxis_title='가격',
    #                 width=1500,
    #                 height=700,                      
    #                 # xaxis_rangeslider_visible = False
    #                 )

    # st.plotly_chart(fig)

    return

def 차트_주봉(df,종목):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['날짜'], y=df['종가'], name='종가'))
    fig.add_trace(go.Scatter(x=df['날짜'], y=df['sma5'], name='sma5'))
    fig.add_trace(go.Scatter(x=df['날짜'], y=df['sma10'], name='sma10'))
    fig.add_trace(go.Scatter(x=df['날짜'], y=df['sma20'], name='sma20'))
    fig.add_trace(go.Scatter(x=df['날짜'], y=df['sma60'], name='sma60'))
    fig.add_trace(go.Scatter(x=df['날짜'], y=df['sma120'], name='sma120'))

    fig.update_layout(title=종목+' 차트(주)',
                    xaxis_title='년월',
                    yaxis_title='가격',
                    width=1500,
                    height=700,                      
                    # xaxis_rangeslider_visible = False
                    )

    st.plotly_chart(fig)

    return

def 차트_월봉(df,종목):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['날짜'], y=df['종가'], name='종가'))
    fig.add_trace(go.Scatter(x=df['날짜'], y=df['sma5'], name='sma5'))
    fig.add_trace(go.Scatter(x=df['날짜'], y=df['sma10'], name='sma10'))
    fig.add_trace(go.Scatter(x=df['날짜'], y=df['sma20'], name='sma20'))
    fig.add_trace(go.Scatter(x=df['날짜'], y=df['sma60'], name='sma60'))

    fig.update_layout(title=종목+' 차트(월)',
                    xaxis_title='년월',
                    yaxis_title='가격',
                    width=1500,
                    height=700,                      
                    # xaxis_rangeslider_visible = False
                    )

    st.plotly_chart(fig)

    return