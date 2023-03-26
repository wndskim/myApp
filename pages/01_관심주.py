import streamlit as st
from pykrx import stock
import pandas as pd
from datetime import date

st.write('관심주')

chk00=st.sidebar.checkbox('코스피200 보기',value=False)
if chk00:
    col1,col2=st.columns([1,5])
    with col1:
        조회일=st.date_input('조회일', date.today())
        조회일=str(조회일).replace('-','')
        container=st.container()
    with col2:
        종목s=[]
        티커s=stock.get_index_portfolio_deposit_file('1028')
        for 티커 in 티커s:
            종목s.append(stock.get_market_ticker_name(티커))
        _df1=pd.DataFrame(list(zip(티커s, 종목s)), columns=['티커', '종목'])
        _df2=stock.get_market_ohlcv(조회일)
        _df2=_df2[_df2.index.isin(티커s)]

        df=pd.merge(_df1, _df2, on='티커')
        df.sort_values(by='등락률', ascending=False, inplace=True)

        df.reset_index(inplace=True)
        df.drop('index', axis=1, inplace=True)

        st.write('코스피200',len(df),'건')
        st.dataframe(df)

        종목s=df.종목.tolist()


        _dict=_df1.to_dict()
        종목=container.selectbox('선택', 종목s)
        container.text(종목,_df1[_df1['종목']==종목]['티커'].values[0])
        container.dataframe(_dict)


import pandas as pd

# create a sample dataframe
df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})

# convert the dataframe to a dictionary
my_dict = df.to_dict()

# print the resulting dictionary
print(my_dict)
