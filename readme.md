> Casos de covid-19 por zona en el Municipio de La Paz, Bolivia

Fuente: [Observatorio Covid-19 del Gobierno Autónomo Municipal](http://observatoriocovid19.lapaz.bo/observatorio/index.php/datos-abiertos-covid)

Los datos comenzaron a ser recolectados el 1 de Julio, el primer día de operación del observatorio. Consulto la fuente a cada hora entre las 10am y 6pm para actualizar los datos del día anterior.

Última actualización para el 2020-10-19

## Confirmados en el último día

| Macrodistrito   | Zona      |   Total |   Último Día |
|-----------------|-----------|---------|--------------|
| COTAHUMA        | Kantutani |      30 |            1 |

## Recuperados en el último día

| Macrodistrito   | Zona                  |   Total |   Último Día |
|-----------------|-----------------------|---------|--------------|
| PERIFERICA      | Vino Tinto            |     321 |            7 |
| SAN ANTONIO     | Pampahasi             |     448 |            4 |
| SAN ANTONIO     | San Antonio           |     682 |            4 |
| PERIFERICA      | Villa El Carmen       |     207 |            3 |
| SUR             | Obrajes               |     395 |            3 |
| SUR             | Irpavi                |     320 |            3 |
| PERIFERICA      | Achachicala           |     314 |            3 |
| CENTRO          | Miraflores            |     968 |            3 |
| COTAHUMA        | San Pedro Alto        |     261 |            3 |
| COTAHUMA        | Sopocachi             |     572 |            2 |
| MAX PAREDES     | Gran Poder            |     181 |            2 |
| CENTRO          | San Jorge             |     236 |            2 |
| SUR             | Alto Obrajes          |     286 |            2 |
| MAX PAREDES     | Pura Pura             |     265 |            2 |
| SAN ANTONIO     | Kupini                |     116 |            1 |
| CENTRO          | Central               |     222 |            1 |
| CENTRO          | El Rosario            |      88 |            1 |
| COTAHUMA        | Inca Llojeta          |      51 |            1 |
| SUR             | Casegural             |      16 |            1 |
| SUR             | Alto Calacoto         |      16 |            1 |
| SUR             | Achumani              |     373 |            1 |
| COTAHUMA        | Tembladerani          |     286 |            1 |
| SUR             | Los Pinos             |     146 |            1 |
| SAN ANTONIO     | Villa Litoral         |      26 |            1 |
| MAX PAREDES     | Obispo Indaburo       |     114 |            1 |
| SAN ANTONIO     | Villa Salomé          |     172 |            1 |
| MAX PAREDES     | 14 de Septiembre      |     132 |            1 |
| SAN ANTONIO     | 24 de Junio           |       8 |            1 |
| SAN ANTONIO     | Villa Copacabana      |     538 |            1 |
| COTAHUMA        | Sopocachi Alto        |     277 |            1 |
| MAX PAREDES     | Caja Ferroviaria      |      32 |            1 |
| PERIFERICA      | Villa de la Cruz      |     113 |            1 |
| PERIFERICA      | Limanipata            |       4 |            1 |
| MAX PAREDES     | Alto Mcal. Santa Cruz |      71 |            1 |
| MAX PAREDES     | Villa Victoria        |     269 |            1 |
| MAX PAREDES     | El Tejar              |     310 |            1 |
| MAX PAREDES     | Chijini               |     200 |            1 |
| COTAHUMA        | Tacagua               |     146 |            1 |

## Fallecidos en el último día

| Macrodistrito   | Zona            |   Total |   Último Día |
|-----------------|-----------------|---------|--------------|
| NO IDENTIFICADO | No Identificado |     161 |            1 |

## Activos desde el 1 de Julio

### Centro

![Centro](plots/activos_centro.png)

### Cotahuma

![Cotahuma](plots/activos_cotahuma.png)

### Hampaturi

![Hampaturi](plots/activos_hampaturi.png)

### Mallasa

![Mallasa](plots/activos_mallasa.png)

### Max Paredes

![Max Paredes](plots/activos_max_paredes.png)

### Periferica

![Periferica](plots/activos_periferica.png)

### San Antonio

![San Antonio](plots/activos_san_antonio.png)

### Sur

![Sur](plots/activos_sur.png)

---

### Notas

Consulto el servicio de datos del Gobierno Municipal cada día a las 10am y asumo que estos valores reflejan el estado de los casos para el día anterior. Algunas posibles fuentes de error son:

1. Si los datos se actualizaran contínuamente, una parte de los casos que asigno al día anterior corresponden en realidad al día en curso. [He consultado al encargado](https://twitter.com/mauforonda/status/1278727234765959168) del servicio si la inferencia que hago es correcta y no ha respondido.

2. A diario, algunos casos no son georeferenciados y no se reportan en el conteo de ninguna zona, pero sí aparecen en el conteo total de casos. Reporto el número diario de estos casos como 'No Identificado'.  Sin embargo, el Gobierno Municipal podría georeferenciar estos casos en los días siguientes y se sumarían al conteo de casos en sus zonas. Esto significa que una parte de los valores que asigno a cada zona podría representar casos de días pasados. En la actualidad, el Gobierno Municipal no ofrece una forma de corregir este error. Por esto, si deseas estudiar la curva epidemiológica para cada zona en base a estos datos, sugiero usar una media móvil de al menos 3 días.