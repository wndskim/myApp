import streamlit as st
from pykrx import stock

@st.cache
def load_from_prx_해당일전체(조회일):
    return stock.get_market_ohlcv(조회일)

def Index_Fundamental_조회(시작일, 종료일, 마켓):
    if 마켓=='코스피': market='1001'
    else: market='2001' # 코스닥
    df=stock.get_index_fundamental(시작일, 종료일, market)
    df.drop(['선행PER'], inplace=True, axis=1)
    df.reset_index(inplace=True)
    df.sort_values(by='날짜',ascending=False,inplace=True)
    df['날짜']=df['날짜'].dt.strftime('%Y-%m-%d')
    df['종가'] = df['종가'].map('{:,.2f}'.format)
    df['등락률'] = df['등락률'].map('{:,.2f}'.format)
    df['PER'] = df['PER'].map('{:,.2f}'.format)
    df['PBR'] = df['PBR'].map('{:,.2f}'.format)
    df['배당수익률'] = df['배당수익률'].map('{:,.2f}'.format)
    return df