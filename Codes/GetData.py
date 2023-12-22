import streamlit as st
from pykrx import stock
import OpenDartReader
import ta,os
import pandas as pd
import numpy as np
import yfinance as yf

def load_from_yfinance():

    tickers=['SCHD','TQQQ','TMF','PFIX']
    for i,ticker in enumerate(tickers):
        df=yf.download(ticker,start='2013-01-01',end='2023-12-20')

        st.dataframe(df)

        df['Date']=df['Date'].dt.strftime('%Y-%m-%d')


        df['sma120']=ta.trend.sma_indicator(df.Close, window=120)
        df['sma140']=ta.trend.sma_indicator(df.Close, window=140)
        df['sma175']=ta.trend.sma_indicator(df.Close, window=175)
        df['sma200']=ta.trend.sma_indicator(df.Close, window=200)


        # 200일선 아래 있는가 확인
        df['아래_200일선']=np.where(df.sma200 > df.Close, 1, 0)

        # 140일선 하락중인가 확인(전전날과 전날기준으로 확인)
        df['전140']=df.sma140.shift(1)
        df['전전140']=df.sma140.shift(2)
        df['하락_104일선']=np.where(df.전140 < df.전전140, 1, 0)

        st.text(ticker)
        st.dataframe(df)


    return df




def DART_재무정보(종목):
    API_KEY_DART=os.getenv("API_KEY_DART")
    dart=OpenDartReader(API_KEY_DART)
    df=pd.DataFrame(dart.finstate(종목, 2022, reprt_code='11011')) # 1분기=>11013, 반기=>11012, 3분기=>11014, 사업보고서=>11011
    # df=pd.DataFrame(dart.finstate_all('삼성전자', 2022)) # 1분기=>11013, 반기=>11012, 3분기=>11014, 사업보고서=>11011
    if len(df)<1: st.text('재무정보 없음..!!'); return
    df.ord=df.ord.astype(int)
    df.sort_values(by='ord',ascending=True,inplace=True)
    return df

def 금감원_공시내역_보기(조회일):
    API_KEY_DART=os.getenv("API_KEY_DART")
    dart=OpenDartReader(API_KEY_DART)
    # 금일 금강원 공시 내역
    조회일=조회일.strftime('%Y%m%d')
    df=dart.list(start=조회일, end=조회일, final=False)
    if len(df)<1: st.text('금일 공시내역 없음..!!'); return

    df['날짜']=df['rcept_dt']
    df['티커']=df['stock_code']
    df['종목명']=df['corp_name']
    df['공시내용']=df['report_nm']

    df=df.drop(['corp_code','corp_name','stock_code','corp_cls','report_nm','rcept_no','rcept_dt'], axis=1)
    df = df.reindex(columns = ['날짜','티커','종목명','공시내용'])

    st.markdown('-----')
    st.text('금일 금감원 공시 건수:'+str(len(df))+'건')
    st.dataframe(df)
    return

# @st.cache_resource
def load_from_pykrx_해당일전체(조회일):
    return stock.get_market_ohlcv(조회일)

# @st.cache
def load_from_pykrx_개별종목(시작일,종료일,티커):
    df=stock.get_market_ohlcv(시작일,종료일,티커,'d',adjusted=False)
    df['변동액']=df['종가'].diff()
    df['등락률']=df['종가'].pct_change()
    df.dropna(inplace=True)
    # df.reset_index(inplace=True)
    # df['날짜']=df['날짜'].dt.strftime('%Y-%m-%d')
    # df.index=df.index.strftime('%Y-%m-%d')
    df['변동액']=df['변동액'].astype(int)
    return df

# @st.cache_resource
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

def set_indicator(data):
    data['등락']=data.종가.diff(periods=1)
    data['등락률']=data.종가.pct_change(periods=1)*100
    data['Low52']=data.저가.rolling(min_periods=1, window=262, center=False).min()
    data['High52']=data.고가.rolling(min_periods=1, window=262, center=False).max()
    data['Mid52']=(data['High52']+data['Low52'])/2
    data['sma5']=ta.trend.sma_indicator(data.종가, window=5)
    data['sma10']=ta.trend.sma_indicator(data.종가, window=10)
    data['sma20']=ta.trend.sma_indicator(data.종가, window=20)
    data['sma60']=ta.trend.sma_indicator(data.종가, window=60)
    data['sma120']=ta.trend.sma_indicator(data.종가, window=120)
    data['sma150']=ta.trend.sma_indicator(data.종가, window=150)
    data['sma240']=ta.trend.sma_indicator(data.종가, window=240)
    data['sma480']=ta.trend.sma_indicator(data.종가, window=480)
    data['거래량20평균']=ta.trend.sma_indicator(data.거래량, window=20)
    data['거래대금20평균']=ta.trend.sma_indicator(data.거래대금, window=20)

    data['거래량20대비']=data['거래량']/data['거래량20평균']
    data['거래대금20대비']=data['거래대금']/data['거래대금20평균']
    data['diff5120']=data['sma5']/data['sma120']*100
    data['diff10120']=data['sma10']/data['sma120']*100
    data['diff20120']=data['sma20']/data['sma120']*100
    data['diff60120']=data['sma60']/data['sma120']*100
    
    # upperband, middleband, lowerband = talib.BBANDS(data.종가, timeperiod=5, nbdevup=2, nbdevdn=2, matype=0)
    # data['bb_upper']=upperband
    # data['bb_middle']=middleband
    # data['bb_lower']=lowerband
    # # Momentum Indocatio Functions
    # macd, macdsignal, macdhist = talib.MACD(data.종가, fastperiod=12, slowperiod=26, signalperiod=9)
    # data['macd']=macd
    # data['macdsignal']=macdsignal
    # data['macdhist']=macdhist
    # data['rsi']=talib.RSI(data.종가, timeperiod=10)
    # slowk, slowd = talib.STOCH(data.고가, data.저가, data.종가, fastk_period=5, slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0)
    # data['slowk']=slowk
    # data['slowd']=slowd
    # # Volatility Indicator Functions
    # data['atr']=talib.ATR(data.고가, data.저가, data.종가, timeperiod=14)
    # # # Volume indicator Functions
    # # data['adosc']=talib.ADOSC(data.고가, data.저가, data.종가, data.Volume, fastperiod=3, s저가period=10)

    return data