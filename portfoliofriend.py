import numpy as np
import pandas as pd
import yfinance as s
import streamlit as st
from streamlit import caching 
 

#July/21
 
 
#function to create drawdowns
def create_drawdowns(equity_curve):
    hwm = [0]
    eq_idx = equity_curve.index
    drawdown = pd.Series(index = eq_idx)
    for t in range(1, len(eq_idx)):
        cur_hwm = max(hwm[t-1], equity_curve[t])
        hwm.append(cur_hwm)
        drawdown[t]= ((hwm[t] - equity_curve[t])/ hwm[t]) 
    return drawdown.max()
 

 
#title
st.markdown('''# Portfolio Friend''')
st.markdown('#')      
st.markdown('#')


#cache for portfolio metrics and correlation matrix
@st.cache(allow_output_mutation=True)
def persistdata():
    return {}
@st.cache(allow_output_mutation=True)
def persistdata_2():
    return {}

#containers to enter asset and units
with st.beta_container():
    #button to specify period of analysis
    p= st.radio("Select time period for all Assets",('1y','5y','Max'))
    st.write("#")


    #dictionaries for portfolio metrics and correlation matrix
    d = persistdata()    
    corr=persistdata_2()
    col1, col2 = st.beta_columns(2)
 
    with col1:
        stock = st.text_input(" Enter Asset ticker")
        result=pd.DataFrame(s.Ticker(stock).history(period=p)).fillna(method='bfill')
                 
    with col2:
        units = st.number_input("Enter units of Asset",min_value=0, max_value=100000, value=0, step=1)
 
    #add to portfolio or not
    button = st.button("Click here to add asset to Portfolio")
    if button:
        if stock and units:  
            st.markdown(' Historical price movement') 
            st.line_chart(result['Close'],width=760,height=200,use_container_width=False)         
            result['prev_close'] = result['Close'].shift(1).fillna(method='bfill')            
            dollar_exposure=  int(units) * result['prev_close'][-1]
            result['intraday upside']= ((result['High']- result['Open'])/result['Open'])*100
            result['intraday downside']= ((result['Low'] - result['Open'])/result['Open'])*100
            result['overnight movement']= ((result['prev_close']- result['Open'])/result['Open'])*100
            result['intraday range']=((result['High']- result['Low'])/result['Low'])*100
            result['drawdown']= (create_drawdowns(result['Close']))*dollar_exposure
            d[stock] = {'units': units,'dollar exposure':np.round(dollar_exposure),'max intraday upside %': int(result['intraday upside'].max()),'max intraday downside %': int(result['intraday downside'].min()) ,'max overnight movement %': int(result['overnight movement'].max()),
	                            'max intraday range %':int(result['intraday range'].max()) ,'max drawdown dollars': int(np.round((create_drawdowns(result['Close']))*dollar_exposure))}   
            df=pd.DataFrame(d).T
            df.loc['Total',:] = df.sum(axis=0).round()

            #Get prices for correlation matrix
            corr[stock]= pd.Series(result.Close.values).fillna(method='bfill')
            df_2 = pd.DataFrame(corr) 
            st.markdown('Current Portfolio')
            st.dataframe(df)
            st.markdown('#')
            st.markdown("Asset Price Correlations")            
            st.dataframe(df_2.corr())
            

             

 
 
            	 

             
		     
		    		 
 

		 
 
 
 

  

 
    


 

 
 
 

 

 
 
	  
