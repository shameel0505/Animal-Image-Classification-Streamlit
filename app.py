import streamlit as st
import cv2 
from PIL import Image
import tensorflow as tf
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.densenet import preprocess_input
print(tf.__version__)
classe=['cat','dog','snake']
st.title('Animal Classification')
st.subheader('Upload your image')
image=st.file_uploader('Upload your image',type=('jpg','jpeg','JPG','JPEG'))
st.sidebar.title('Select the model you want to use')
option=st.sidebar.radio('choose one:',
                 ('densenet121','efficentnetB0','inceptionV2','mobilenetV2',"resnet"))
# img=cv2.imread(image)
if image is not None:
    image=Image.open(image)
    st.write('the uploaded image')
    st.image(image)
    img_cv=np.array(image)
    if option=='densenet121':
        model=load_model('animal_classification/models/densenet121.h5')
        img=cv2.resize(img_cv,(224,224))
        img=preprocess_input(img)
        img=np.expand_dims(img,axis=0)
        result=model.predict(img)
        clas=classe[np.argmax(result)]
        st.subheader(f'class: {clas} (densenet121)')
        
    elif option=='efficentnetB0':
        model=load_model('animal_classification/models/efficentnet_b0.h5')
        img=cv2.resize(img_cv,(224,224))
        img=preprocess_input(img)
        img=np.expand_dims(img,axis=0)
        result=model.predict(img)
        clas=classe[np.argmax(result)]
        st.subheader(f'class: {clas} (efficentnetB0)')
    elif option=='inceptionV2':
        model=load_model('animal_classification/models/inceptionv3.h5')
        img=cv2.resize(img_cv,(299,299))
        img=preprocess_input(img)
        img=np.expand_dims(img,axis=0)
        result=model.predict(img)
        clas=classe[np.argmax(result)]
        st.subheader(f'class: {clas} (inceptionV2)')
    elif option=='mobilenetV2':
        model=load_model('animal_classification/models/MobileNetV2.h5')
        img=cv2.resize(img_cv,(224,224))
        img=preprocess_input(img)
        img=np.expand_dims(img,axis=0)
        result=model.predict(img)
        clas=classe[np.argmax(result)]
        st.subheader(f'class: {clas} (mobilenetV2)')
    elif option=='resnet':
        model=load_model('animal_classification/models/ResNet.h5')
        img=cv2.resize(img_cv,(180,180))
        # img=preprocess_input(img)
        img=np.expand_dims(img,axis=0)
        result=model.predict(img)
        clas=classe[np.argmax(result)]
        st.subheader(f'class: {clas} (resnet)')