import pickle 
import numpy as np
import streamlit as st

loaded_model=pickle.load(open("grid_search.sav",'rb'))

def liver_patient(input_data):
    input_data_as_numpy_array=np.asarray(input_data)
    input_data_reshaped=input_data_as_numpy_array.reshaped(1,-1)
    prediction=loaded_model.predict(input_data_reshaped)
    print(prediction)
    
    if(prediction[1]==1):
        return "Liver diesease"
    else:
        return "Patient have no liver diesease"
        
def main():
    st.title("Indian Liver Diesease Prediction")
    
    Age=st.text_input("Age",'0.00')
    Gender=st.text_input("Gender",'0.00')
    Total_Bilirubin=st.text_input("Total_Bilirubin",'0.00')
    Direct_Bilirubin=st.text_input("Direct_Bilirubin",'0.00')
    Alkaline_Phosphotase=st.text_input("Alkaline_Phosphotase",'0.00')
    Alamine_Aminotransferase=st.text_input("Alamine_Aminotransferase",'0.00')
    Total_Protiens=st.text_input("Total_Protiens",'0.00')
    Albumin=st.text_input("Albumin",'0.00')
    Albumin_and_Globulin_Ratio=st.text_input("Albumin_and_Globulin_Ratio",'0.00')
    
    test_result=''
    
    if st.button('Check the Liver Diesease Prediction'):
        test_result=liver_patient([Age,Gender,Total_Bilirubin,Direct_Bilirubin,
                                   Alkaline_Phosphotase,Alamine_Aminotransferase,
                                   Aspartate_Aminotransferase,Total_Protiens,Albumin,
                                   Albumin_and_Globulin_Ratio])
        
        st.success(test_result)
        
if __name__=='__main__':
    main()

    
        

