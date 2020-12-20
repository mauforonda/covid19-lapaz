> Casos de covid-19 por zona en el Municipio de La Paz, Bolivia

Fuente: [Observatorio Covid-19 del Gobierno Autónomo Municipal](http://observatoriocovid19.lapaz.bo/observatorio/index.php/datos-abiertos-covid)

Los datos comenzaron a ser recolectados el 1 de Julio, el primer día de operación del observatorio. Consulto la fuente a cada hora entre las 10am y 6pm para actualizar los datos del día anterior.

Última actualización para el 2020-12-19

## Confirmados en el último día

| Macrodistrito   | Zona               |   Total |   Último Día |
|-----------------|--------------------|---------|--------------|
| NO IDENTIFICADO | No Identificado    |    2309 |           13 |
| COTAHUMA        | Sopocachi          |     723 |           10 |
| PERIFERICA      | Achachicala        |     428 |            8 |
| PERIFERICA      | Villa Fátima       |     458 |            8 |
| CENTRO          | Miraflores         |    1205 |            7 |
| COTAHUMA        | San Pedro          |     595 |            5 |
| CENTRO          | Miraflores Sur     |     455 |            3 |
| MAX PAREDES     | Pura Pura          |     341 |            3 |
| SAN ANTONIO     | Pampahasi          |     584 |            3 |
| PERIFERICA      | Las Delicias       |     128 |            3 |
| SUR             | Alto Obrajes       |     358 |            3 |
| PERIFERICA      | Villa El Carmen    |     281 |            2 |
| SUR             | Calacoto           |     237 |            2 |
| SAN ANTONIO     | Villa Copacabana   |     678 |            2 |
| SUR             | Obrajes            |     508 |            2 |
| PERIFERICA      | Challapampa        |     190 |            2 |
| SAN ANTONIO     | Villa Armonía      |     260 |            2 |
| PERIFERICA      | Zona Norte         |     297 |            2 |
| MAX PAREDES     | Chijini            |     273 |            2 |
| CENTRO          | Central            |     296 |            2 |
| SAN ANTONIO     | Villa Salomé       |     211 |            2 |
| MALLASA         | Mallasa            |      45 |            1 |
| SUR             | San Miguel         |      58 |            1 |
| MALLASA         | Mallasilla         |      36 |            1 |
| CENTRO          | San Sebastián      |     161 |            1 |
| CENTRO          | San Jorge          |     292 |            1 |
| COTAHUMA        | Sopocachi Bajo     |      74 |            1 |
| SAN ANTONIO     | San Antonio        |     883 |            1 |
| COTAHUMA        | Sopocachi Alto     |     370 |            1 |
| PERIFERICA      | Miraflores Alto    |     259 |            1 |
| PERIFERICA      | Agua de la Vida    |     143 |            1 |
| PERIFERICA      | Villa de la Cruz   |     155 |            1 |
| MAX PAREDES     | Munaypata          |     402 |            1 |
| MAX PAREDES     | Callampaya         |     156 |            1 |
| MAX PAREDES     | El Tejar           |     367 |            1 |
| MAX PAREDES     | Los Andes          |     118 |            1 |
| COTAHUMA        | San Pedro Alto     |     345 |            1 |
| COTAHUMA        | Bello Horizonte    |     191 |            1 |
| PERIFERICA      | Santa Rosa de Tiji |      23 |            1 |

## Recuperados en el último día

| Macrodistrito   | Zona               |   Total |   Último Día |
|-----------------|--------------------|---------|--------------|
| NO IDENTIFICADO | No Identificado    |    1925 |           28 |
| COTAHUMA        | Villa Nuevo Potosí |     345 |            2 |
| CENTRO          | Miraflores         |    1113 |            2 |
| MAX PAREDES     | 14 de Septiembre   |     150 |            1 |
| PERIFERICA      | Villa Pabón        |     138 |            1 |
| PERIFERICA      | Las Delicias       |     120 |            1 |
| PERIFERICA      | Villa El Carmen    |     253 |            1 |
| SAN ANTONIO     | Villa Copacabana   |     640 |            1 |
| SAN ANTONIO     | Villa Armonía      |     233 |            1 |
| CENTRO          | Miraflores Sur     |     425 |            1 |

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