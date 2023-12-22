import streamlit as st
from datetime import date

from Codes import Share, GetData

def 전략보기():
    st.write('심플강력 전략')
    st.write('1. 투자ETFs')
    st.text(' - TQQQ: 50%')
    st.text(' - SCHD: 30%')
    st.text(' - PFIX: 10%')
    st.text(' - TMF: 10%')
    st.write('2. Rebalancing')
    st.text(' - 매월 첫 거래일에 비중을 맞추어 리밸런싱 진행')
    st.text(' - SCHD는 리밸런싱 하지 않는다')
    st.text(' - 200일선 아래에 있는 자산은 50% 매도')
    st.text(' - 140일선이 하락하고 있는 자산은 50% 추가 매도(이동평균선 하락은 전전날과 전날 이평선을 비교하여 판단)')
    st.text(' - 감산에서 2연타를 맞은 자산이 PFIX나 TMF인경우 비중을 0으로 만들고 모두 매도')
    st.text(' - TMF를 모두 매도 했다면 PFIX를 2배의 비중으로 보유')
    st.text(' - PFIX를 모두 매도 했다면 TMF를 2배의 비중으로 보유')
    st.text(' - TQQQ가 감산 2연타를 맞으면 PFIX에 35%의 비중을 더해 준다')
    st.text(' - PFIX를 모두 매도 했는데 TQQQ가 2연타 감산을 맞지 않은 상태면 남은 현금으로 TQQQ를 매수')
    st.write('3. 리밸런싱중 아래의 상황이 발행하면 월중 리밸런싱 진행')
    st.text(' - SCHD를 제외한 모든 자산을 매일 확인')
    st.text(' - 전전일 종가가 120일선 위에 있었는데 전일 종가가 120일선 아래에 형성된 자산은 보유수량 50% 매도')
    st.text(' - 전전일 종가가 200일선 위에 있었는데 전일 종가가 200일선 아래에 형성된 자산은 보유수량 50% 매도')
    st.text(' - 전일 종가 기준 140일선이 상승하다가 감소 했다면 보유 수량의 50% 매도')
    st.text(' - 전일 종가 기준 175일선이 상승하다가 감소 했다면 보유 수량의 50% 매도')
    st.text(' - 매도할 50%의 보유 수량이 4주 이하라면 모두 매도')

    st.text(' - 자 이렇게 되면 금리 상승기와 금리 하락기를 대비하려고 배치해둔 PFIX와 TMF의 비중이 줄어들 수 밖에 없는데요. \n\
    원래 각각 15%였는데 5%씩을 떼어서 배당ETF인 SCHD에 10% 비중을 더 준 것이거든요. \n\
    그러면 금리 상승기, 하락기를 제대로 대비할 수 있을까 걱정이 되죠. \n\
    ​그래서 PFIX와 TMF에 보너스 비중을 줍니다.\n\
    언제?? TQQQ가 2연타 감산을 맞았을 때요.\n\
    TQQQ가 50% 비중인데 2연타 감산을 맞게 되면???\n\
    12.5%비중으로 줄어 들게 되며 37.5%비중이 현금으로 남게 되는데요.\n\
    여기서 35%를 과감히 PFIX나 TMF에 넣어주는 거죠! (완벽한 스위칭!)\n\
    이렇게 되면 TQQQ가 하락하는 장세에서 PFIX나 TMF가 커버를 충분히 쳐줄 수 있게 됩니다!\n\
    그리고 기술주 위주의 TQQQ는 아무래도 금리의 영향을 많이 받기에 금리 상승기를 대비한 PFIX와 반대로 움직이는 경향이 큽니다!\n\
    그래서 PFIX가 2연타 감산을 맞았는데 TQQQ는 2연타 감산을 맞지 않은 상황이라면 남은 현금 비중을 TQQQ에 투자해 공격성을 높였습니다!\n\
    자 그리고 마지막으로 월 중 리밸런싱을 진행합니다.\n\
    사실 월 첫 거래일에만 리밸런싱 하게 되면 월 중에 급락하는 이벤트에 대응할 수가 없죠?\n\
    그래서 4가지 조건을 두어 만족할 때 보유 수량의 50%씩 팔도록 했습니다')
    
    return

def 연방은행주요지표보기():

    st.text('미연방은행 주요지표 보기..!!')
    st.write('[10-Year Treasury Constant Maturity Minus 2-Year Treasury Constant Maturity](https://fred.stlouisfed.org/series/{})'.format('T10Y2Y'))
    st.write('[Continued Claims (Insured Unemployment)(실업수당 청구 건수)](https://fred.stlouisfed.org/series/{})'.format('CCSA'))
    st.write('[ Consumer Price Index for All Urban Consumers: All Items in U.S. City Average](https://fred.stlouisfed.org/series/{})'.format('CPIAUCSL'))

    return

