> Casos de covid-19 por zona en el Municipio de La Paz, Bolivia

Fuente: [Observatorio Covid-19 del Gobierno Autónomo Municipal](http://observatoriocovid19.lapaz.bo/observatorio/index.php/datos-abiertos-covid)

Los datos comenzaron a ser recolectados el 1 de Julio, el primer día de operación del observatorio. Consulto la fuente a cada hora entre las 10am y 6pm para actualizar los datos del día anterior.

Última actualización para el 2021-01-05

## Confirmados en el último día

| Macrodistrito   | Zona                  |   Total |   Último Día |
|-----------------|-----------------------|---------|--------------|
| COTAHUMA        | Sopocachi             |     919 |           23 |
| CENTRO          | Miraflores            |    1387 |           23 |
| SAN ANTONIO     | San Antonio           |     996 |           19 |
| SUR             | Obrajes               |     604 |           14 |
| SUR             | Achumani              |     542 |           12 |
| PERIFERICA      | Zona Norte            |     349 |           12 |
| SAN ANTONIO     | Villa Copacabana      |     783 |           12 |
| MAX PAREDES     | El Tejar              |     409 |           11 |
| CENTRO          | Miraflores Sur        |     535 |           10 |
| SUR             | Irpavi                |     443 |           10 |
| SAN ANTONIO     | Pampahasi             |     651 |           10 |
| SAN ANTONIO     | Villa Salomé          |     245 |           10 |
| CENTRO          | Central               |     343 |            8 |
| SUR             | Cota Cota             |     258 |            8 |
| PERIFERICA      | Achachicala           |     471 |            8 |
| MAX PAREDES     | Gran Poder            |     277 |            7 |
| MAX PAREDES     | Pura Pura             |     384 |            7 |
| PERIFERICA      | San Juan Lazareto     |     109 |            6 |
| SUR             | Los Pinos             |     215 |            6 |
| COTAHUMA        | San Pedro Alto        |     393 |            6 |
| CENTRO          | San Jorge             |     335 |            6 |
| COTAHUMA        | Tembladerani          |     403 |            6 |
| PERIFERICA      | Villa Fátima          |     511 |            5 |
| PERIFERICA      | Villa Pabón           |     166 |            5 |
| PERIFERICA      | Limanipata            |      12 |            5 |
| SUR             | Koani                 |      44 |            5 |
| MAX PAREDES     | Villa Victoria        |     378 |            4 |
| SUR             | Alto Calacoto         |      25 |            4 |
| PERIFERICA      | Vino Tinto            |     468 |            4 |
| SAN ANTONIO     | Kupini                |     179 |            4 |
| MAX PAREDES     | Callampaya            |     176 |            4 |
| SUR             | Chasquipampa          |     186 |            4 |
| SUR             | Alto Obrajes          |     420 |            4 |
| MAX PAREDES     | Los Andes             |     129 |            4 |
| COTAHUMA        | San Pedro             |     655 |            4 |
| SAN ANTONIO     | Villa Armonía         |     297 |            3 |
| MAX PAREDES     | Ciudadela Ferroviaria |     118 |            3 |
| SAN ANTONIO     | Valle Hermoso         |     115 |            3 |
| SUR             | Alto Següencoma       |     147 |            3 |
| PERIFERICA      | Villa El Carmen       |     293 |            3 |
| COTAHUMA        | Sopocachi Alto        |     426 |            3 |
| COTAHUMA        | Villa Nuevo Potosí    |     417 |            3 |
| SUR             | Auquisamaña           |      53 |            3 |
| SUR             | Calacoto              |     271 |            3 |
| SUR             | Alto Irpavi           |     140 |            3 |
| CENTRO          | Santa Barbara         |     202 |            3 |
| COTAHUMA        | Llojeta               |     135 |            3 |
| SUR             | Bolognia              |     102 |            3 |
| SUR             | Irpavi II             |      59 |            3 |
| COTAHUMA        | Inca Llojeta          |      79 |            2 |

## Recuperados en el último día

| Macrodistrito   | Zona   | Total   | Último Día   |
|-----------------|--------|---------|--------------|

## Fallecidos en el último día

| Macrodistrito   | Zona            |   Total |   Último Día |
|-----------------|-----------------|---------|--------------|
| NO IDENTIFICADO | No Identificado |     181 |           98 |
| SAN ANTONIO     | San Antonio     |      29 |            1 |

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