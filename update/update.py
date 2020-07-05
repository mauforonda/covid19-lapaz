#!/usr/bin/env python3
import requests
import pandas as pd
import pytz
from  datetime import datetime, timedelta
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
from textwrap import wrap

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

def save_data(data, day):
  for col in ['confirmados', 'activos', 'recuperados', 'fallecidos']:
    data_col = data[['macrodistrito', 'macro', 'distrito', 'zona', col]]
    data_col = data_col.rename(columns={col:day})
    data_col = data_col[['macrodistrito', 'macro', 'distrito', 'zona', day]]
    data_col.to_csv('{}.csv'.format(col), index=False)
    
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

def make_plot(category):
  sns.set(font='Quicksand', rc={'axes.facecolor':'#f9f9f9', 'text.color': '#938e99', 'axes.grid': True, 'grid.color': '#dedede', 'xtick.color': '#938e99', 'ytick.color': '#938e99', 'font.weight': 'medium'})
  df = pd.read_csv('{}.csv'.format(category))
  df = df[df['zona'] != 'No Identificado']
  df['zona'] = df['zona'].apply(lambda x: x[:18] + '...' if len(x) > 17 else x)
  df = df.sort_values(df.columns.tolist()[-1], ascending=False)
  df2 = pd.concat([df[['zona', i]].rename(columns={i:'casos'}).assign(fecha=[i] * len(df)) for i in df.columns.tolist()[4:]], axis=0)
  df2['fecha'] = pd.to_datetime(df2['fecha'])
  g = sns.FacetGrid(df2, col="zona", col_wrap=6, height=1.5, aspect=1.5)
  g.map(plt.stackplot, "fecha", "casos", color='#8c8cf7', alpha=0.5)
  g.set(xticks=[])
  g.set_axis_labels('', '')
  g.set_titles("{col_name}", size=13)
  plt.tight_layout()
  g.savefig('{}.png'.format(category))
  plt.close()

data = get_data()
day = day_is()
# save_data(d, day)
save_newday(day, data, get_saved())
make_plot('activos')
