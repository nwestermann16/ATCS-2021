#NatalieWestermann December 1
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

#read in data from csv file
wide_df = pd.read_csv("SelectedData.csv")

#set x axis, y axis, and title    #define labels   #set colors with corresponding medals
fig = px.bar(wide_df, x="Country", y=["Gold Medals", "Silver Medals", "Bronze Medals"], title="Wide-Form Input"
             , labels={"value": "Medal Count", "variable": "Medal Color"},
             color_discrete_map={"Gold Medals": "red", "Silver Medals": "white", "Bronze Medals": "blue"})
fig.show()