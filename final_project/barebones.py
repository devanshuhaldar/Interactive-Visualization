
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import parallelcoordinates
import plotly.express as px


def grabtroyneighborhoods(data):
    troyhoods = dict() # neighborhood : row data
    date_titles = list(data.keys())[9:]
 
    for row, val in data.iterrows():
        city = val["City"]
        state = val["StateName"]
        hood = val["RegionName"]
        if city == "Troy" and state == "NY":

            troy_hoods[hood] = (date_titles,val[9:])

    return troy_hoods


def create_pcg(data):
    df = pd.DataFrame.from_dict(data, orient='index', columns=['Date', 'Value'])
    df.reset_index(inplace=True, drop = False)
    df.rename(columns={'index': 'Neighborhood'}, inplace=True)
    # df['Date'] = df['Date'].apply(lambda dates: [pd.to_datetime(date) for date in dates])

    hoods = df['Neighborhood'].tolist()
    dates = df['Date'].tolist()[0]
    values = df['Value'].tolist()

    new_values = []
    for i in range(len(values)):
        sum = 0
        temp_list = []
        for j in range(len(values[i])):
            sum+= values[i][j]
            if j % 12 == 0: 
                temp_list.append(sum / 12)
        new_values.append(temp_list)
    print(len(new_values[0]))


if __name__ == "__main":
    data = pd.read_csv("sfh_neighborhood.csv")
    troy_hoods = grab_troy_neighborhoods(data)
    for key,val in troy_hoods.items():
        troy_hoods[key] = (val[0],val[1].tolist())

    create_pcg(troy_hoods)