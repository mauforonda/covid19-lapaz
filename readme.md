> Casos de covid-19 por zona en el Municipio de La Paz, Bolivia

Fuente: [Observatorio Covid-19 del Gobierno Autónomo Municipal](http://observatoriocovid19.lapaz.bo/observatorio/index.php/datos-abiertos-covid)

Los datos comenzaron a ser recolectados el 1 de Julio, el primer día de operación del observatorio. Consulto la fuente a cada hora entre las 10am y 6pm para actualizar los datos del día anterior.

Última actualización para el 2020-10-14

## Confirmados en el último día

| Macrodistrito   | Zona            |   Total |   Último Día |
|-----------------|-----------------|---------|--------------|
| PERIFERICA      | Achachicala     |     393 |            2 |
| NO IDENTIFICADO | No Identificado |    2244 |            2 |
| COTAHUMA        | Bello Horizonte |     179 |            1 |
| MAX PAREDES     | Pura Pura       |     318 |            1 |
| MAX PAREDES     | Los Andes       |     108 |            1 |
| MAX PAREDES     | Gran Poder      |     226 |            1 |
| PERIFERICA      | Zona Norte      |     267 |            1 |
| SAN ANTONIO     | Escobar Uría    |      66 |            1 |
| SAN ANTONIO     | San Isidro      |     136 |            1 |
| SUR             | Cota Cota       |     214 |            1 |
| SUR             | Obrajes         |     494 |            1 |
| SUR             | Alto Següencoma |     116 |            1 |
| CENTRO          | El Rosario      |     104 |            1 |

## Recuperados en el último día

| Macrodistrito   | Zona                     |   Total |   Último Día |
|-----------------|--------------------------|---------|--------------|
| CENTRO          | Miraflores               |     947 |            6 |
| PERIFERICA      | Villa de la Cruz         |     111 |            5 |
| COTAHUMA        | Sopocachi                |     563 |            5 |
| SAN ANTONIO     | Pampahasi                |     439 |            4 |
| COTAHUMA        | Tembladerani             |     283 |            3 |
| PERIFERICA      | Villa Fátima             |     360 |            3 |
| SAN ANTONIO     | San Antonio              |     664 |            3 |
| SUR             | Obrajes                  |     384 |            3 |
| COTAHUMA        | San Pedro                |     470 |            2 |
| CENTRO          | Central                  |     221 |            2 |
| PERIFERICA      | Huaychani                |      13 |            2 |
| SAN ANTONIO     | Villa Copacabana         |     521 |            2 |
| SUR             | Los Pinos                |     143 |            1 |
| PERIFERICA      | Condorini                |      11 |            1 |
| SUR             | Cota Cota                |     185 |            1 |
| COTAHUMA        | Inca Llojeta             |      50 |            1 |
| SUR             | Calacoto                 |     176 |            1 |
| PERIFERICA      | Las Delicias             |     108 |            1 |
| SUR             | Bella Vista              |     153 |            1 |
| SUR             | Alto Obrajes             |     277 |            1 |
| CENTRO          | Santa Barbara            |     140 |            1 |
| CENTRO          | San Jorge                |     232 |            1 |
| CENTRO          | Miraflores Sur           |     354 |            1 |
| SUR             | Chasquipampa             |     120 |            1 |
| PERIFERICA      | San Juan                 |      71 |            1 |
| PERIFERICA      | Agua de la Vida          |     103 |            1 |
| COTAHUMA        | Pasankeri                |     147 |            1 |
| COTAHUMA        | Belén                    |      99 |            1 |
| MAX PAREDES     | Alto Ciudadela           |      36 |            1 |
| MAX PAREDES     | Ciudadela Ferroviaria    |      82 |            1 |
| MAX PAREDES     | Pura Pura                |     257 |            1 |
| MAX PAREDES     | Chamoco Chico            |      78 |            1 |
| MAX PAREDES     | Sagrado Corazón de Jesús |      20 |            1 |
| MAX PAREDES     | Mariscal Santa Cruz      |     137 |            1 |
| MAX PAREDES     | El Tejar                 |     307 |            1 |
| MAX PAREDES     | Villa Victoria           |     265 |            1 |
| MAX PAREDES     | La Portada               |     161 |            1 |
| MAX PAREDES     | Munaypata                |     314 |            1 |
| COTAHUMA        | Llojeta                  |      78 |            1 |
| PERIFERICA      | Vino Tinto               |     302 |            1 |
| PERIFERICA      | Villa Pabón              |     110 |            1 |
| PERIFERICA      | Challapampa              |     150 |            1 |
| PERIFERICA      | Achachicala              |     304 |            1 |

## Fallecidos en el último día

| Macrodistrito   | Zona            |   Total |   Último Día |
|-----------------|-----------------|---------|--------------|
| COTAHUMA        | San Pedro Alto  |       7 |            1 |
| PERIFERICA      | La Mercéd       |       5 |            1 |
| SAN ANTONIO     | San Antonio     |      26 |            1 |
| SUR             | Alto Següencoma |       5 |            1 |

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