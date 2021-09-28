> Casos de covid-19 por zona en el Municipio de La Paz, Bolivia

Fuente: [Observatorio Covid-19 del Gobierno Autónomo Municipal](http://observatoriocovid19.lapaz.bo/observatorio/index.php/datos-abiertos-covid)

Los datos comenzaron a ser recolectados el 1 de Julio, el primer día de operación del observatorio. Consulto la fuente a cada hora entre las 10am y 6pm para actualizar los datos del día anterior.

Última actualización para el 2021-09-27

## Confirmados en el último día

| Macrodistrito   | Zona             |   Total |   Último Día |
|-----------------|------------------|---------|--------------|
| COTAHUMA        | Inca Llojeta     |     210 |            1 |
| PERIFERICA      | Zona Norte       |     913 |            1 |
| PERIFERICA      | Achachicala      |    1080 |            1 |
| PERIFERICA      | Las Delicias     |     322 |            1 |
| SAN ANTONIO     | Villa Copacabana |    1832 |            1 |
| SAN ANTONIO     | Pampahasi        |    1716 |            1 |
| CENTRO          | Miraflores       |    3428 |            1 |

## Recuperados en el último día

| Macrodistrito   | Zona                      |   Total |   Último Día |
|-----------------|---------------------------|---------|--------------|
| CENTRO          | Miraflores                |    3076 |           10 |
| COTAHUMA        | Sopocachi                 |    2121 |            9 |
| SAN ANTONIO     | Pampahasi                 |    1565 |            8 |
| SUR             | Obrajes                   |    1581 |            6 |
| COTAHUMA        | Villa Nuevo Potosí        |     879 |            6 |
| CENTRO          | Central                   |     808 |            5 |
| SUR             | Irpavi                    |    1111 |            5 |
| COTAHUMA        | Sopocachi Alto            |     948 |            5 |
| MAX PAREDES     | El Tejar                  |     935 |            4 |
| SUR             | Achumani                  |    1322 |            4 |
| PERIFERICA      | Achachicala               |     967 |            4 |
| MAX PAREDES     | Munaypata                 |     842 |            4 |
| MAX PAREDES     | Villa Victoria            |     790 |            4 |
| PERIFERICA      | Villa Fátima              |    1101 |            4 |
| NO IDENTIFICADO | No Identificado           |    4835 |            3 |
| CENTRO          | Miraflores Sur            |     977 |            3 |
| CENTRO          | San Jorge                 |     724 |            3 |
| SAN ANTONIO     | Villa Copacabana          |    1666 |            3 |
| SUR             | Alto Obrajes              |    1204 |            3 |
| SUR             | Alto Següencoma           |     404 |            3 |
| SAN ANTONIO     | Kupini                    |     423 |            3 |
| PERIFERICA      | Vino Tinto                |     989 |            3 |
| COTAHUMA        | San Pedro Alto            |     858 |            3 |
| COTAHUMA        | Pasankeri                 |     376 |            2 |
| PERIFERICA      | Kalajahuira               |      53 |            2 |
| SUR             | Los Pinos                 |     515 |            2 |
| SUR             | Los Rosales Alto Calacoto |      75 |            2 |
| SUR             | Calacoto                  |     670 |            2 |
| COTAHUMA        | San Pedro                 |    1292 |            2 |
| SUR             | Chasquipampa              |     517 |            2 |
| COTAHUMA        | Alpacoma                  |      33 |            2 |
| CENTRO          | Santa Barbara             |     409 |            2 |
| COTAHUMA        | Tembladerani              |     870 |            2 |
| PERIFERICA      | Chuquiaguillo             |     195 |            2 |
| MAX PAREDES     | Gran Poder                |     508 |            2 |
| MAX PAREDES     | Callampaya                |     340 |            2 |
| MAX PAREDES     | Alto Ciudadela            |     122 |            2 |
| MAX PAREDES     | Alto Munaypata Cusicancha |      98 |            2 |
| PERIFERICA      | Agua de la Vida Norte     |      52 |            1 |
| SUR             | Bella Vista               |     674 |            1 |
| SUR             | Ovejuyo                   |     101 |            1 |
| SUR             | Casegural                 |      55 |            1 |
| PERIFERICA      | Villa de la Cruz          |     347 |            1 |
| MAX PAREDES     | La Portada                |     462 |            1 |
| SUR             | Gramadal                  |      42 |            1 |
| SUR             | Bolognia                  |     240 |            1 |
| MAX PAREDES     | Ciudadela Ferroviaria     |     226 |            1 |
| PERIFERICA      | San Juan                  |     185 |            1 |
| MAX PAREDES     | Alto Tejar                |     181 |            1 |
| SUR             | Ventilla                  |     122 |            1 |

## Fallecidos en el último día

| Macrodistrito   | Zona            |   Total |   Último Día |
|-----------------|-----------------|---------|--------------|
| NO IDENTIFICADO | No Identificado |     236 |            1 |

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