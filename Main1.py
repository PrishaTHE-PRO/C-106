import plotly.express as px
import csv
import numpy as np

def getDataSource(data_path):
    average_time=[]
    size_tv=[]
    with open(data_path) as f:
        csv_reader=csv.DictReader(f)
        for row in csv_reader:
            size_tv.append(float(row['Size of TV']))
            average_time.append(float(row['Average']))
    return{'x': average_time,'y': size_tv}

def findCorrelation(dataSource):
    Correlation=np.corrcoef(dataSource['x'],dataSource['y'])
    print('correlation between Average Time & Size of TV is =>',Correlation[0,1])

def setUp():
    data_path='tv.csv'
    dataSource=getDataSource(data_path)
    findCorrelation(dataSource)

setUp()