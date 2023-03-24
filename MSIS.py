import streamlit as st


def main():

    st.header('My Stock Inquiry System(MSIS)')

    chk01=st.sidebar.checkbox('미연방은행(FRED) 주요지표 보기')
    chk02=st.sidebar.checkbox('주요 뉴스 보기')
    if chk01: st.text('미연방은행 주요 지표')
    if chk02: st.text('주요 뉴스 보기')

    return



#####################################################
##### Main ##########################################
#####################################################
if __name__ == '__main__':
    main()