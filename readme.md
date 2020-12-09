> Casos de covid-19 por zona en el Municipio de La Paz, Bolivia

Fuente: [Observatorio Covid-19 del Gobierno Autónomo Municipal](http://observatoriocovid19.lapaz.bo/observatorio/index.php/datos-abiertos-covid)

Los datos comenzaron a ser recolectados el 1 de Julio, el primer día de operación del observatorio. Consulto la fuente a cada hora entre las 10am y 6pm para actualizar los datos del día anterior.

Última actualización para el 2020-12-08

## Confirmados en el último día

| Macrodistrito   | Zona                  |   Total |   Último Día |
|-----------------|-----------------------|---------|--------------|
| PERIFERICA      | Villa Pabón           |     151 |            3 |
| NO IDENTIFICADO | No Identificado       |    2272 |            3 |
| COTAHUMA        | Sopocachi Alto        |     361 |            1 |
| COTAHUMA        | Tacagua               |     178 |            1 |
| MAX PAREDES     | Ciudadela Ferroviaria |     105 |            1 |
| MAX PAREDES     | Chamoco Chico         |     101 |            1 |
| PERIFERICA      | Zona Norte            |     288 |            1 |
| SAN ANTONIO     | Villa Copacabana      |     663 |            1 |
| SAN ANTONIO     | San Antonio           |     865 |            1 |
| SAN ANTONIO     | Pampahasi             |     569 |            1 |
| SUR             | Los Pinos             |     182 |            1 |
| SUR             | Calacoto              |     234 |            1 |
| CENTRO          | Miraflores Sur        |     439 |            1 |
| CENTRO          | Miraflores            |    1166 |            1 |

## Recuperados en el último día

| Macrodistrito   | Zona                  |   Total |   Último Día |
|-----------------|-----------------------|---------|--------------|
| SAN ANTONIO     | San Antonio           |     825 |            2 |
| COTAHUMA        | San Pedro Alto        |     323 |            2 |
| COTAHUMA        | Sopocachi             |     651 |            1 |
| CENTRO          | San Jorge             |     276 |            1 |
| SUR             | Alto Obrajes          |     333 |            1 |
| SUR             | Bella Vista           |     207 |            1 |
| SUR             | Obrajes               |     475 |            1 |
| SUR             | Alto Achumani         |      31 |            1 |
| SUR             | Achumani              |     446 |            1 |
| SUR             | Los Rosales           |      34 |            1 |
| SUR             | La Florida            |      43 |            1 |
| SAN ANTONIO     | Villa Armonía         |     229 |            1 |
| PERIFERICA      | 3 de Mayo             |      29 |            1 |
| COTAHUMA        | 8 de Diciembre        |      50 |            1 |
| PERIFERICA      | Achachicala           |     382 |            1 |
| PERIFERICA      | Challapampa           |     179 |            1 |
| PERIFERICA      | Zona Norte            |     273 |            1 |
| PERIFERICA      | Villa de la Cruz      |     141 |            1 |
| MAX PAREDES     | Alto Mcal. Santa Cruz |      87 |            1 |
| MAX PAREDES     | Villa Victoria        |     308 |            1 |
| MAX PAREDES     | Callampaya            |     140 |            1 |
| MAX PAREDES     | Chamoco Chico         |      95 |            1 |
| COTAHUMA        | San Pedro             |     548 |            1 |
| CENTRO          | Miraflores            |    1106 |            1 |

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