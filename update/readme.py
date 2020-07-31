#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def make_plot(category):
  sns.set(font='Quicksand', rc={'axes.facecolor':'#f9f9f9', 'text.color': '#938e99', 'axes.grid': True, 'grid.color': '#dedede', 'xtick.color': '#938e99', 'ytick.color': '#938e99', 'font.weight': 'medium'})
  lapaz = pd.read_csv('{}.csv'.format(category))
  plots = []
  for macrodistrito, df in lapaz[lapaz['macrodistrito'] != 'NO IDENTIFICADO'].groupby('macrodistrito'):
    df['zona'] = df['zona'].apply(lambda x: x[:18] + '...' if len(x) > 17 else x)
    df = df.sort_values(df.columns.tolist()[-1], ascending=False)
    df2 = pd.concat([df[['zona', i]].rename(columns={i:'casos'}).assign(fecha=[i] * len(df)) for i in df.columns.tolist()[4:]], axis=0)
    df2['fecha'] = pd.to_datetime(df2['fecha'])
    g = sns.FacetGrid(df2, col="zona", col_wrap=6, height=1.5, aspect=1.5)
    g.map(plt.stackplot, "fecha", "casos", color='#403d3d', alpha=0.5)
    g.set(xticks=[])
    g.set_axis_labels('', '')
    g.set_titles("{col_name}", size=13)
    plt.tight_layout()
    fn = 'plots/{c}_{m}.png'.format(c=category, m=macrodistrito.lower())
    g.savefig(fn)
    plots.append({'filename':fn, 'title':macrodistrito.title()})
    plt.close()
  return plots

def make_summary(category):
  df = pd.read_csv('{}.csv'.format(category))
  days = df.columns.tolist()[-2:]
  df['diff'] = df[days].diff(axis=1)[days[1]].astype(int)
  df = df[['macrodistrito', 'zona', days[1], 'diff']]
  summary = ['## {} en el último día'.format(category.capitalize())] 
  summary.append(df[df['diff'] > 0].sort_values('diff', ascending=False).head(50).to_markdown(tablefmt='github', showindex=False, headers=['Macrodistrito', 'Zona', 'Total', 'Último Día']))
  return summary

def make_header():
  return ['> Casos de covid-19 por zona en el Municipio de La Paz, Bolivia',
          'Fuente: [Observatorio Covid-19 del Gobierno Autónomo Municipal](http://observatoriocovid19.lapaz.bo/observatorio/index.php/datos-abiertos-covid)',
          'Los datos comenzaron a ser recolectados el 1 de Julio, el primer día de operación del observatorio. Consulto la fuente a cada hora entre las 10am y 6pm para actualizar los datos del día anterior.',
          'Última actualización para el {}'.format(pd.read_csv('confirmados.csv').columns.tolist()[-1])]

def display_plot(plots):
  md = ['## Activos desde el 1 de Julio']
  for plot in plots:
    md.extend(['### {}'.format(plot['title']), '![{title}]({filename})'.format(title=plot['title'], filename=plot['filename'])])
  return md

def display_notes():
  return ["---",
          "### Notas",
          "Consulto el servicio de datos del Gobierno Municipal cada día a las 10am y asumo que estos valores reflejan el estado de los casos para el día anterior. Algunas posibles fuentes de error son:",
          "1. Si los datos se actualizaran contínuamente, una parte de los casos que asigno al día anterior corresponden en realidad al día en curso. [He consultado al encargado](https://twitter.com/mauforonda/status/1278727234765959168) del servicio si la inferencia que hago es correcta y no ha respondido.",
          "2. A diario, algunos casos no son georeferenciados y no se reportan en el conteo de ninguna zona, pero sí aparecen en el conteo total de casos. Reporto el número diario de estos casos como 'No Identificado'.  Sin embargo, el Gobierno Municipal podría georeferenciar estos casos en los días siguientes y se sumarían al conteo de casos en sus zonas. Esto significa que una parte de los valores que asigno a cada zona podría representar casos de días pasados. En la actualidad, el Gobierno Municipal no ofrece una forma de corregir este error. Por esto, si deseas estudiar la curva epidemiológica para cada zona en base a estos datos, sugiero usar una media móvil de al menos 3 días."
  ]


def write_readme(readme):
  with open('readme.md', 'w+') as f:
    f.write('\n\n'.join(readme))

def make_readme(plots):
  readme = make_header()
  readme.extend(make_summary('confirmados'))
  readme.extend(make_summary('recuperados'))
  readme.extend(make_summary('fallecidos'))
  readme.extend(display_plot(plots))
  readme.extend(display_notes())
  write_readme(readme)


plots = make_plot('activos')
make_readme(plots)
