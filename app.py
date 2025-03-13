import streamlit as st
import time
import pygame
from datetime import datetime


pygame.mixer.init()

def play_sound(sound_file):
    """Play The Sound"""
    try:
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play()
    except pygame.error:
        st.error("Error: Sound file not found!")

def stop_Sound():
    """Stop The Alaram"""
    pygame.mixer.music.stop()



st.title("⏰Alaram Clock⏰")
st.write("Set the Time for Alarm")


alarm_time = st.time_input("Set time (HH:MM)" )

if alarm_time:
    alarm_time_str = alarm_time.strftime("%H:%M")

uploaded_file = st.file_uploader("Upload an MP3 file for alarm sound", type=["mp3"])

# Save uploaded file
if uploaded_file is not None:
    sound_path = "custom_alarm.mp3"
    with open(sound_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success("Custom sound uploaded successfully!")
else:
    sound_path = "alarm1.mp3" 


if st.button("Set Alaram"):
    st.success(f"Alarm set is {alarm_time_str} ")

status = st.empty()

alarm_triggered = False

while not alarm_triggered :
    current_time = datetime.now().strftime("%H:%M")

    if alarm_time_str == current_time:
        play_sound(sound_path)
        st.warning("Time up ! Wake up")
        alarm_triggered = True
        
   
if st.button("Stop Alaram", key="stop_button"):
   stop_Sound()
   st.success("Alarm Stopped")
   
