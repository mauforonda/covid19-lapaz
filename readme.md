> Casos de covid-19 por zona en el Municipio de La Paz, Bolivia

Fuente: [Observatorio Covid-19 del Gobierno Autónomo Municipal](http://observatoriocovid19.lapaz.bo/observatorio/index.php/datos-abiertos-covid)

Los datos comenzaron a ser recolectados el 1 de Julio, el primer día de operación del observatorio. Consulto la fuente a cada hora entre las 10am y 6pm para actualizar los datos del día anterior.

Última actualización para el 2021-01-03

## Confirmados en el último día

| Macrodistrito   | Zona                |   Total |   Último Día |
|-----------------|---------------------|---------|--------------|
| NO IDENTIFICADO | No Identificado     |    2585 |           80 |
| COTAHUMA        | Sopocachi           |     896 |           35 |
| CENTRO          | Miraflores          |    1364 |           29 |
| SAN ANTONIO     | San Antonio         |     977 |           29 |
| SAN ANTONIO     | Villa Copacabana    |     771 |           25 |
| SUR             | Obrajes             |     590 |           23 |
| COTAHUMA        | San Pedro           |     651 |           21 |
| SUR             | Alto Obrajes        |     416 |           16 |
| CENTRO          | Miraflores Sur      |     525 |           15 |
| SAN ANTONIO     | Villa Armonía       |     294 |           14 |
| SAN ANTONIO     | Pampahasi           |     641 |           14 |
| COTAHUMA        | Tembladerani        |     397 |           13 |
| COTAHUMA        | Sopocachi Alto      |     423 |           10 |
| CENTRO          | San Jorge           |     329 |           10 |
| SUR             | Bolognia            |      99 |           10 |
| PERIFERICA      | Zona Norte          |     337 |            9 |
| PERIFERICA      | Achachicala         |     463 |            9 |
| COTAHUMA        | Villa Nuevo Potosí  |     414 |            9 |
| COTAHUMA        | San Pedro Alto      |     387 |            8 |
| PERIFERICA      | Villa Fátima        |     506 |            8 |
| MAX PAREDES     | El Tejar            |     398 |            8 |
| SUR             | Chasquipampa        |     182 |            7 |
| SUR             | Achumani            |     530 |            7 |
| MAX PAREDES     | Pura Pura           |     377 |            7 |
| MAX PAREDES     | Chijini             |     288 |            7 |
| PERIFERICA      | Vino Tinto          |     464 |            7 |
| MAX PAREDES     | Villa Victoria      |     374 |            7 |
| COTAHUMA        | Bello Horizonte     |     217 |            7 |
| CENTRO          | Central             |     335 |            6 |
| MAX PAREDES     | Munaypata           |     423 |            6 |
| PERIFERICA      | Miraflores Alto     |     301 |            6 |
| COTAHUMA        | Bajo Llojeta        |     206 |            6 |
| SAN ANTONIO     | Villa Salomé        |     235 |            5 |
| COTAHUMA        | Sopocachi Bajo      |      88 |            5 |
| MAX PAREDES     | Gran Poder          |     270 |            5 |
| SUR             | Alto Següencoma     |     144 |            5 |
| COTAHUMA        | Llojeta             |     132 |            4 |
| SUR             | Jurenko             |       4 |            4 |
| SUR             | Bella Vista         |     257 |            4 |
| PERIFERICA      | Las Delicias        |     139 |            4 |
| CENTRO          | El Rosario          |     127 |            4 |
| PERIFERICA      | Villa El Carmen     |     290 |            4 |
| MAX PAREDES     | Mariscal Santa Cruz |     186 |            4 |
| MAX PAREDES     | Obispo Indaburo     |     153 |            4 |
| COTAHUMA        | Tacagua             |     193 |            3 |
| SUR             | Irpavi              |     433 |            3 |
| SUR             | Següencoma Bajo     |     104 |            3 |
| SUR             | La Florida          |      52 |            3 |
| SAN ANTONIO     | Escobar Uría        |      74 |            3 |
| SUR             | Los Pinos           |     209 |            3 |

## Recuperados en el último día

| Macrodistrito   | Zona            |   Total |   Último Día |
|-----------------|-----------------|---------|--------------|
| NO IDENTIFICADO | No Identificado |   13260 |        11232 |

## Fallecidos en el último día

| Macrodistrito   | Zona   | Total   | Último Día   |
|-----------------|--------|---------|--------------|

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