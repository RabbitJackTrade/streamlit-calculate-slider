import streamlit as st
import pandas as pd

eb_actual = st.sidebar.slider('Enter the dollar amount (in $M) from EB', min_value=1.0, step=0.5, max_value=7.0,format="$%gM")
guys_actual = st.sidebar.slider('Enter the dollar amount (in $M) from Guys', min_value=1.0, step = 0.5, max_value=8.0,format="$%gM")

eb5_targ = 7000000
eb_perc_targ = 0.0875
eb_perc_actual = eb_perc_targ*(eb_actual*1000000/eb5_targ)

guys_targ = 8000000
guys_perc_targ = 0.9
guys_perc_actual = guys_perc_targ*(guys_actual*1000000/guys_targ)*(1-eb_perc_actual)


df = pd.DataFrame({'Perc_Owned': [.0,.0,.0,0]})
df.iloc[0,0]=eb_perc_actual
df.iloc[1,0]=guys_perc_actual
df.iloc[2,0]=(1-eb_perc_actual-guys_perc_actual)
df.iloc[3,0] = df.iloc[0:3].sum(numeric_only=True, axis=0)
df['Perc_Owned'] = df['Perc_Owned'].astype(float).map("{:.3%}".format)
df.index = ['SP_man', 'Guys', 'Son',' Total']

st.write(df)

html_code = f"""
<table style="border-collapse: collapse; border: none; margin-top: 0em; table-layout: auto;">
<thead>
<tr style="border: none;">
    <th style="padding: 0 1em 0 0.5em; text-align: right; border: none;">Member</th>
    <th style="padding: 0 0.5em 0 0.5em; text-align: left; border: none;">Percent Owned</th>
</tr>
</thead>
<tbody>
    <tr style="background-color: hsl(120, 100.00%, 80.00%); border: none;">
        <td style="padding: 0 1em 0 0.5em; text-align: right; border: none;">
            SP_Man
        </td>
        <td style="padding: 0 0.5em 0 0.5em; text-align: left; border: none;">
            &nbsp;&nbsp;{eb_perc_actual:.3%} 
        </td>
    </tr>
    <tr style="background-color: hsl(120, 100.00%, 81.40%); border: none;">
        <td style="padding: 0 1em 0 0.5em; text-align: right; border: none;">
           Guys
        </td>
        <td style="padding: 0 0.5em 0 0.5em; text-align: left; border: none;">
           &nbsp;{guys_perc_actual:.3%}
        </td>
    </tr>
    <tr style="background-color: hsl(120, 100.00%, 93.05%); border: none;">
        <td style="padding: 0 1em 0 0.5em; text-align: right; border: none;">
            Son
        </td>
        <td style="padding: 0 0.5em 0 0.5em; text-align: left; border: none;">
            &nbsp;&nbsp;{(1-eb_perc_actual-guys_perc_actual):.3%}
        </td>
    </tr>
    <tr style="background-color: hsl(120, 100.00%, 96.96%); border: none;">
        <td style="padding: 0 1em 0 0.5em; text-align: right; border: none;">
            Total
        </td>
        <td style="padding: 0 0.5em 0 0.5em; text-align: left; border: none;">
            100.000%
        </td>
    </tr>
</tbody>
"""

st.markdown(html_code, unsafe_allow_html=True)
ht2 = f"""<table style="width:50%">
  <tr>
    <th>Member</th>
    <th>Percent Owned</th>    
  </tr>
  <tr>
    <td>SP_Man</td>
    <td> &nbsp;&nbsp;{eb_perc_actual:.3%} </td>    
  </tr>
  <tr>
    <td>Guys</td>
    <td>&nbsp;{guys_perc_actual:.3%}</td>    
  </tr>
  <tr>
    <td>Son</td>
    <td>&nbsp;&nbsp;{(1-eb_perc_actual-guys_perc_actual):.3%}</td>    
  </tr>  
  <tr>
    <td>Total</td>
    <td>100.000%</td>    
  </tr>  
</table>"""
st.markdown(ht2, unsafe_allow_html=True)
