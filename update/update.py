#!/usr/bin/env python3
import requests
import pandas as pd
import pytz
from  datetime import datetime, timedelta

def get_data():
  url = 'http://observatoriocovid19.lapaz.bo/obsadmin/casosXZona.php'
  data = pd.DataFrame(requests.get(url).json()['data'])
  data.index = (data['macro'] + '.' + data['distrito']).astype(float)
  data = data.sort_index()
  data[['distrito', 'macro', 'positivo', 'recuperado',
       'fallecido', 'total']] = data[['distrito', 'macro', 'positivo', 'recuperado','fallecido', 'total']].astype(int)
  return data

def get_saved():
  return [pd.read_csv('{}.csv'.format(col)) for col in ['positivo', 'recuperado', 'fallecido']]

def day_is():
  return datetime.strftime(datetime.now(pytz.timezone('America/La_Paz')) - timedelta(days=1), '%Y-%m-%d')

def save_data(data, day):
  for col in ['positivo', 'recuperado', 'fallecido']:
    data_col = data[['macrodistrito', 'macro', 'distrito', 'zona', col]]
    data_col = data_col.rename(columns={col:day})
    data_col = data_col[['macrodistrito', 'macro', 'distrito', 'zona', day]]
    data_col.to_csv('{}.csv'.format(col), index=False)
    
def save_newday(day, data, positivo, recuperado, fallecido):
  data = data.set_index('zona', drop=False)
  for col in [['positivo', positivo], ['recuperado', recuperado], ['fallecido', fallecido]]:
    data_day = data[['zona', 'distrito', 'macro', 'macrodistrito', col[0]]]
    data_day = data_day.rename(columns={col[0]:day})
    data_col = col[1].set_index('zona', drop=False)
    data_final = pd.concat([data_day[['macrodistrito', 'macro', 'distrito', 'zona']],
                            data_col[data_col.columns[4:].tolist()],
                            data_day[day]], axis=1)
    data_final = data_final.fillna(0)
    data_final[data_final.columns[4:]] = data_final[data_final.columns[4:]].astype(int)
    data_final.fillna(0).to_csv('{}.csv'.format(col[0]), index=False)
    print(day)
  
data = get_data()
positivo, recuperado, fallecido = get_saved()
day = day_is()
# save_data(d, day)
save_newday(day, data, positivo, recuperado, fallecido)
