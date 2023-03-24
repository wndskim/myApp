import streamlit as st


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


    return