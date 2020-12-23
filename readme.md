> Casos de covid-19 por zona en el Municipio de La Paz, Bolivia

Fuente: [Observatorio Covid-19 del Gobierno Autónomo Municipal](http://observatoriocovid19.lapaz.bo/observatorio/index.php/datos-abiertos-covid)

Los datos comenzaron a ser recolectados el 1 de Julio, el primer día de operación del observatorio. Consulto la fuente a cada hora entre las 10am y 6pm para actualizar los datos del día anterior.

Última actualización para el 2020-12-22

## Confirmados en el último día

| Macrodistrito   | Zona               |   Total |   Último Día |
|-----------------|--------------------|---------|--------------|
| CENTRO          | Miraflores         |    1222 |           14 |
| NO IDENTIFICADO | No Identificado    |    2325 |           13 |
| SUR             | Calacoto           |     243 |            3 |
| COTAHUMA        | Sopocachi          |     731 |            3 |
| COTAHUMA        | Villa Nuevo Potosí |     377 |            2 |
| PERIFERICA      | Miraflores Alto    |     263 |            2 |
| SUR             | Auquisamaña        |      48 |            2 |
| SUR             | Obrajes            |     515 |            2 |
| SUR             | Irpavi             |     402 |            2 |
| COTAHUMA        | Tembladerani       |     367 |            2 |
| CENTRO          | Central            |     301 |            2 |
| CENTRO          | San Jorge          |     295 |            1 |
| CENTRO          | El Rosario         |     115 |            1 |
| CENTRO          | Santa Barbara      |     188 |            1 |
| SUR             | Següencoma Bajo    |      96 |            1 |
| SUR             | Bella Vista        |     227 |            1 |
| CENTRO          | Miraflores Sur     |     460 |            1 |
| SUR             | Chasquipampa       |     165 |            1 |
| COTAHUMA        | Alpacoma           |      15 |            1 |
| SUR             | Achumani           |     477 |            1 |
| CENTRO          | San Sebastián      |     162 |            1 |
| SUR             | Los Pinos          |     185 |            1 |
| COTAHUMA        | Belén              |     140 |            1 |
| SAN ANTONIO     | Villa Litoral      |      33 |            1 |
| COTAHUMA        | Sopocachi Alto     |     373 |            1 |
| SAN ANTONIO     | Villa Salomé       |     213 |            1 |
| SAN ANTONIO     | Pampahasi          |     589 |            1 |
| SAN ANTONIO     | San Antonio        |     894 |            1 |
| SAN ANTONIO     | Valle Hermoso      |      99 |            1 |
| PERIFERICA      | Villa Fátima       |     460 |            1 |
| PERIFERICA      | Urkupiña           |      13 |            1 |
| PERIFERICA      | Alto Las Delicias  |      50 |            1 |
| PERIFERICA      | Achachicala        |     429 |            1 |
| PERIFERICA      | Zona Norte         |     302 |            1 |
| MAX PAREDES     | Chijini            |     276 |            1 |
| MAX PAREDES     | Pura Pura          |     345 |            1 |
| COTAHUMA        | San Pedro Alto     |     347 |            1 |
| SAN ANTONIO     | San Isidro         |     142 |            1 |

## Recuperados en el último día

| Macrodistrito   | Zona             |   Total |   Último Día |
|-----------------|------------------|---------|--------------|
| CENTRO          | Miraflores Sur   |     430 |            5 |
| NO IDENTIFICADO | No Identificado  |    1956 |            3 |
| SUR             | Següencoma Bajo  |      86 |            2 |
| MAX PAREDES     | La Portada       |     199 |            2 |
| PERIFERICA      | Miraflores Alto  |     249 |            2 |
| PERIFERICA      | Villa El Carmen  |     256 |            2 |
| SAN ANTONIO     | San Isidro       |     133 |            1 |
| CENTRO          | Miraflores       |    1119 |            1 |
| SUR             | Alto Següencoma  |     115 |            1 |
| SUR             | Obrajes          |     476 |            1 |
| SUR             | Los Pinos        |     171 |            1 |
| SAN ANTONIO     | Villa Armonía    |     235 |            1 |
| COTAHUMA        | Llojeta          |     107 |            1 |
| SAN ANTONIO     | Pampahasi        |     544 |            1 |
| COTAHUMA        | San Pedro        |     557 |            1 |
| PERIFERICA      | Agua de la Vida  |     132 |            1 |
| PERIFERICA      | Achachicala      |     385 |            1 |
| MAX PAREDES     | Villa Victoria   |     312 |            1 |
| MAX PAREDES     | Callampaya       |     141 |            1 |
| MAX PAREDES     | Pura Pura        |     313 |            1 |
| SAN ANTONIO     | Villa Copacabana |     642 |            1 |

## Fallecidos en el último día

| Macrodistrito   | Zona            |   Total |   Último Día |
|-----------------|-----------------|---------|--------------|
| NO IDENTIFICADO | No Identificado |     164 |            1 |

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