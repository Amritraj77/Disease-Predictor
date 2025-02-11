import os 
import pickle
import streamlit as st

st.set_page_config(page_title = 'Prediction of Disease Outbreaks', 
                   layout='wide', page_icon = "👨‍⚕️")

model_directory = os.path.join("saved_models")
diabetes_model = pickle.load(open(os.path.join(model_directory, "diabetes_model.sav"), "rb"))
heart_model = pickle.load(open(os.path.join(model_directory, "heart_model.sav"), "rb"))
parkinsons_model = pickle.load(open(os.path.join(model_directory, "parkinsons_model.sav"), "rb"))



with st.sidebar:
    selected = st.selectbox(
        'Select Disease Prediction',
        ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction']
    )
    
if selected == 'Diabetes Prediction':  
    st.title('Diabetes Prediction using ML')  
    col1, col2, col3 = st.columns(3)  
    
    with col1:  
        Pregnancies = st.text_input('Number of Pregnancies')  
    
    with col2:  
        Glucose = st.text_input('Glucose level')  
    
    with col3:  
        Bloodpressure = st.text_input('Blood Pressure value')  
    
    with col1:  
        SkinThickness = st.text_input('Skin Thickness value')  
    
    with col2:  
        Insulin = st.text_input('Insulin level')  
    
    with col3:  
        BMI = st.text_input('BMI value')  
    
    with col1:  
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function')  
    
    with col2:  
        Age = st.text_input('Age of the person')

    diab_diagnosis = ''

    if st.button('Diabetes Test Result'):
        user_input = [Pregnancies, Glucose, Bloodpressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
        user_input = [float(x) if x.strip() else 0 for x in user_input]
        diab_prediction = diabetes_model.predict([user_input])
        if diab_prediction[0] == 1:
            diab_prediction = 'The Person is Diabetic'
        else:
            diab_diagnosis = 'The Person is Not Diabetic'

    st.success(diab_diagnosis)


    
elif selected == 'Heart Disease Prediction':  
    st.title('Heart Disease Prediction using ML')  
    col1, col2, col3 = st.columns(3)  
    
    with col1:  
        d1 = st.text_input('Age')  
    
    with col2:  
        d2 = st.text_input('Sex')  
    
    with col3:  
        d3 = st.text_input('Chest Pain Types')  
    
    with col1:  
        d4 = st.text_input('Resting Blood Pressure')  
    
    with col2:  
        d5 = st.text_input('Serum Cholestrol in mg/dl')  
    
    with col3:  
        d6 = st.text_input('Fasting Blood Sugar > 120 mg/dl')  
    
    with col1:  
        d7 = st.text_input('Resting Electrocardiographic Results')  
    
    with col2:  
        d8 = st.text_input('Maximum Heart Rate Achieved')
    
    with col3:
        d9 = st.text_input('Excised Induced Angina')
    
    with col1:  
        d10 = st.text_input('ST Depression Induced By Exercise ')  
    
    with col2:  
        d11 = st.text_input('Slope of Peak Exercise ST Segment')  
    
    with col3:  
        d12 = st.text_input('Major Vessels Colored by Flourosopy') 

    with col1:  
        d13 = st.text_input('Thal: 0 = Normal, 1=Fixed Defect, 2=Reversible Defect')  

    heart_diagnosis = ''

    if st.button('Heart Test Result'):
        user_input = [d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13]
        user_input = [float(x) if x.strip() else 0 for x in user_input]
        heart_prediction = heart_model.predict([user_input])
        if heart_prediction[0] == 1:
            heart_diagnosis = 'The Person Has a Heart Disease '
        else:
            heart_diagnosis = 'The Person Does Not Has a Heart Disease'

    st.success(heart_diagnosis)

elif selected == 'Parkinsons Prediction':  
    st.title('Parkinsons Prediction using ML')  
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:  
        p1 = st.text_input('MDVP:Fo(Hz)')  
    
    with col2:  
        p2 = st.text_input('MDVP:Fhi(Hz)')  
    
    with col3:  
        p3 = st.text_input('MDVP:Flo(Hz)')  
    
    with col4:  
        p4 = st.text_input('MDVP:Jitter(%)')  
    
    with col5:  
        p5 = st.text_input('MDVP:Jitter(Abs)')  
    
    with col1:  
        p6 = st.text_input('MDVP:RAP')  
    
    with col2:  
        p7 = st.text_input('MDVP:PPQ')  
    
    with col3:  
        p8 = st.text_input('Jitter:DDP')
    
    with col4:
        p9 = st.text_input('MDVP:Shimmer')
    
    with col5:  
        p10 = st.text_input('MDVP:Shimmer(dB)')  
    
    with col1:  
        p11 = st.text_input('Shimmer:APQ3')  
    
    with col2:  
        p12 = st.text_input('Shimmer:APQ5') 

    with col3:  
        p13 = st.text_input('MDVP:APQ')  
    
    with col4:
        p14 = st.text_input('Shimmer:DDA')

    with col5:  
        p15 = st.text_input('NHR')

    with col1:  
        p16 = st.text_input('HNR')  
    
    with col2:  
        p17 = st.text_input('RPDE') 

    with col3:  
        p18 = st.text_input('DFA')  
    
    with col4:
        p19 = st.text_input('spread1')

    with col5:  
        p20 = st.text_input('spread2')
    
    with col1:  
        p21 = st.text_input('D2')  
    
    with col2:  
        p22 = st.text_input('PPE') 

    park_diagnosis = ''

    if st.button('Parkinsons Test Result'):
        user_input = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19,p20,p21,p22]
        user_input = [float(x) if x.strip() else 0 for x in user_input]
        park_prediction = parkinsons_model.predict([user_input])
        if park_prediction[0] == 1:
            park_diagnosis = 'Parkinsons Positive'
        else:
            park_diagnosis = 'Parkinsons Negative'

    st.success(park_diagnosis)




