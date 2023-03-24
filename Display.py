import streamlit as st
from datetime import date

import Share, GetData


def 연방은행주요지표보기():

    st.text('미연방은행 주요지표 보기..!!')
    st.write('[10-Year Treasury Constant Maturity Minus 2-Year Treasury Constant Maturity](https://fred.stlouisfed.org/series/{})'.format('T10Y2Y'))
    st.write('[Continued Claims (Insured Unemployment)(실업수당 청구 건수)](https://fred.stlouisfed.org/series/{})'.format('CCSA'))
    st.write('[ Consumer Price Index for All Urban Consumers: All Items in U.S. City Average](https://fred.stlouisfed.org/series/{})'.format('CPIAUCSL'))

    return

def 주요뉴스보기():
    st.text('주요 뉴스 보기..!!')
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
        st.text('...코스피...')
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
        st.text('...코스닥...')
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