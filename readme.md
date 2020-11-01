> Casos de covid-19 por zona en el Municipio de La Paz, Bolivia

Fuente: [Observatorio Covid-19 del Gobierno Autónomo Municipal](http://observatoriocovid19.lapaz.bo/observatorio/index.php/datos-abiertos-covid)

Los datos comenzaron a ser recolectados el 1 de Julio, el primer día de operación del observatorio. Consulto la fuente a cada hora entre las 10am y 6pm para actualizar los datos del día anterior.

Última actualización para el 2020-10-31

## Confirmados en el último día

| Macrodistrito   | Zona            |   Total |   Último Día |
|-----------------|-----------------|---------|--------------|
| NO IDENTIFICADO | No Identificado |    2269 |           11 |
| MAX PAREDES     | Obispo Indaburo |     142 |            2 |
| SUR             | Achumani        |     463 |            2 |
| COTAHUMA        | Sopocachi Alto  |     353 |            1 |
| MAX PAREDES     | Alto Ciudadela  |      46 |            1 |
| SUR             | Irpavi          |     381 |            1 |
| CENTRO          | Miraflores      |    1149 |            1 |

## Recuperados en el último día

| Macrodistrito   | Zona                  |   Total |   Último Día |
|-----------------|-----------------------|---------|--------------|
| SUR             | Achumani              |     386 |            4 |
| NO IDENTIFICADO | No Identificado       |    1439 |            3 |
| PERIFERICA      | Vino Tinto            |     335 |            3 |
| SUR             | Obrajes               |     420 |            3 |
| SAN ANTONIO     | San Antonio           |     714 |            2 |
| SAN ANTONIO     | Villa Copacabana      |     559 |            2 |
| SAN ANTONIO     | Kupini                |     122 |            2 |
| PERIFERICA      | Barrio Gráfico        |     100 |            2 |
| MAX PAREDES     | Gran Poder            |     193 |            2 |
| SAN ANTONIO     | Villa Salomé          |     178 |            2 |
| COTAHUMA        | San Pedro Alto        |     277 |            2 |
| SUR             | Pedregal              |      39 |            1 |
| SUR             | Irpavi                |     327 |            1 |
| SUR             | Calacoto              |     186 |            1 |
| CENTRO          | Miraflores            |    1004 |            1 |
| CENTRO          | Central               |     232 |            1 |
| SUR             | Coqueni               |      10 |            1 |
| CENTRO          | Miraflores Sur        |     369 |            1 |
| SUR             | Gramadal              |      13 |            1 |
| SUR             | Bella Vista           |     173 |            1 |
| CENTRO          | Santa Barbara         |     143 |            1 |
| CENTRO          | El Rosario            |      90 |            1 |
| SUR             | Chasquipampa          |     130 |            1 |
| COTAHUMA        | Sopocachi             |     587 |            1 |
| COTAHUMA        | Sopocachi Alto        |     289 |            1 |
| PERIFERICA      | Alto Las Delicias     |      40 |            1 |
| PERIFERICA      | Agua de la Vida Norte |      17 |            1 |
| PERIFERICA      | Poqueni               |      38 |            1 |
| PERIFERICA      | Achachicala           |     333 |            1 |
| PERIFERICA      | Villa Pabón           |     117 |            1 |
| PERIFERICA      | Zona Norte            |     228 |            1 |
| PERIFERICA      | Villa de la Cruz      |     118 |            1 |
| MAX PAREDES     | Munaypata             |     330 |            1 |
| MAX PAREDES     | Chijini               |     214 |            1 |
| MAX PAREDES     | Obispo Indaburo       |     120 |            1 |
| MAX PAREDES     | Ciudadela Ferroviaria |      88 |            1 |
| COTAHUMA        | San Pedro             |     493 |            1 |
| COTAHUMA        | Villa Nuevo Potosí    |     299 |            1 |
| COTAHUMA        | Tembladerani          |     300 |            1 |
| PERIFERICA      | Villa El Carmen       |     221 |            1 |

## Fallecidos en el último día

| Macrodistrito   | Zona            |   Total |   Último Día |
|-----------------|-----------------|---------|--------------|
| MAX PAREDES     | El Tejar        |      12 |            1 |
| NO IDENTIFICADO | No Identificado |     162 |            1 |

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