import pandas as pd 
import csv 
import plotly.figure_factory as ff 

df = pd.read_csv('pdata1.csv') 
figure = ff.create_distplot([df["Avg Rating"].tolist()], ["Average rating"])
figure.show()