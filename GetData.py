import streamlit as st
from pykrx import stock
import ta

@st.cache
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
    # df['index']=df['index'].dt.strftime('%Y-%m-%d')
    df['변동액']=df['변동액'].astype(int)

    return df

@st.cache
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