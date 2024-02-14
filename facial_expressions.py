import numpy as np
import pandas as pd
import random

import json

from hume import HumeBatchClient
from hume.models.config import FaceConfig

import cv2
import datetime

from antitilt import insert_into_table

API_KEY = # Insert API key here

all_emotions = ['Admiration', 'Adoration','Aesthetic Appreciation','Amusement','Anger','Anxiety','Awe','Awkwardness',
                'Boredom','Calmness','Concentration','Confusion','Contemplation','Contempt','Contentment','Craving',
                'Desire','Determination','Disappointment','Disgust','Distress','Doubt','Ecstasy','Embarrassment',
                'Empathic Pain','Entrancement','Envy','Excitement','Fear','Guilt','Horror','Interest',
                'Joy','Love','Nostalgia','Pain','Pride','Realization','Relief','Romance',
                'Sadness','Satisfaction','Shame','Surprise (negative)','Surprise (positive)','Sympathy','Tiredness','Triumph']

# Start webcam
print("\nStarting webcam.")
webcam = cv2.VideoCapture(0)
print("Press \'esc\' upon finalizing trade.\n")

fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
out = cv2.VideoWriter('tradefootage.mp4', fourcc, 30.0, (640, 480)) # 30 fps, 640 x 480 px

while(True):
    # Capture frame
    check, frame = webcam.read()

    # Check for successful capture
    if check:
        # Write the frame into the file 'tradefootage.mp4'
        out.write(frame)
        # Display the resulting frame
        cv2.imshow("Midas", frame)

    # Stop recording when 'esc' key is pressed
    if cv2.waitKey(1) & 0xFF == 27:
        time_of_trade = datetime.datetime.now()
        currency = np.random.choice(['BTCUSDT', 'ETHUSDT', 'XRPUSDT', 'DOGEUSDT'])
        break

# Close webcam, release video, and free memory
webcam.release()
out.release()
cv2.destroyAllWindows()

# Start Hume Batch API
batch_client = HumeBatchClient(API_KEY)

# Send video to analyze facial expressions
job = batch_client.submit_job(urls=[], configs=[FaceConfig(identify_faces=True)], files=["tradefootage.mp4"])
print("Hume API is processing the footage...")
details = job.await_complete()
print("Emotion predictions downloaded.\n")
job.download_predictions("trade_emotions.json")

# Process emotion predictions into pandas DataFrame
vid_dict = json.load(open("trade_emotions.json"))[0]["results"]["predictions"][0]["models"]["face"]["grouped_predictions"][0]["predictions"]
trade_df = pd.DataFrame.from_dict({"name": all_emotions, "score": np.repeat(0.0, 48),
                                "top count": np.repeat(0, 48), "total top score": np.repeat(0.0, 48)})
num_frames = len(vid_dict)
for i in range(num_frames):
    emotions_dict = vid_dict[i]["emotions"]
    emotions_df = pd.DataFrame.from_dict(emotions_dict).sort_values("name")
    trade_df["score"] = trade_df["score"] + emotions_df["score"]

    emotions_df = emotions_df.sort_values("score", ascending=False)
    index = emotions_df.iloc[[0]].index[0]
    trade_df.iloc[index, 2] += 1
    trade_df.iloc[index, 3] += emotions_df.iloc[0, 1]
trade_df["score"] = trade_df["score"] / num_frames
trade_df.rename(columns={"score": "mean score"}, inplace=True)
trade_df["mean top score"] = (trade_df["total top score"] / trade_df["top count"]).fillna(0.0)

# Define statistics
highest_mean = trade_df.sort_values("mean score", ascending=False).iloc[0, 0], trade_df.sort_values("mean score", ascending=False).iloc[0, 1]
top = trade_df[trade_df["top count"] > 0].sort_values("top count", ascending=False)
top_emotion = top.iloc[0, 0]
top_emotion_time_proportion = top.iloc[0, 2] / num_frames
top_emotion_mean_score = round(top.iloc[0, 4], 2)

# Decide on descriptive message depending on emotion score
description = ""
percentage = round(top_emotion_time_proportion * 100, 1)

if top_emotion_mean_score >= 0.75 and top_emotion_mean_score <= 1:
    description = f"This trade was characterized by very prominent {top_emotion}, which was observed during {percentage}% of the time elapsed with a mean expressiveness score of {top_emotion_mean_score}."
elif top_emotion_mean_score >= 0.5 and top_emotion_mean_score < 0.75:
    description = f"{top_emotion} was fairly noticeable during {percentage}% of the time elapsed for this trade with a mean expressiveness score of {top_emotion_mean_score}."
elif top_emotion_mean_score >= 0.3 and top_emotion_mean_score < 0.5:
    description = f"Some {top_emotion} was detected during {percentage}% of the time elapsed for this trade with a mean expressiveness score of {top_emotion_mean_score}."
elif top_emotion_mean_score < 0.3:
    description = "This trade had no significant emotional context."

# Test printing
# print(top)
# print(f"Using mean over entire vid: {highest_mean}")
print(description, "\n")

# Send trade data to database
insert_into_table(currency, top_emotion , top_emotion_mean_score, np.round(random.random(), decimals=2), description, time_of_trade)