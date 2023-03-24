import streamlit as st

import Display


def main():

    st.header('My Stock Inquiry System(MSIS)')

    chk00=st.sidebar.checkbox('시장 지표 보기')
    chk01=st.sidebar.checkbox('미연방은행(FRED) 주요지표 보기')
    chk02=st.sidebar.checkbox('주요 뉴스 보기')
    if chk00: st.text('시장 지표 보기')
    if chk01: Display.연방은행주요지표보기()
    if chk02: st.text('주요 뉴스 보기')

    return



#####################################################
##### Main ##########################################
#####################################################
if __name__ == '__main__':
    main()