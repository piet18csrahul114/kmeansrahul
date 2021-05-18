import streamlit as st 
from PIL import Image
import pickle
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
st.set_option('deprecation.showfileUploaderEncoding', False)
# Load the pickled model
model = pickle.load(open('kmeansclusterrahul.pkl','rb'))   
dataset= pd.read_csv('Wholesale customers data.csv')
X = dataset.iloc[:,2:8].values
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X = sc.fit_transform(X)
def predict_note_authentication(Channel,Region,Fresh,Milk,Grocery,Frozen,Detergents_Paper,Delicassen):
  predict= model.predict(sc.transform([[Fresh,Milk,Grocery,Frozen,Detergents_Paper,Delicassen]]))
  print("cluster number", predict)
  if predict==[0]:
    res="Customer is careless"
  elif predict==[1]:
    res="Customer is standard"
  elif predict==[2]:
    res="Customer is Target"
  elif predict==[3]:
    res="Customer is careful"
  else:
    res="Customer is sensible"
  return res
  
def main():
    
    html_temp = """
   <div class="" style="background-color:yellow;" >
   <div class="clearfix">           
   <div class="col-md-12">
   <center><p style="font-size:40px;color:white;margin-top:10px;">Poornima Institute of Engineering & Technology</p></center> 
   <center><p style="font-size:30px;color:white;margin-top:10px;">Department of Computer Engineering</p></center> 
   <center><p style="font-size:25px;color:white;margin-top:10px;"Machine Learning Lab Experiment</p></center> 
   </div>
   </div>
   </div>
   """
    st.markdown(html_temp,unsafe_allow_html=True)
    st.header("Customer Segmenation on wholesale data ")

    Channel = st.selectbox(
    "Channel",
    ("1", "2")
    )
    Region = st.selectbox(
    "Region",
    ("1", "2","3")
    )

    Fresh = st.number_input('Insert fresh',3,112151)
    Milk = st.number_input('Insert milk',55,73498)
    Grocery = st.number_input('Insert grocery',3,92780)
    Frozen = st.number_input('Insert frozen',25,60869)
    Detergents_Paper = st.number_input('Insert Detergents_Paper',3,40827)
    Delicassen = st.number_input('Insert Delicassen',3,47943)
    

    result=""

    if st.button("Predict"):
      result=predict_note_authentication(Channel,Region,Fresh,Milk,Grocery,Frozen,Detergents_Paper,Delicassen)
      st.success('Model has predicted {}'.format(result))

    if st.button("About"):
      st.subheader("Developed by Rahul Chhablani")
      st.subheader("Department of Computer Engineering") 

if __name__=='__main__':
  main()
