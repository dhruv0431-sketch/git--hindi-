import streamlit as st 
st.set_page_config(page_title="ECONav AI", LAYOUT="CENTERED " ) 
#title 
st.title("ECONAV AI")
st.subheader (" smart Eco- friendly route finder ") 
 
 #input 
source = st.text_input("enter source location ")
destination=st.text_input("enter destination ")
 
 # option 
option = st.selectbox ( 
    " choose preference ", 
    ["eco friendly ", "fastest", "cheapest"]
 ) 

#button 
if st.button("find route "): 
 if source =="" or destination == "": 
      st.warning (" please enter both location  ") 
 else: st.sucess ("FINDING BEST ROUTE ") \
 
st.subheader("result ") 
st.write("route: abc road XYZ HIGHWAY" ) 
st.write(" pollution:low ") 
st.write(" traffic:medium ")