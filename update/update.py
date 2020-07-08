#!/usr/bin/env python3
import requests
import pandas as pd
import pytz
from  datetime import datetime, timedelta

def get_total():
  url = 'http://observatoriocovid19.lapaz.bo/obsadmin/casosAcumulados.php?accion=json'
  response = requests.get(url).json()
  r = [int(response[i]) for i in ['confirmadosMunicipio', 'recuperadosMunicipio', 'fallecidosMunicipio']]
  return {'confirmados': r[0],
          'activos': r[0] - r[1] - r[2],
          'recuperados': r[1],
          'fallecidos': r[2]}

def get_data():
  url = 'http://observatoriocovid19.lapaz.bo/obsadmin/casosXZona.php'
  data = pd.DataFrame(requests.get(url).json()['data'])
  data.index = (data['macro'] + '.' + data['distrito']).astype(float)
  data = data.sort_index()
  data[['distrito', 'macro', 'positivo', 'recuperado', 'fallecido', 'total']] = data[['distrito', 'macro', 'positivo', 'recuperado','fallecido', 'total']].astype(int)
  cols = ['zona', 'distrito', 'macro', 'macrodistrito', 'activos', 'recuperados', 'fallecidos', 'confirmados']
  data.columns = cols
  total = get_total()
  ni = ['No Identificado', 0, 0, 'NO IDENTIFICADO'] + [total[i] - data[i].sum() for i in ['activos', 'recuperados', 'fallecidos', 'confirmados']]
  ni = {cols[n]:i for n, i in enumerate(ni)}
  return data.append(pd.DataFrame([ni]))

def get_saved():
  return [pd.read_csv('{}.csv'.format(col)) for col in ['confirmados', 'activos', 'recuperados', 'fallecidos']]

def day_is():
  return datetime.strftime(datetime.now(pytz.timezone('America/La_Paz')) - timedelta(days=1), '%Y-%m-%d')

def save_newday(day, data, saved):
  confirmados, activos, recuperados, fallecidos = saved
  data = data.set_index('zona', drop=False)
  for col in [['confirmados', confirmados], ['activos', activos], ['recuperados', recuperados], ['fallecidos', fallecidos]]:
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

def is_new_data(data):
  df = data.copy().sort_index()
  df = df[df['zona'] != 'No Identificado']
  cols = ['recuperados', 'fallecidos', 'confirmados']
  differences = 0
  for i in cols:
    old = pd.read_csv('{}.csv'.format(i))
    old.index = (old['macro'].astype(str) + '.' + old['distrito'].astype(str)).astype(float)
    old = old.sort_index()
    old = old[old['zona'] != 'No Identificado']
    differences += (df[i] - old[old.columns.tolist()[-1]]).sum()
  return differences > 0
  
data = get_data()
if is_new_data(data):
  save_newday(day_is(), data, get_saved())
else:
  print('0')
