# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#loading saved models
diabetes_model = pickle.load(open('C:/Users/devan/Desktop/Multiple Disease Prediction System/Saved Models/diabetes_model.sav','rb'))

heart_model = pickle.load(open('C:/Users/devan/Desktop/Multiple Disease Prediction System/Saved Models/heart_disease_model.sav','rb'))

parkinsons_model = pickle.load(open('C:/Users/devan/Desktop/Multiple Disease Prediction System/Saved Models/parkinsons_model.sav','rb'))

#sidebar for navigate

with st.sidebar:
    
    selected = option_menu('Mutliple Disease Prediction System',
                           ['Diabetes Disease',
                            'Heart Disease',
                            'Parkinsons Disease'],
                             icons = ['activity','suit-heart','person-fill'],
                             default_index = 0)
    
    #Diabetes Prediction 
    
if(selected == 'Diabetes Disease'):
    #page title
    st.title('Diabetes Prediction')
    
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('Blood Pressure value')
    SkinThickness = st.text_input('Skin Thickness value')
    Insulin = st.text_input('Insulin Level')
    BMI = st.text_input('BMI value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    Age = st.text_input('Age of the Person')
    
    diab_diagnosis = ''
    
    if st.button('Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'Yes.....diabetes!!!'
        
        else:
            diab_diagnosis = 'No.....diabetes!!! '
        
    st.success(diab_diagnosis)

if(selected == 'Heart Disease'):
     #page title
     st.title('Heart Prediction')
     
     age = st.text_input('Age')
     sex = st.text_input('Sex')
     cp = st.text_input('Chest Pain types')
     trestbps = st.text_input('Resting Blood Pressure')
     chol = st.text_input('Serum Cholestoral in mg/dl')
     fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
     restecg = st.text_input('Resting Electrocardiographic results')
     thalach = st.text_input('Maximum Heart Rate achieved')
     exang = st.text_input('Exercise Induced Angina')
     oldpeak = st.text_input('ST depression induced by exercise')
     slope = st.text_input('Slope of the peak exercise ST segment')
     ca = st.text_input('Major vessels colored by flourosopy')
     thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
     # code for Prediction
     heart_diagnosis = ''
    
    # creating a button for Prediction
    
     if st.button('Result'):
        heart_prediction = heart_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'Yes.....heart disease!!!'
        else:
          heart_diagnosis = 'No.....heart disease!!!'
        
     st.success(heart_diagnosis)
         
if(selected == 'Parkinsons Disease'):
      #page title
      st.title('Parkinsons Prediction')
      fo = st.text_input('MDVP:Fo(Hz)')
      fhi = st.text_input('MDVP:Fhi(Hz)')
      flo = st.text_input('MDVP:Flo(Hz)')
      Jitter_percent = st.text_input('MDVP:Jitter(%)')
      Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
      RAP = st.text_input('MDVP:RAP')
      PPQ = st.text_input('MDVP:PPQ')   
      DDP = st.text_input('Jitter:DDP')
      Shimmer = st.text_input('MDVP:Shimmer')
      Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
      APQ3 = st.text_input('Shimmer:APQ3')
      APQ5 = st.text_input('Shimmer:APQ5')
      APQ = st.text_input('MDVP:APQ')
      DDA = st.text_input('Shimmer:DDA')       
      NHR = st.text_input('NHR')
      HNR = st.text_input('HNR')
      RPDE = st.text_input('RPDE')
      DFA = st.text_input('DFA')
      spread1 = st.text_input('spread1')
      spread2 = st.text_input('spread2')
      D2 = st.text_input('D2')
      PPE = st.text_input('PPE')  
         # code for Prediction
      parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
      if st.button("Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "Yes.....Parkinson's disease!!!"
        else:
          parkinsons_diagnosis = "No.....Parkinson's disease!!!"
        
      st.success(parkinsons_diagnosis)
      