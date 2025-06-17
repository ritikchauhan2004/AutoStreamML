import profile
import streamlit as st
import pandas as pd
import os
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report



from pycaret.classification import setup, compare_models,pull,save_model


with st.sidebar:
    st.image("https://www.onepointltd.com/wp-content/uploads/2020/03/inno2.png")
    st.title("AutoStreamML")
    choice=st.radio("Navigation",["Upload","Profiling","ML","Download"])
    st.info("This app is used for making an automated ML pipline using Streamlit")

if os.path.exists("sourcedata.csv"):
    df= pd.read_csv("sourcedata.csv", index_col=None)

if choice== "Upload":
    st.title("Upload your DATA")
    file=st.file_uploader("Upload your dataset here")
    if file:
        df = pd.read_csv(file, index_col=None)
        df.to_csv("sourcedata.csv", index=None)    # type: ignore
        st.dataframe(df)
        
elif choice=="Profiling":
    st.title("Automated EDA")
    profile_report= df.profile_report()
    st_profile_report(profile_report)
    
elif choice=="ML":
    st.title("Machine Learning")
    target= st.selectbox("Select your Target",df.columns)
    if st.button("Train Model"):
        setup(df,target=target,silent=True)
        setup_df=pull()
        st.info("This is ML Expriment Setting")
        st.dataframe(setup_df)
        best_model=compare_models()
        compare_df=pull()
        st.info("This is the ML Model")
        st.dataframe(compare_df)
        best_model
        save_model(best_model,'best_model')
        st.success("Model Trained Successfully")
elif choice=="Download":
    pass