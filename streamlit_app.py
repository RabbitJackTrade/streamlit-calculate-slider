import streamlit as st
import pandas as pd
"""
# My first app
Here's our first attempt at using data to create a table without write():
"""

df = pd.DataFrame({'Units_num': [20,70,0], 
                   'Own_pct': [0,0,0]})
df['Own_pct'] = df.Units_num/ df.Units_num.sum()
df.loc['Units_total']= df.sum(numeric_only=True, axis=0)
df['Units_num'] = df['Units_num'].astype(int)
df.index = ['Member_1', 'Member_2', 'Exec',' Total']

"""
mushi = [10,20,30,40]
option = st.sidebar.selectbox(
    'How many units in the grant?',    
     mushi)
'You selected: ', option
"""
score = st.sidebar.slider('Select number of units to grant', min_value=5, max_value=40, value = 5) # Getting the input.
df.at['Exec','Units_num']=score
df.loc[' Total']= df.iloc[0:3].sum(numeric_only=True, axis=0)
total = df.iloc[0:3].sum(numeric_only=True, axis=0).to_list()[0]
df['Own_pct'] = (df.Units_num/ total).map("{:.2%}".format)


st.write(df)
