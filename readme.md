> Casos de covid-19 por zona en el Municipio de La Paz, Bolivia

Fuente: [Observatorio Covid-19 del Gobierno Autónomo Municipal](http://observatoriocovid19.lapaz.bo/observatorio/index.php/datos-abiertos-covid)

Los datos comenzaron a ser recolectados el 1 de Julio, el primer día de operación del observatorio. Consulto la fuente a cada hora entre las 10am y 6pm para actualizar los datos del día anterior.

Última actualización para el 2021-03-02

## Confirmados en el último día

| Macrodistrito   | Zona                     |   Total |   Último Día |
|-----------------|--------------------------|---------|--------------|
| NO IDENTIFICADO | No Identificado          |    4118 |            8 |
| CENTRO          | Miraflores               |    2063 |            5 |
| CENTRO          | Central                  |     536 |            3 |
| COTAHUMA        | Sopocachi                |    1364 |            3 |
| COTAHUMA        | San Pedro                |     916 |            2 |
| SUR             | Los Pinos                |     310 |            2 |
| SUR             | Alto Irpavi              |     213 |            2 |
| MAX PAREDES     | Villa Victoria           |     597 |            2 |
| SUR             | Alto Obrajes             |     724 |            1 |
| SUR             | Cota Cota                |     388 |            1 |
| SUR             | Jardines del Sur         |      66 |            1 |
| SUR             | Achumani                 |     837 |            1 |
| SUR             | Auquisamaña              |      72 |            1 |
| CENTRO          | Santa Barbara            |     302 |            1 |
| SAN ANTONIO     | Cuarto Centenario        |     182 |            1 |
| CENTRO          | San Sebastián            |     261 |            1 |
| CENTRO          | San Jorge                |     516 |            1 |
| COTAHUMA        | Tacagua                  |     261 |            1 |
| CENTRO          | Miraflores Sur           |     729 |            1 |
| COTAHUMA        | Tembladerani             |     622 |            1 |
| SAN ANTONIO     | Callapa                  |      34 |            1 |
| SAN ANTONIO     | San Antonio              |    1457 |            1 |
| MAX PAREDES     | Ciudadela Ferroviaria    |     167 |            1 |
| SAN ANTONIO     | Villa Copacabana         |    1189 |            1 |
| COTAHUMA        | Sopocachi Alto           |     639 |            1 |
| PERIFERICA      | 27 de Mayo               |      48 |            1 |
| PERIFERICA      | Las Delicias             |     192 |            1 |
| PERIFERICA      | San Juan                 |     139 |            1 |
| PERIFERICA      | Challapampa              |     254 |            1 |
| PERIFERICA      | Villa de la Cruz         |     251 |            1 |
| MAX PAREDES     | Munaypata                |     587 |            1 |
| MAX PAREDES     | El Tejar                 |     627 |            1 |
| MAX PAREDES     | Gran Poder               |     372 |            1 |
| MAX PAREDES     | Obispo Indaburo          |     207 |            1 |
| MAX PAREDES     | Sagrado Corazón de Jesús |      38 |            1 |
| MAX PAREDES     | Caja Ferroviaria         |      53 |            1 |
| PERIFERICA      | Villa El Carmen          |     436 |            1 |

## Recuperados en el último día

| Macrodistrito   | Zona            |   Total |   Último Día |
|-----------------|-----------------|---------|--------------|
| CENTRO          | Miraflores      |    1306 |            4 |
| NO IDENTIFICADO | No Identificado |    2155 |            2 |
| COTAHUMA        | Tembladerani    |     391 |            1 |
| CENTRO          | San Sebastián   |     172 |            1 |
| SUR             | Alto Obrajes    |     402 |            1 |
| SUR             | Obrajes         |     561 |            1 |
| SUR             | Chasquipampa    |     176 |            1 |
| SUR             | Alto Achumani   |      32 |            1 |
| SAN ANTONIO     | Villa Armonía   |     275 |            1 |
| SAN ANTONIO     | Pampahasi       |     649 |            1 |
| COTAHUMA        | Sopocachi Alto  |     401 |            1 |
| PERIFERICA      | Miraflores Alto |     278 |            1 |
| PERIFERICA      | Achachicala     |     453 |            1 |
| PERIFERICA      | Zona Norte      |     317 |            1 |
| MAX PAREDES     | El Tejar        |     396 |            1 |
| MAX PAREDES     | Gran Poder      |     244 |            1 |
| MAX PAREDES     | Chijini         |     285 |            1 |
| COTAHUMA        | Bello Horizonte |     199 |            1 |
| COTAHUMA        | San Pedro       |     619 |            1 |
| PERIFERICA      | 3 de Mayo       |      32 |            1 |

## Fallecidos en el último día

| Macrodistrito   | Zona            |   Total |   Último Día |
|-----------------|-----------------|---------|--------------|
| NO IDENTIFICADO | No Identificado |     215 |            1 |

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