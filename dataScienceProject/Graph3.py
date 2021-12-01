#Natalie Westermann December 1
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

#read in data from csv file
df = pd.read_csv("SelectedData.csv")

#set x axis and y axis   #define legend colors   #customize what shows up when hovering over a bubble
fig = px.scatter(df, x="Participants", y="Total Medals", size={"United States ": 100, "China": 80, "Japan": 40,
                                                               "Great Britain": 30, "Russian Olympic Committee": 20},
                 color="Country",
                 labels={"value": "Total Medals", "variable": "Country"},
                 hover_name="Country", log_x=True, size_max=60)
fig.show()