def 주요뉴스보기():
    st.text('주요 뉴스 보기..!!')

    st.write('[9999-99-99(  ): 네이버 많이 본 뉴스](https://finance.naver.com/news/news_list.naver?mode=RANK)')
    st.text('')
    st.write('[2023-03-15(수): 경기 용인에 세계 최대 규모 반도체클러스터 조성](https://m.sedaily.com/NewsView/29N1BNH3JZ#cb)')
    st.write('[2023-03-14(화): 이엔플러스, 사우디아라비아 SIIVC 실사 진행 확인...2차전지 대규모 투자 검토](https://m.sedaily.com/NewsView/29N0V55N2B#cb)')
    st.write('[2023-03-14(화): 가온셀, 사우디 1조4,000억원 규모 투자 기대](http://www.todayenergy.kr/news/articleView.html?idxno=258514)')
    st.write('[2023-03-08(화): 尹정부 첫 수주 "이집트 원전" 법률자문 우선협상자로 율촌 가닥](https://www.ajunews.com/view/20230307122709675)')
    st.write('[2023-03-08(화): 하나기술, 올해 매출 2배 성장 목표..."노르웨이서만 1조 수주 전망"](https://m.newspim.com/news/view/20230304000030)')
    st.write('[2023-03-07(월): 700조 규모 "네옴시티"도 결국은 "물"…수처리 건설사들 노났다](https://biz.newdaily.co.kr/site/data/html/2023/03/06/2023030600073.html)')

    return

def 시장지표보기():

    조회일=date.today()
    시작일=str(Share.get_date(조회일, 20)).replace('-','')  # 조회일로부터 20일전 부터 데이타 가져오기
    종료일=str(조회일).replace('-','')

    df_kospi=GetData.Index_Fundamental_조회(시작일,종료일,'코스피')
    df_kosdaq=GetData.Index_Fundamental_조회(시작일,종료일,'코스닥')

    # col1,col2=st.columns(2)
    # with col1: st.dataframe(df_kospi)
    # with col2: st.dataframe(df_kosdaq)

    col1,col2=st.columns(2)
    with col1:
        st.markdown(f'''##### :orange[... 코스피 ...]''')
        st.markdown('-----')

        subcol1, subcol2=st.beta_columns(2)
        with subcol1:
            날짜1=df_kospi.loc[len(df_kospi)-1, '날짜']
            지수1=df_kospi.loc[len(df_kospi)-1, '종가']
            등락률1=df_kospi.loc[len(df_kospi)-1, '등락률']
            PER1=df_kospi.loc[len(df_kospi)-1, 'PER']
            PBR1=df_kospi.loc[len(df_kospi)-1, 'PBR']

            st.markdown(f'''###### :orange[날짜: {날짜1}]''')
            st.markdown(f'''###### :orange[코스피지수: {지수1}]''')
            st.markdown(f'''###### :orange[등락률: {등락률1}]''')
            st.markdown(f'''###### :orange[PER: {PER1}]''')
            st.markdown(f'''###### :orange[PBR: {PBR1}]''')
        with subcol2:
            날짜2=df_kospi.loc[len(df_kospi)-2, '날짜']
            지수2=df_kospi.loc[len(df_kospi)-2, '종가']
            등락률2=df_kospi.loc[len(df_kospi)-2, '등락률']
            PER2=df_kospi.loc[len(df_kospi)-2, 'PER']
            PBR2=df_kospi.loc[len(df_kospi)-2, 'PBR']

            st.markdown(f'''###### :orange[날짜: {날짜2}]''')
            st.markdown(f'''###### :orange[코스피지수: {지수2}]''')
            st.markdown(f'''###### :orange[등락률: {등락률2}]''')
            st.markdown(f'''###### :orange[PER: {PER2}]''')
            st.markdown(f'''###### :orange[PBR: {PBR2}]''')

    with col2:
        st.markdown(f'''##### :blue[... 코스닥 ...]''')
        st.markdown('-----')

        subcol1, subcol2=st.beta_columns(2)
        with subcol1:
            날짜1=df_kosdaq.loc[len(df_kosdaq)-1, '날짜']
            지수1=df_kosdaq.loc[len(df_kosdaq)-1, '종가']
            등락률1=df_kosdaq.loc[len(df_kosdaq)-1, '등락률']
            PER1=df_kosdaq.loc[len(df_kosdaq)-1, 'PER']
            PBR1=df_kosdaq.loc[len(df_kosdaq)-1, 'PBR']

            st.markdown(f'''###### :blue[날짜: {날짜1}]''')
            st.markdown(f'''###### :blue[코스피지수: {지수1}]''')
            st.markdown(f'''###### :blue[등락률: {등락률1}]''')
            st.markdown(f'''###### :blue[PER: {PER1}]''')
            st.markdown(f'''###### :blue[PBR: {PBR1}]''')
        with subcol2:
            날짜2=df_kosdaq.loc[len(df_kosdaq)-2, '날짜']
            코스피지수2=df_kosdaq.loc[len(df_kosdaq)-2, '종가']
            등락률2=df_kosdaq.loc[len(df_kosdaq)-2, '등락률']
            PER2=df_kosdaq.loc[len(df_kosdaq)-2, 'PER']
            PBR2=df_kosdaq.loc[len(df_kosdaq)-2, 'PBR']

            st.markdown(f'''###### :blue[날짜: {날짜2}]''')
            st.markdown(f'''###### :blue[코스피지수: {지수2}]''')
            st.markdown(f'''###### :blue[등락률: {등락률2}]''')
            st.markdown(f'''###### :blue[PER: {PER2}]''')
            st.markdown(f'''###### :blue[PBR: {PBR2}]''')


    return