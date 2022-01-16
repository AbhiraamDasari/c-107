from asyncore import read
import csv
import pandas as pd
import plotly.graph_objects as go

data = pd.read_csv("data.csv")
db = data.loc[data["student_id"]=="TRL_987"]
print(db.groupby("level")["attempt"].mean())
fig = go.Figure(go.Bar(
    x= db.groupby("level")["attempt"].mean(),
    y= ["Level 1","Level 2","Level 3","Level 4"],
    orientation = "h",
))
fig.show()