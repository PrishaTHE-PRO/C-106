import plotly.express as px
import csv
with open ('tv.csv') as f:
    df = csv.DictReader(f)
    fig=px.scatter(df,x = 'Size of TV', y ='Average')
    fig.show()