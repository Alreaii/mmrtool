import pnwkit
import numpy
import pandas as pd
import streamlit as st

kit = pnwkit.QueryKit(st.secrets["apikey"])

st.markdown("<h1 style='text-align: center;'>Nation MMR Tool</h1>", unsafe_allow_html=True)



nationid = st.text_input("Nation ID", "")

if nationid != "":
    nationid = int(nationid)
    
    nationCities = kit.query("nations", {"id": nationid}, "nation_name num_cities soldiers tanks aircraft ships").get()
    citycount = nationCities.nations[0].num_cities
    mmrtype = 0
    
    
    "---"
    
    st.write(f"Nation name: {nationCities.nations[0].nation_name}")
    
    st.write(f"City count: {citycount}")
    
    
    st.markdown("<h4 style='text-align: center;'>Your current military</h4>", unsafe_allow_html=True)
    nationMil = pd.DataFrame({"Soldiers": [nationCities.nations[0].soldiers], "Tanks": [nationCities.nations[0].tanks], "Planes": [nationCities.nations[0].aircraft], "Ships": [nationCities.nations[0].ships]})
    st.table(nationMil)
    
    st.markdown("<h4 style='text-align: center;'>Your regulation minimum military</h4>", unsafe_allow_html=True)
    
    
    
    if citycount == 0:
        st.write("Nation not found")
    
    elif citycount <= 9 and citycount >= 1:
        mmrtype = 1
        st.write(f"Raiding MMR -> 5/2/1/1")
        mmrTable = pd.DataFrame({"Soldiers": [citycount * 3000 * 5], "Tanks": [citycount * 250 * 2], "Planes": [citycount * 15 * 1], "Ships": [citycount * 5 * 1]})
        st.table(mmrTable)
    
    elif citycount <= 19 and citycount >= 10:
        mmrtype = 2
        st.write(f"Farming MMR -> 1/2/5/1")
        mmrTable = pd.DataFrame({"Soldiers": [citycount * 3000 * 1], "Tanks": [citycount * 250 * 2], "Planes": [citycount * 15 * 5], "Ships": [citycount * 5 * 1]})
        st.table(mmrTable)
    
    elif citycount >= 20:
        mmrtype = 3
        st.write(f"Farming MMR -> 0/2/5/0")
        mmrTable = pd.DataFrame({"Soldiers": [citycount * 3000 * 0], "Tanks": [citycount * 250 * 2], "Planes": [citycount * 15 * 5], "Ships": [citycount * 5 * 0]})
        st.table(mmrTable)
    
    st.markdown("<h4 style='text-align: center;'>Troops needed to meet MMR</h4>", unsafe_allow_html=True)
    
    if mmrtype == 1:
        diffDf = (mmrTable["Soldiers"] - nationMil["Soldiers"], mmrTable["Tanks"] - nationMil["Tanks"], mmrTable["Planes"] - nationMil["Planes"], mmrTable["Ships"] - nationMil["Ships"])
        st.table(diffDf)
    elif mmrtype == 2:
        diffDf = (mmrTable["Soldiers"] - nationMil["Soldiers"], mmrTable["Tanks"] - nationMil["Tanks"], mmrTable["Planes"] - nationMil["Planes"], mmrTable["Ships"] - nationMil["Ships"])
        st.table(diffDf)
    elif mmrtype == 3:
        diffDf = (mmrTable["Soldiers"] - nationMil["Soldiers"], mmrTable["Tanks"] - nationMil["Tanks"], mmrTable["Planes"] - nationMil["Planes"], mmrTable["Ships"] - nationMil["Ships"])
        
        st.table(diffDf)







