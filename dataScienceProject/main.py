#Natalie Westermann Dec 1, 2021
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

df = pd.read_csv("NatalieWestermann_PieChartData.csv")

# Establishing Pie Pieces, title and color
fig = px.pie(df, values='Total Medals', names='Country', title='Total Medals Per Country',
             color_discrete_sequence=px.colors.sequential.RdBu)
# Country Names Inside Pie Pieces
fig.update_traces(textposition='inside', textinfo='percent+label')
fig.show()

