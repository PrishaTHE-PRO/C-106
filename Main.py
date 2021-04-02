import plotly.express as px
import csv
import numpy as np

def getDataSource(data_path):
    icecream_sales=[]
    colddrink_sales=[]
    with open(data_path) as f:
        csv_reader=csv.DictReader(f)
        for row in csv_reader:
            icecream_sales.append(float(row['Temperature']))
            colddrink_sales.append(float(row['Cold drink sales']))
    return{'x': icecream_sales,'y': colddrink_sales}

def findCorrelation(dataSource):
    Correlation=np.corrcoef(dataSource['x'],dataSource['y'])
    print('correlation between Temperature & Cold drink sales is =>',Correlation[0,1])

def setUp():
    data_path='temp.csv'
    dataSource=getDataSource(data_path)
    findCorrelation(dataSource)

setUp()