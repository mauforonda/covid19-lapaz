> Casos de covid-19 por zona en el Municipio de La Paz, Bolivia

Fuente: [Observatorio Covid-19 del Gobierno Autónomo Municipal](http://observatoriocovid19.lapaz.bo/observatorio/index.php/datos-abiertos-covid)

Los datos comenzaron a ser recolectados el 1 de Julio, el primer día de operación del observatorio. Consulto la fuente a cada hora entre las 10am y 6pm para actualizar los datos del día anterior.

Última actualización para el 2020-09-27

## Confirmados en el último día

| Macrodistrito   | Zona            |   Total |   Último Día |
|-----------------|-----------------|---------|--------------|
| CENTRO          | Miraflores      |    1140 |            4 |
| NO IDENTIFICADO | No Identificado |    2228 |            4 |
| PERIFERICA      | Miraflores Alto |     251 |            3 |
| MAX PAREDES     | La Portada      |     197 |            2 |
| COTAHUMA        | San Pedro Alto  |     326 |            1 |
| MAX PAREDES     | Pura Pura       |     314 |            1 |
| MAX PAREDES     | Obispo Indaburo |     139 |            1 |
| PERIFERICA      | Plan Autopista  |      27 |            1 |
| PERIFERICA      | Vino Tinto      |     393 |            1 |
| PERIFERICA      | Challapampa     |     181 |            1 |
| PERIFERICA      | Villa Fátima    |     426 |            1 |
| SAN ANTONIO     | Pampahasi       |     545 |            1 |
| SUR             | Casegural       |      18 |            1 |
| SUR             | Ventilla        |      56 |            1 |
| CENTRO          | Central         |     274 |            1 |

## Recuperados en el último día

| Macrodistrito   | Zona                   |   Total |   Último Día |
|-----------------|------------------------|---------|--------------|
| NO IDENTIFICADO | No Identificado        |    1265 |            5 |
| SUR             | Obrajes                |     361 |            3 |
| COTAHUMA        | Sopocachi              |     525 |            3 |
| COTAHUMA        | Tembladerani           |     249 |            3 |
| PERIFERICA      | Huaychani              |      11 |            2 |
| SAN ANTONIO     | Valle de las Flores    |      20 |            2 |
| COTAHUMA        | Llojeta                |      71 |            2 |
| PERIFERICA      | Chuquiaguillo          |      61 |            2 |
| SAN ANTONIO     | Villa Copacabana       |     472 |            2 |
| CENTRO          | Miraflores Sur         |     335 |            2 |
| MAX PAREDES     | Pura Pura              |     243 |            2 |
| SAN ANTONIO     | Cuarto Centenario      |      64 |            2 |
| CENTRO          | Santa Barbara          |     126 |            1 |
| MALLASA         | Mallasilla             |      24 |            1 |
| MALLASA         | Jupapina               |      22 |            1 |
| SUR             | Alto Obrajes           |     245 |            1 |
| SAN ANTONIO     | San Isidro             |     103 |            1 |
| SUR             | Kantutani Bajo Llojeta |      36 |            1 |
| SUR             | Casegural              |      14 |            1 |
| SUR             | Coqueni                |       6 |            1 |
| CENTRO          | Central                |     210 |            1 |
| SUR             | Ovejuyo                |      30 |            1 |
| SAN ANTONIO     | Villa Armonía          |     174 |            1 |
| CENTRO          | Miraflores             |     883 |            1 |
| COTAHUMA        | Villa Nuevo Potosí     |     259 |            1 |
| COTAHUMA        | San Pedro              |     444 |            1 |
| SAN ANTONIO     | San Antonio            |     615 |            1 |
| PERIFERICA      | Villa Fátima           |     327 |            1 |
| PERIFERICA      | Barrio Gráfico         |      86 |            1 |
| PERIFERICA      | Challapampa            |     134 |            1 |
| PERIFERICA      | Villa Pabón            |     100 |            1 |
| MAX PAREDES     | Alto Mcal. Santa Cruz  |      64 |            1 |
| MAX PAREDES     | Villa Victoria         |     248 |            1 |
| MAX PAREDES     | Gran Poder             |     169 |            1 |
| MAX PAREDES     | Chijini                |     183 |            1 |
| MAX PAREDES     | Obispo Indaburo        |     108 |            1 |
| MAX PAREDES     | Chamoco Chico          |      72 |            1 |
| COTAHUMA        | San Pedro Alto         |     233 |            1 |
| SAN ANTONIO     | Pampahasi              |     404 |            1 |

## Fallecidos en el último día

| Macrodistrito   | Zona            |   Total |   Último Día |
|-----------------|-----------------|---------|--------------|
| NO IDENTIFICADO | No Identificado |     159 |            2 |

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