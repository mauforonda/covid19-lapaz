> Casos de covid-19 por zona en el Municipio de La Paz, Bolivia

Fuente: [Observatorio Covid-19 del Gobierno Autónomo Municipal](http://observatoriocovid19.lapaz.bo/observatorio/index.php/datos-abiertos-covid)

Los datos comenzaron a ser recolectados el 1 de Julio, el primer día de operación del observatorio. Consulto la fuente a cada hora entre las 10am y 6pm para actualizar los datos del día anterior.

Última actualización para el 2020-07-30

## Confirmados en el último día

| Macrodistrito   | Zona                |   Total |   Último Día |
|-----------------|---------------------|---------|--------------|
| CENTRO          | Miraflores          |     582 |           25 |
| SAN ANTONIO     | San Antonio         |     385 |           21 |
| NO IDENTIFICADO | No Identificado     |     715 |           16 |
| SAN ANTONIO     | Villa Copacabana    |     312 |           15 |
| COTAHUMA        | Sopocachi           |     356 |           14 |
| SAN ANTONIO     | Pampahasi           |     228 |           13 |
| COTAHUMA        | San Pedro           |     292 |           12 |
| COTAHUMA        | Pasankeri           |      88 |           11 |
| CENTRO          | Central             |     154 |           10 |
| COTAHUMA        | San Pedro Alto      |     155 |           10 |
| PERIFERICA      | Villa Fátima        |     215 |           10 |
| COTAHUMA        | Sopocachi Alto      |     162 |            9 |
| CENTRO          | Miraflores Sur      |     216 |            9 |
| MAX PAREDES     | El Tejar            |     200 |            9 |
| MAX PAREDES     | La Portada          |      97 |            9 |
| MAX PAREDES     | Mariscal Santa Cruz |      78 |            9 |
| SAN ANTONIO     | Villa Armonía       |      92 |            9 |
| MAX PAREDES     | Pura Pura           |     140 |            8 |
| SUR             | Obrajes             |     209 |            8 |
| MAX PAREDES     | 14 de Septiembre    |      83 |            8 |
| PERIFERICA      | Achachicala         |     157 |            7 |
| COTAHUMA        | Tembladerani        |     158 |            7 |
| SUR             | Cota Cota           |     107 |            6 |
| SUR             | Alto Següencoma     |      63 |            6 |
| PERIFERICA      | Challapampa         |      95 |            6 |
| MAX PAREDES     | Munaypata           |     204 |            6 |
| MAX PAREDES     | Callampaya          |      76 |            6 |
| SAN ANTONIO     | San Isidro          |      62 |            6 |
| SUR             | Irpavi              |     190 |            6 |
| COTAHUMA        | Villa Nuevo Potosí  |     153 |            5 |
| MAX PAREDES     | Chijini             |     112 |            5 |
| PERIFERICA      | Villa El Carmen     |     131 |            5 |
| PERIFERICA      | San Juan Lazareto   |      56 |            5 |
| MAX PAREDES     | Alto Tejar          |      24 |            5 |
| PERIFERICA      | Zona Norte          |     124 |            5 |
| MAX PAREDES     | Gran Poder          |     118 |            4 |
| CENTRO          | El Rosario          |      39 |            4 |
| SUR             | Achumani            |     183 |            4 |
| MAX PAREDES     | Obispo Indaburo     |      67 |            4 |
| PERIFERICA      | Las Delicias        |      58 |            4 |
| PERIFERICA      | Agua de la Vida     |      61 |            4 |
| CENTRO          | San Jorge           |     134 |            4 |
| MAX PAREDES     | Los Andes           |      52 |            4 |
| SAN ANTONIO     | Kupini              |      47 |            3 |
| SUR             | Calacoto            |     111 |            3 |
| CENTRO          | Santa Barbara       |      73 |            3 |
| SUR             | Bella Vista         |      85 |            3 |
| SUR             | Alto Irpavi         |      52 |            2 |
| MAX PAREDES     | Villa Victoria      |     167 |            2 |
| SAN ANTONIO     | Escobar Uría        |      33 |            2 |

## Recuperados en el último día

| Macrodistrito   | Zona            |   Total |   Último Día |
|-----------------|-----------------|---------|--------------|
| NO IDENTIFICADO | No Identificado |      31 |           16 |
| SUR             | Obrajes         |      12 |            1 |

## Fallecidos en el último día

| Macrodistrito   | Zona            |   Total |   Último Día |
|-----------------|-----------------|---------|--------------|
| NO IDENTIFICADO | No Identificado |      18 |            7 |

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