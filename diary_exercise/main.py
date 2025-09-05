from pathlib import  Path
import streamlit as st
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
import plotly.graph_objects as go

diary_folder = Path('diary')

titles = sorted([f.stem for f in diary_folder.glob('*.txt')])

sia = SentimentIntensityAnalyzer()

positivity = []
negativity = []

for title in titles:
    file_path = diary_folder / f"{title}.txt"
    text = file_path.read_text(encoding='utf-8')
    scores = sia.polarity_scores(text)
    positivity.append(scores['pos'])
    negativity.append(scores['neg'])

st.header("Diary Tone")

st.subheader("Positively")

fig = go.Figure(data=[
    go.Bar(name='Positivity', x=titles, y=positivity),
    go.Bar(name='Negativity', x=titles, y=negativity)
])
fig.update_layout(barmode='group', title='Diary Tone')

st.plotly_chart(fig)