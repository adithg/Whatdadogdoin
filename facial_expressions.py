import numpy as np
import pandas as pd

import json

import asyncio

from hume import HumeStreamClient, StreamSocket, HumeBatchClient
from hume.models.config import FaceConfig

import os
import cv2

LUAN_API_KEY = "0BU3yyyBmwT7r6uXV8uh7q17pjNQofKCUnDA2ZfNAGl5Rn8U"

all_emotions = ['Admiration', 'Adoration','Aesthetic Appreciation','Amusement','Anger','Anxiety','Awe','Awkwardness',
                'Boredom','Calmness','Concentration','Confusion','Contemplation','Contempt','Contentment','Craving',
                'Desire','Determination','Disappointment','Disgust','Distress','Doubt','Ecstasy','Embarrassment',
                'Empathic Pain','Entrancement','Envy','Excitement','Fear','Guilt','Horror','Interest',
                'Joy','Love','Nostalgia','Pain','Pride','Realization','Relief','Romance',
                'Sadness','Satisfaction','Shame','Surprise (negative)','Surprise (positive)','Sympathy','Tiredness','Triumph']

# Start webcam
webcam = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
out = cv2.VideoWriter('tradevid.mp4', fourcc, 30.0, (640, 480)) # 30 fps, 640 x 480 px

while(True):
    # Capture frame
    check, frame = webcam.read()

    # Check for successful capture
    if check:
        # Write the frame into the file 'tradevid.mp4'
        out.write(frame)
        # Display the resulting frame
        cv2.imshow("IronMind", frame)

    # Stop recording when 'esc' key is pressed
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Close webcam, release video, and free memory
webcam.release()
out.release()
cv2.destroyAllWindows()

# Start Hume Batch API
batch_client = HumeBatchClient(LUAN_API_KEY)

# Send video to analyze facial expressions
job = batch_client.submit_job(urls=[], configs=[FaceConfig(identify_faces=True)], files=["tradevid.mp4"])
details = job.await_complete()
job.download_predictions("trade_emotions.json")

# Process emotion predictions into pandas DataFrame with mean score per emotion
vid_dict = json.load(open("trade_emotions.json"))[0]["results"]["predictions"][0]["models"]["face"]["grouped_predictions"][0]["predictions"]
trade_df = pd.DataFrame.from_dict({"name": all_emotions, "score": np.repeat(0.0, 48)})
num_frames = len(vid_dict)
for i in range(num_frames):
    emotions_dict = vid_dict[i]["emotions"]
    emotions_df = pd.DataFrame.from_dict(emotions_dict).sort_values("name")
    trade_df["score"] = trade_df["score"] + emotions_df["score"]
trade_df["score"] = trade_df["score"] / num_frames

# Identify emotion with highest mean value
trade_df = trade_df.sort_values("score", ascending=False)
print(trade_df)
top_emotion = trade_df.iloc[0, 0]
print(f"Top emotion: {top_emotion}")
top_score = trade_df.iloc[0, 1]
print(f"Score for top emotion: {top_score}")

# Decide on output message depending on emotion value
description = ""
if top_score >= 0.75 and top_score <= 1:
    description = f"This trade was characterized by very prominent ({np.round(top_score * 100, 2)}%) {top_emotion}."
elif top_score >= 0.5 and top_score < 0.75:
    description = f"{top_emotion} was noticeable ({np.round(top_score * 100, 2)}%) throughout this trade."
elif top_score >= 0.3 and top_score < 0.5:
    description = f"Some {top_emotion} was detected ({np.round(top_score * 100, 2)}%) during this trade."
elif top_score < 0.3:
    description = "No significant emotional data for this trade."
print(description)