> Casos de covid-19 por zona en el Municipio de La Paz, Bolivia

Fuente: [Observatorio Covid-19 del Gobierno Autónomo Municipal](http://observatoriocovid19.lapaz.bo/observatorio/index.php/datos-abiertos-covid)

Los datos comenzaron a ser recolectados el 1 de Julio, el primer día de operación del observatorio. Consulto la fuente a cada hora entre las 10am y 6pm para actualizar los datos del día anterior.

Última actualización para el 2020-11-17

## Confirmados en el último día

| Macrodistrito   | Zona               |   Total |   Último Día |
|-----------------|--------------------|---------|--------------|
| SUR             | Achumani           |     468 |            2 |
| COTAHUMA        | Villa Nuevo Potosí |     361 |            1 |
| MAX PAREDES     | El Tejar           |     360 |            1 |
| PERIFERICA      | Vino Tinto         |     414 |            1 |
| SAN ANTONIO     | Villa Copacabana   |     660 |            1 |
| SUR             | Los Pinos          |     181 |            1 |
| SUR             | Irpavi             |     385 |            1 |
| SUR             | Calacoto           |     232 |            1 |
| SUR             | Chasquipampa       |     159 |            1 |
| CENTRO          | Miraflores         |    1155 |            1 |

## Recuperados en el último día

| Macrodistrito   | Zona                  |   Total |   Último Día |
|-----------------|-----------------------|---------|--------------|
| NO IDENTIFICADO | No Identificado       |    1585 |           20 |
| COTAHUMA        | San Pedro Alto        |     301 |            3 |
| CENTRO          | Miraflores Sur        |     406 |            3 |
| PERIFERICA      | Villa Fátima          |     404 |            3 |
| COTAHUMA        | Sopocachi             |     625 |            3 |
| MAX PAREDES     | Chijini               |     235 |            2 |
| COTAHUMA        | Bello Horizonte       |     169 |            2 |
| CENTRO          | Miraflores            |    1061 |            2 |
| CENTRO          | San Jorge             |     265 |            2 |
| SUR             | Meseta Achumani       |      34 |            2 |
| SAN ANTONIO     | Villa Copacabana      |     597 |            2 |
| SAN ANTONIO     | San Antonio           |     772 |            2 |
| PERIFERICA      | Barrio Gráfico        |     109 |            1 |
| PERIFERICA      | Villa El Carmen       |     235 |            1 |
| MAX PAREDES     | Alto Mcal. Santa Cruz |      82 |            1 |
| COTAHUMA        | Bajo Llojeta          |     152 |            1 |
| CENTRO          | El Rosario            |      97 |            1 |
| PERIFERICA      | Plan Autopista        |      25 |            1 |
| MALLASA         | Aranjuéz              |      23 |            1 |
| SUR             | Següencoma Bajo       |      75 |            1 |
| SUR             | Bolognia              |      69 |            1 |
| SUR             | Achumani              |     413 |            1 |
| SUR             | Aruntaya              |      13 |            1 |
| SUR             | Irpavi II             |      49 |            1 |
| SUR             | Irpavi                |     343 |            1 |
| PERIFERICA      | Zona Norte            |     249 |            1 |
| SAN ANTONIO     | Kupini                |     135 |            1 |
| SAN ANTONIO     | Villa Salomé          |     187 |            1 |
| MAX PAREDES     | Munaypata             |     349 |            1 |
| SAN ANTONIO     | Escobar Uría          |      57 |            1 |
| COTAHUMA        | Obispo Bosque         |      62 |            1 |
| PERIFERICA      | Poqueni               |      45 |            1 |
| PERIFERICA      | Chuquiaguillo         |      75 |            1 |
| PERIFERICA      | La Mercéd             |     141 |            1 |
| PERIFERICA      | Miraflores Alto       |     228 |            1 |
| SAN ANTONIO     | Valle Hermoso         |      89 |            1 |

## Fallecidos en el último día

| Macrodistrito   | Zona         |   Total |   Último Día |
|-----------------|--------------|---------|--------------|
| MAX PAREDES     | Munaypata    |      14 |            1 |
| SAN ANTONIO     | Villa Salomé |       4 |            1 |
| SUR             | Bolognia     |       2 |            1 |

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