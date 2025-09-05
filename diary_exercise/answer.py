import streamlit as st
import plotly.express as px
from pathlib import Path

from nltk.sentiment import SentimentIntensityAnalyzer

path = Path("diary")

filenames = sorted([file.stem for file in path.glob('*.txt')])

analyzer = SentimentIntensityAnalyzer()

negativity = []
positivity = []

for filename in filenames:
    file = path / f"{filename}.txt"
    with open(file, 'r') as f:
        content = f.read()
    scores = analyzer.polarity_scores(content)
    positivity.append(scores['pos'])
    negativity.append(scores['neg'])


st.header("Diary Exercise")
st.subheader("Positivity")
pos_figure = px.line(x=filenames, y=positivity, labels={"x": "Date", "y": "Positivity"})
st.plotly_chart(pos_figure)

st.subheader("Negativity")
pos_figure = px.line(x=filenames, y=negativity, labels={"x": "Date", "y": "Negativity"})
st.plotly_chart(pos_figure)