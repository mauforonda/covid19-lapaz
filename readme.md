> Casos de covid-19 por zona en el Municipio de La Paz, Bolivia

Fuente: [Observatorio Covid-19 del Gobierno Autónomo Municipal](http://observatoriocovid19.lapaz.bo/observatorio/index.php/datos-abiertos-covid)

Los datos comenzaron a ser recolectados el 1 de Julio, el primer día de operación del observatorio. Consulto la fuente a cada hora entre las 10am y 6pm para actualizar los datos del día anterior.

Última actualización para el 2020-12-04

## Confirmados en el último día

| Macrodistrito   | Zona                   |   Total |   Último Día |
|-----------------|------------------------|---------|--------------|
| NO IDENTIFICADO | No Identificado        |    2266 |            3 |
| MAX PAREDES     | Los Andes              |     114 |            2 |
| COTAHUMA        | Sopocachi Alto         |     360 |            2 |
| MAX PAREDES     | Chamoco Chico          |      99 |            1 |
| MAX PAREDES     | Pura Pura              |     326 |            1 |
| MAX PAREDES     | Callampaya             |     151 |            1 |
| MAX PAREDES     | Villa Victoria         |     331 |            1 |
| PERIFERICA      | Miraflores Alto        |     257 |            1 |
| COTAHUMA        | Pasankeri              |     187 |            1 |
| SUR             | Cota Cota              |     220 |            1 |
| SUR             | Kantutani Bajo Llojeta |      58 |            1 |
| SUR             | Obrajes                |     499 |            1 |
| SUR             | Següencoma Bajo        |      87 |            1 |
| CENTRO          | San Jorge              |     288 |            1 |
| CENTRO          | Central                |     288 |            1 |
| CENTRO          | Miraflores             |    1162 |            1 |
| SAN ANTONIO     | Villa Salomé           |     204 |            1 |

## Recuperados en el último día

| Macrodistrito   | Zona                   |   Total |   Último Día |
|-----------------|------------------------|---------|--------------|
| CENTRO          | Miraflores Sur         |     421 |            4 |
| CENTRO          | Miraflores             |    1104 |            3 |
| SAN ANTONIO     | Kupini                 |     152 |            3 |
| PERIFERICA      | Zona Norte             |     270 |            3 |
| COTAHUMA        | Sopocachi              |     649 |            2 |
| MAX PAREDES     | La Portada             |     192 |            2 |
| CENTRO          | Central                |     265 |            2 |
| CENTRO          | Santa Barbara          |     165 |            2 |
| SUR             | Bella Vista            |     204 |            2 |
| SAN ANTONIO     | Villa Armonía          |     228 |            2 |
| PERIFERICA      | Agua de la Vida        |     128 |            2 |
| PERIFERICA      | Achachicala            |     379 |            2 |
| NO IDENTIFICADO | No Identificado        |    1785 |            2 |
| COTAHUMA        | Sopocachi Alto         |     338 |            2 |
| MAX PAREDES     | Pura Pura              |     308 |            2 |
| COTAHUMA        | Villa Nuevo Potosí     |     341 |            2 |
| COTAHUMA        | San Pedro              |     545 |            2 |
| PERIFERICA      | Villa de la Cruz       |     140 |            1 |
| SAN ANTONIO     | Villa Salomé           |     196 |            1 |
| COTAHUMA        | Llojeta                |     103 |            1 |
| COTAHUMA        | Tembladerani           |     339 |            1 |
| CENTRO          | San Sebastián          |     146 |            1 |
| SUR             | Alto Següencoma        |     113 |            1 |
| COTAHUMA        | Tacagua                |     168 |            1 |
| SUR             | Kantutani Bajo Llojeta |      52 |            1 |
| SUR             | Achumani               |     445 |            1 |
| SUR             | Irpavi                 |     368 |            1 |
| COTAHUMA        | San Pedro Alto         |     320 |            1 |
| SAN ANTONIO     | San Antonio            |     820 |            1 |
| MAX PAREDES     | Villa Victoria         |     306 |            1 |
| SAN ANTONIO     | Valle Hermoso          |      93 |            1 |
| PERIFERICA      | La Mercéd              |     145 |            1 |
| PERIFERICA      | 3 de Mayo              |      28 |            1 |
| PERIFERICA      | Villa El Carmen        |     251 |            1 |
| PERIFERICA      | Barrio Gráfico         |     118 |            1 |
| COTAHUMA        | 8 de Diciembre         |      49 |            1 |
| PERIFERICA      | Las Delicias           |     118 |            1 |
| PERIFERICA      | Santiago de Lacaya     |       8 |            1 |
| PERIFERICA      | Poqueni                |      51 |            1 |
| MAX PAREDES     | Chijini                |     251 |            1 |
| PERIFERICA      | Challapampa            |     178 |            1 |
| PERIFERICA      | Alto Las Delicias      |      43 |            1 |

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