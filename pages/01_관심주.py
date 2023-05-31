import streamlit as st
import yfinance as yf
from pykrx import stock
import pandas as pd
import os
from datetime import date, datetime
import plotly.graph_objs as go
from Codes import GetData, Share, Chart

st.write('관심주')

종료일=date.today()
시작일=Share.get_date(종료일,260*2) #2년전 날짜
종료일=종료일.strftime('%Y%m%d')

def get_tickers(인덱스):
    return stock.get_index_portfolio_deposit_file(인덱스)

def download_history(티커,시작일):
    return yf.download(티커+'.KS',start=시작일)['Close']

chk00=st.sidebar.checkbox('코스피200 보기',value=False)
if chk00:
    종목s=[]
    티커s=stock.get_index_portfolio_deposit_file('1028')
    for 티커 in 티커s:
        종목s.append(stock.get_market_ticker_name(티커))
    _df1=pd.DataFrame(list(zip(티커s, 종목s)), columns=['티커', '종목'])
    _dict=dict(zip(종목s,티커s))

    col1,col2,col3=st.columns([1,5,5])
    with col1:
        조회일=st.date_input('조회일', date.today())
        조회일=str(조회일).replace('-','')
        container=st.container()
    with col2:
        _df2=GetData.load_from_pykrx_해당일전체(조회일)
        _df2=_df2[_df2.index.isin(티커s)]

        df=pd.merge(_df1, _df2, on='티커')
        df1=df.sort_values(by='등락률', ascending=False)

        df1.reset_index(inplace=True)
        df1.drop('index', axis=1, inplace=True)
        _종목s=df1.종목.tolist()

        st.write('코스피200 상승률순')
        st.dataframe(df1)

        _종목=container.selectbox('선택', _종목s,key='선택종목')
        _티커=_dict[_종목]

    with col3:
        # _종목=st.selectbox('선택', _종목s,key='참조종목')
        # _티커=_dict[_종목]
        # st.write(_종목, _티커)
        df2=df.sort_values(by='등락률', ascending=True)

        df2.reset_index(inplace=True)
        df2.drop('index', axis=1, inplace=True)
        # _종목s=df1.종목.tolist()

        st.write('코스피200 하락률순')
        st.dataframe(df2)        

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

    Chart.차트_일봉(df_개별종목[-150:],_종목)
    Chart.차트_주봉(df_w,_종목)
    Chart.차트_월봉(df_m,_종목)

chk01=st.sidebar.checkbox('인덱스별(업종별) 기간 상승률 순위',value=False)
if chk01:

