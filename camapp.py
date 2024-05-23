{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "8db5eefe",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "0bd3176d",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "from streamlit_webrtc import webrtc_streamer\n",
    "st.title(\"OpenCV Filters on Video Stream\")\n",
    "webrtc_streamer(key=\"streamer\", sendback_audio=False)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
