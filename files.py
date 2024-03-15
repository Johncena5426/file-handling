import streamlit as st
import pandas as pd

st.subheader('Uploading the CSV')
df = st.file_uploader('upload the csv file:',type = ['csv'])
if df is not None:
    st.dataframe(df)
    st.table(df)

st.subheader('Loading the CSV')
df = pd.read_csv('Products.csv')
if df is not None:
    st.table(df.head())

st.subheader('Dealing with images Directly')
st.image('img.png')
st.subheader('Dealing with images while uploading')
img_file = st.file_uploader('upload the image file:',type = ['png'])
if(img_file is not None):
    st.image(img_file)

st.subheader('Working with videos')
video_file = st.file_uploader('upload the Video file:',type = ['mp4'])
if(video_file is not None):
    st.video(video_file,start_time = 0)
    
st.subheader('Working with Audio')
Audio_file = st.file_uploader('upload the Audio file:',type = ['mp3'])
if(Audio_file is not None):
    st.audio(Audio_file.read())