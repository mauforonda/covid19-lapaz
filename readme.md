> Casos de covid-19 por zona en el Municipio de La Paz, Bolivia

Fuente: [Observatorio Covid-19 del Gobierno Autónomo Municipal](http://observatoriocovid19.lapaz.bo/observatorio/index.php/datos-abiertos-covid)

Los datos comenzaron a ser recolectados el 1 de Julio, el primer día de operación del observatorio. Consulto la fuente a cada hora entre las 10am y 6pm para actualizar los datos del día anterior.

Última actualización para el 2020-12-17

## Confirmados en el último día

| Macrodistrito   | Zona                   |   Total |   Último Día |
|-----------------|------------------------|---------|--------------|
| COTAHUMA        | Sopocachi              |     708 |           12 |
| SUR             | Obrajes                |     508 |            5 |
| CENTRO          | Miraflores             |    1196 |            4 |
| CENTRO          | Miraflores Sur         |     451 |            4 |
| CENTRO          | Santa Barbara          |     185 |            4 |
| SAN ANTONIO     | San Antonio            |     880 |            4 |
| SAN ANTONIO     | Villa Copacabana       |     673 |            3 |
| PERIFERICA      | Agua de la Vida        |     142 |            3 |
| MAX PAREDES     | Gran Poder             |     244 |            3 |
| PERIFERICA      | Villa Fátima           |     450 |            3 |
| SUR             | Alto Obrajes           |     353 |            3 |
| CENTRO          | Central                |     293 |            3 |
| SUR             | Irpavi                 |     392 |            3 |
| PERIFERICA      | Villa de la Cruz       |     153 |            2 |
| PERIFERICA      | Agua de la Vida Norte  |      25 |            2 |
| SUR             | Achumani               |     473 |            2 |
| SAN ANTONIO     | Pampahasi              |     579 |            2 |
| PERIFERICA      | Villa Pabón            |     155 |            2 |
| PERIFERICA      | Vino Tinto             |     420 |            2 |
| SUR             | Los Rosales            |      37 |            2 |
| SUR             | Cota Cota              |     226 |            2 |
| MAX PAREDES     | Munaypata              |     399 |            2 |
| MAX PAREDES     | 14 de Septiembre       |     163 |            2 |
| MAX PAREDES     | Pura Pura              |     335 |            2 |
| COTAHUMA        | Bello Horizonte        |     189 |            2 |
| COTAHUMA        | San Pedro              |     588 |            2 |
| SUR             | Següencoma Bajo        |      94 |            2 |
| COTAHUMA        | Obispo Bosque          |      68 |            2 |
| SUR             | Casegural              |      19 |            1 |
| SUR             | Auquisamaña            |      46 |            1 |
| SUR             | Bella Vista            |     224 |            1 |
| SUR             | San Miguel             |      57 |            1 |
| SUR             | Jardines del Sur       |      43 |            1 |
| SUR             | Aruntaya               |      14 |            1 |
| CENTRO          | San Jorge              |     291 |            1 |
| SUR             | Kantutani Bajo Llojeta |      60 |            1 |
| PERIFERICA      | Alto Las Delicias      |      49 |            1 |
| SAN ANTONIO     | Villa Litoral          |      32 |            1 |
| SAN ANTONIO     | Villa Armonía          |     258 |            1 |
| COTAHUMA        | Sopocachi Bajo         |      73 |            1 |
| COTAHUMA        | Pasankeri              |     192 |            1 |
| COTAHUMA        | Bajo Llojeta           |     170 |            1 |
| COTAHUMA        | Faro Murillo           |      28 |            1 |
| COTAHUMA        | Villa Nuevo Potosí     |     367 |            1 |
| COTAHUMA        | Tacagua                |     180 |            1 |
| COTAHUMA        | Alto Tacagua           |      52 |            1 |
| MAX PAREDES     | Callampaya             |     155 |            1 |
| MAX PAREDES     | Villa Victoria         |     341 |            1 |
| MAX PAREDES     | Alto Mcal. Santa Cruz  |      97 |            1 |
| PERIFERICA      | Zona Norte             |     292 |            1 |

## Recuperados en el último día

| Macrodistrito   | Zona            |   Total |   Último Día |
|-----------------|-----------------|---------|--------------|
| NO IDENTIFICADO | No Identificado |    1900 |            1 |

## Fallecidos en el último día

| Macrodistrito   | Zona      |   Total |   Último Día |
|-----------------|-----------|---------|--------------|
| MAX PAREDES     | Pura Pura |      11 |            1 |

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