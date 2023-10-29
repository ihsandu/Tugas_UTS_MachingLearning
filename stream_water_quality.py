import pickle
import numpy as np
import streamlit as st

model = pickle.load(open('water_quality_lr.sav', 'rb'))

st.title('Predict Water Quality')

col1, col2, col3, col4 = st.columns(4)

with col1:
    aluminium = st.number_input('Aluminium')
    ammonia	= st.number_input('Ammonia')
    arsenic	= st.number_input('Arsenic')
    barium = st.number_input('Barium')
    cadmium = st.number_input('Cadnium')
with col2:
    chloramine = st.number_input('Chloramine')
    chromium = st.number_input('Chromium')
    copper = st.number_input('Copper')
    flouride = st.number_input('Flouride')
    bacteria = st.number_input('Bacteria')
with col3:
    viruses = st.number_input('Viruses')
    lead = st.number_input('Lead')
    nitrates = st.number_input('Nitrates')
    nitrites = st.number_input('Nitrites')
    mercury = st.number_input('Mercury')
with col4:
    perchlorate	= st.number_input('Perchlorate')
    radium = st.number_input('Radium')
    selenium = st.number_input('Selenium')
    silver = st.number_input('Silver')
    uranium = st.number_input('Uranium')

water_quality =''

if st.button('Predict Water Quality'):
    water_quality_prediction = model.predict([[aluminium, ammonia, arsenic, barium, cadmium, chloramine, chromium, copper, flouride, bacteria, viruses, lead, nitrates, nitrites, mercury, perchlorate, radium, selenium, silver, uranium]])

    if(water_quality_prediction[0]==1):
        water_quality = 'Water quality is safe'
    else:
        water_quality = 'Water quality is not safe'
st.success(water_quality)