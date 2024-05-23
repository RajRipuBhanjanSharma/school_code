{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "d705d7c5",
   "metadata": {},
   "outputs": [],
   "source": [
    "# !pip install streamlit as st"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "9e66307f",
   "metadata": {},
   "outputs": [],
   "source": [
    "# import streamlit as st\n",
    "# from streamlit_webrtc import webrtc_streamer\n",
    "# st.title(\"OpenCV Filters on Video Stream\")\n",
    "# webrtc_streamer(key=\"streamer\", sendback_audio=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "6f6e70aa",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "from streamlit_webrtc import webrtc_streamer\n",
    "import av\n",
    "import cv2\n",
    "import numpy as np\n",
    "\n",
    "st.title(\"OpenCV Filters on Video Stream\")\n",
    "\n",
    "def video_frame_callback(frame):\n",
    "    img = frame.to_ndarray(format=\"bgr24\")\n",
    "\n",
    "    # Apply OpenCV filter (example: converting to grayscale)\n",
    "    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)\n",
    "    gray_3ch = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)\n",
    "\n",
    "    return av.VideoFrame.from_ndarray(gray_3ch, format=\"bgr24\")\n",
    "\n",
    "webrtc_streamer(\n",
    "    key=\"example\",\n",
    "    video_frame_callback=video_frame_callback,\n",
    "    sendback_audio=False\n",
    ")\n"
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
