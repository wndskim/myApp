# import streamlit as st
# from pykrx import stock
# import pandas as pd
# from datetime import date, datetime
# import GetData, Share
import plotly.graph_objs as go

def 차트_일봉(df,종목):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['날짜'], y=df['종가'], name='종가'))
    fig.add_trace(go.Scatter(x=df['날짜'], y=df['sma5'], name='sma5'))
    fig.add_trace(go.Scatter(x=df['날짜'], y=df['sma10'], name='sma10'))
    fig.add_trace(go.Scatter(x=df['날짜'], y=df['sma20'], name='sma20'))
    fig.add_trace(go.Scatter(x=df['날짜'], y=df['sma60'], name='sma60'))
    fig.add_trace(go.Scatter(x=df['날짜'], y=df['sma120'], name='sma120'))
    fig.add_trace(go.Scatter(x=df['날짜'], y=df['sma240'], name='sma240'))
    fig.add_trace(go.Scatter(x=df['날짜'], y=df['sma480'], name='sma480'))

    fig.update_layout(title=종목+' 차트(일)',
                    xaxis_title='년월',
                    yaxis_title='가격',
                    width=1500,
                    height=700,                      
                    # xaxis_rangeslider_visible = False
                    )

    st.plotly_chart(fig)

    return