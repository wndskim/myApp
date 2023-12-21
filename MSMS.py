import streamlit as st

from Codes import Display


def main():

    st.header('My Stock Management System(MSMS)')

    st.write('심플강력 전략')
    st.write('1. 투자ETFs')
    st.text(' - TQQQ: 50%')
    st.text(' - SCHD: 30%')
    st.text(' - PFIX: 10%')
    st.text(' - TMF: 10%')
    st.write('2. Rebalancing')
    st.text(' - 매월 첫 거래일 비중을 맞추어 리밸런싱 진행')
    st.text(' - SCHD는 리밸런싱 하지 않는다')
    st.text(' - 200일선 아래에 있는 자산은 50% 매도')
    st.text(' - 140일선이 하락하고 있는 자산은 50% 추가 매도(이동평균선 하락은 전전날과 전날 이평선을 비교하여 판단)')
    st.text(' - 감산에서 2연타를 맞은 자산이 PFIX나 TMF인경우 비중을 0으로 만들고 모두 매도')
    st.text(' - TMF를 모두 매도 했다면 PFIX를 2배의 비중으로 보유')
    st.text(' - PFIX를 모두 매도 했다면 TMF를 2배의 비중으로 보유')
    st.text(' - TQQQ가 감산 2연타를 맞으면 PFIX에 35%의 비중을 더해 준다')
    st.text(' - PFIX를 모두 매도 했는데 TQQQ가 2연타 감산을 맞지 않은 상태면 남은 현금으로 TQQQ를 매수')
    



    chk00=st.sidebar.checkbox('시장 지표 보기')
    chk01=st.sidebar.checkbox('미연방은행(FRED) 주요지표 보기')
    chk02=st.sidebar.checkbox('주요 뉴스 보기')
    if chk00: Display.시장지표보기()
    if chk01: Display.연방은행주요지표보기()
    if chk02: Display.주요뉴스보기()

    return



#####################################################
##### Main ##########################################
#####################################################
if __name__ == '__main__':

    st.set_page_config(
        page_title="My Stock Management System",
        layout="centered"
    )
    
    main()