# def 인덱스별_기간상승률(시작일,종료일):

    인덱스명s=[]
    tickers = stock.get_index_ticker_list(market='KOSPI')
    for ticker in tickers:
        인덱스명s.append(stock.get_index_ticker_name(ticker))
    df_인덱스=pd.DataFrame({'인덱스명':인덱스명s,'인덱스':tickers}).set_index('인덱스명')

    df = stock.get_index_price_change(시작일, 종료일, "KOSPI").sort_values(by='등락률', ascending=False)
    df = df.reset_index()
    df=pd.merge(df,df_인덱스,left_on='지수명',right_on='인덱스명',how='left')

    df_업종=df[~df.지수명.str.contains('코스피 200')]
    df_업종=df_업종[~df_업종.지수명.str.contains('코스피200')]
    df_업종=df_업종[~df_업종.지수명.str.contains('코스피 50')]
    df_업종=df_업종[~df_업종.지수명.str.contains('코스피 100')]
    df_업종=df_업종[~df_업종.지수명.str.contains('코스피 대형주')]
    df_업종=df_업종[~df_업종.지수명.str.contains('코스피 소형주')]
    df_업종=df_업종[~df_업종.지수명.str.contains('코스피 중형주')]


    업종인덱스s=df_업종.인덱스.to_list()
    인덱스별종가s=[];인덱스명s=[]
    for i,업종인덱스 in enumerate(업종인덱스s):
        인덱스별종가s.append(stock.get_index_ohlcv(시작일, 종료일, 업종인덱스, "d")['종가'])
        인덱스명s.append(stock.get_index_ticker_name(업종인덱스))
        print(i,업종인덱스)

    인덱스별가격=pd.concat(인덱스별종가s, axis=1)
    인덱스별가격.columns=인덱스명s
    월인덱스별가격=인덱스별가격.resample('M').last()
    월인덱스별가격.index=월인덱스별가격.index.strftime('%Y-%m-%d')
    월인덱스별등락률=인덱스별가격.pct_change().resample('M').agg(lambda x : (x+1).prod()-1)
    월인덱스별등락률.loc[:, 인덱스명s[0]:인덱스명s[-1]] = 월인덱스별등락률.loc[:, 인덱스명s[0]:인덱스명s[-1]].applymap(lambda x: "{:.4f}".format(x))
    월인덱스별등락률.index=월인덱스별등락률.index.strftime('%Y-%m-%d')

    ret_12_인덱스=월인덱스별등락률.rolling(12).agg(lambda x : (x+1).prod()-1)
    ret_6_인덱스=월인덱스별등락률.rolling(6).agg(lambda x : (x+1).prod()-1)
    ret_3_인덱스=월인덱스별등락률.rolling(3).agg(lambda x : (x+1).prod()-1)
    ret_1_인덱스=월인덱스별등락률.rolling(1).agg(lambda x : (x+1).prod()-1)

    for i in range(1,7):
        df_ret12_인덱스=pd.DataFrame(ret_12_인덱스.iloc[i*-1].nlargest(30))
        df_ret6_인덱스=pd.DataFrame(ret_6_인덱스.iloc[i*-1].nlargest(30))
        df_ret3_인덱스=pd.DataFrame(ret_3_인덱스.iloc[i*-1].nlargest(30))
        df_ret1_인덱스=pd.DataFrame(ret_1_인덱스.iloc[i*-1].nlargest(30))
        df_ret12_인덱스.reset_index(inplace=True)
        df_ret6_인덱스.reset_index(inplace=True)
        df_ret3_인덱스.reset_index(inplace=True)
        df_ret1_인덱스.reset_index(inplace=True)

        df_ret12_인덱스=pd.merge(df_ret12_인덱스,df_인덱스,left_on='index',right_on='인덱스명',how='left')
        df_ret6_인덱스=pd.merge(df_ret6_인덱스,df_인덱스,left_on='index',right_on='인덱스명',how='left')
        df_ret3_인덱스=pd.merge(df_ret3_인덱스,df_인덱스,left_on='index',right_on='인덱스명',how='left')
        df_ret1_인덱스=pd.merge(df_ret1_인덱스,df_인덱스,left_on='index',right_on='인덱스명',how='left')
        df_ret12_인덱스=df_ret12_인덱스.reindex(columns = ['인덱스','index',df_ret12_인덱스.columns[1]]).rename(columns={'index':'인덱스명'})
        df_ret6_인덱스=df_ret6_인덱스.reindex(columns = ['인덱스','index',df_ret6_인덱스.columns[1]]).rename(columns={'index':'인덱스명'})
        df_ret3_인덱스=df_ret3_인덱스.reindex(columns = ['인덱스','index',df_ret3_인덱스.columns[1]]).rename(columns={'index':'인덱스명'})
        df_ret1_인덱스=df_ret1_인덱스.reindex(columns = ['인덱스','index',df_ret1_인덱스.columns[1]]).rename(columns={'index':'인덱스명'})

        col1,col2,col3,col4=st.columns(4)
        with col1:
            st.text('12개월 '+str(df_ret12_인덱스.columns[2]))
            st.dataframe(df_ret12_인덱스)
        with col2:
            st.text('6개월 '+str(df_ret6_인덱스.columns[2]))
            st.dataframe(df_ret6_인덱스)
        with col3:
            st.text('3개월 '+str(df_ret3_인덱스.columns[2]))
            st.dataframe(df_ret3_인덱스)
        with col4:
            st.text('1개월 '+str(df_ret1_인덱스.columns[2]))
            st.dataframe(df_ret1_인덱스)

    ###################
    df_ret1_인덱스=pd.DataFrame(ret_1_인덱스.iloc[-1].nlargest(30))
    순위_인덱스명1=df_ret1_인덱스.index.tolist()
    선택_인덱스명=st.selectbox('선택',순위_인덱스명1)

    선택_인덱스id=df_인덱스.loc[선택_인덱스명].values[0]
    티커s=get_tickers(선택_인덱스id)


    st.write(시작일)

    가격s,종목s=[],[]
    for 티커 in 티커s:
        가격s.append(download_history(티커,시작일))
        # 가격s.append(download_history(티커,시작일[:4]+'-'+시작일[4:6]+'-'+시작일[-2:]))
        종목s.append(stock.get_market_ticker_name(티커))

    종목별가격=pd.concat(가격s, axis=1)
    종목별가격.columns=종목s

    st.dataframe(종목별가격)


    월종목별가격=종목별가격.resample('M').last()
    월종목별가격.index=월종목별가격.index.strftime('%Y-%m-%d')

    월종목별등락률=종목별가격.pct_change().resample('M').agg(lambda x : (x+1).prod()-1)
    월종목별등락률.loc[:, 종목s[0]:종목s[-1]] = 월종목별등락률.loc[:, 종목s[0]:종목s[-1]].applymap(lambda x: "{:.4f}".format(x))
    월종목별등락률.index=월종목별등락률.index.strftime('%Y-%m-%d')

    ret_12_종목=월종목별등락률.rolling(12).agg(lambda x : (x+1).prod()-1)
    ret_6_종목=월종목별등락률.rolling(6).agg(lambda x : (x+1).prod()-1)
    ret_3_종목=월종목별등락률.rolling(3).agg(lambda x : (x+1).prod()-1)
    ret_1_종목=월종목별등락률.rolling(1).agg(lambda x : (x+1).prod()-1)

    for i in range(1,7):
        df_ret12_종목=pd.DataFrame(ret_12_종목.iloc[i*-1].nlargest(30))
        df_ret6_종목=pd.DataFrame(ret_6_종목.iloc[i*-1].nlargest(30))
        df_ret3_종목=pd.DataFrame(ret_3_종목.iloc[i*-1].nlargest(30))
        df_ret1_종목=pd.DataFrame(ret_1_종목.iloc[i*-1].nlargest(30))
        df_ret12_종목.reset_index(inplace=True)
        df_ret6_종목.reset_index(inplace=True)
        df_ret3_종목.reset_index(inplace=True)
        df_ret1_종목.reset_index(inplace=True)

        df_ret12_종목=df_ret12_종목.rename(columns={'index':'종목'})
        df_ret6_종목=df_ret6_종목.rename(columns={'index':'종목'})
        df_ret3_종목=df_ret3_종목.rename(columns={'index':'종목'})
        df_ret1_종목=df_ret1_종목.rename(columns={'index':'종목'})

        col1,col2,col3,col4=st.columns(4)
        with col1:
            st.text('지난 12개월 상승률 순')
            st.dataframe(df_ret12_종목)
        with col2:
            st.text('지난 6개월 상승률 순')
            st.dataframe(df_ret6_종목)
        with col3:
            st.text('지난 3개월 상승률 순')
            st.dataframe(df_ret3_종목)
        with col4:
            st.text('이번달 상승률 순')
            st.dataframe(df_ret1_종목)


    # st.dataframe(월종목별등락률)

    #######################

    # return





