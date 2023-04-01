import streamlit as st

from Codes import Display


def main():

    st.header('My Stock Management System(MSMS)')

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
    main()