import streamlit as st
import pandas as pd

ht_tab = """<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>PPS exit 1</td>
      <td>$6</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Exit 1 Value</td>
      <td>$3,847,410</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Manager</td>
      <td>$745,705</td>
    </tr>
    <tr>
      <th>3</th>
      <td>A&amp;L $ entitlement</td>
      <td>$630,000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>A&amp;L $  actual</td>
      <td>$630,000</td>
    </tr>
    <tr>
      <th>5</th>
      <td>A&amp;L $ shortfall</td>
      <td>$0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Exit 1 manager</td>
      <td>$115,705</td>
    </tr>
    <tr>
      <th>7</th>
      <td>PPS exit 2</td>
      <td>$7</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Exit 2 Value</td>
      <td>$2,992,430</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Manager</td>
      <td>$1,496,215</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Exit 2 A&amp;L $ entitlement</td>
      <td>$490,000</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Exit 2 manager</td>
      <td>$1,006,215</td>
    </tr>
    <tr>
      <th>12</th>
      <td>L&amp;J total</td>
      <td>$1,120,000</td>
    </tr>
    <tr>
      <th>13</th>
      <td>A&amp;L total</td>
      <td>$1,121,920</td>
    </tr>
  </tbody>
</table>"""
df = pd.read_html(ht_tab)[0]

df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
#st.write(df)
hold =  1526750
cost = 2356000
ash = 250000

pps1 = st.sidebar.slider('Select pps for inital sale', min_value=2, max_value=30, value = 2)
pps2 = st.sidebar.slider('Select pps for the final sale', min_value=2, max_value=30, value = 2)
forf = st.sidebar.slider('Select forfeiture portion', min_value=0.0, max_value=0.5, value = 0.05)
dispo = st.sidebar.slider('Select initial disposition portion', min_value=0.0, max_value=0.7, value = 0.05)


e_val = hold*(1-forf)*dispo*pps1
inv = e_val if e_val<cost else cost+((e_val-cost)/2)


ash_val = pps1*ash*dispo*(1-forf)
e_val2 = hold*(1-forf)*(1-dispo)*pps2
inv2 = ((e_val+ e_val2-cost)/2)+ cost-inv
ash_val2 = pps2*ash*(1-forf)*(1-dispo)

df.iloc[0,1]=pps1
df.iloc[1,1] = e_val
df.iloc[2,1] = e_val-inv
df.iloc[3,1] = ash_val
df.iloc[4,1] = min(df.iloc[2,1],ash_val)
df.iloc[5,1] = df.iloc[3,1] - df.iloc[4,1] 
df.iloc[6,1] = max(df.iloc[2,1]-df.iloc[4,1],0)
df.iloc[7,1] = pps2
df.iloc[8,1] = e_val2
df.iloc[9,1] = e_val2-inv2
df.iloc[10,1] = ash_val2+df.iloc[5,1]
df.iloc[11,1] = df.iloc[9,1] - df.iloc[10,1]
df.iloc[12,1] = df.iloc[4,1] + df.iloc[10,1]
df.iloc[13,1] = df.iloc[6,1] + df.iloc[11,1]

df.iloc[:,1] = df.iloc[:,1].apply(lambda x: "${0:,.0f}".format(x))
st.table(df)


