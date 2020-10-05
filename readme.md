> Casos de covid-19 por zona en el Municipio de La Paz, Bolivia

Fuente: [Observatorio Covid-19 del Gobierno Autónomo Municipal](http://observatoriocovid19.lapaz.bo/observatorio/index.php/datos-abiertos-covid)

Los datos comenzaron a ser recolectados el 1 de Julio, el primer día de operación del observatorio. Consulto la fuente a cada hora entre las 10am y 6pm para actualizar los datos del día anterior.

Última actualización para el 2020-10-04

## Confirmados en el último día

| Macrodistrito   | Zona                  |   Total |   Último Día |
|-----------------|-----------------------|---------|--------------|
| PERIFERICA      | Agua de la Vida Norte |      23 |            1 |
| SAN ANTONIO     | San Isidro            |     134 |            1 |
| SAN ANTONIO     | Villa Armonía         |     241 |            1 |
| SUR             | Achumani              |     453 |            1 |
| SUR             | Obrajes               |     493 |            1 |
| NO IDENTIFICADO | No Identificado       |    2229 |            1 |

## Recuperados en el último día

| Macrodistrito   | Zona                         |   Total |   Último Día |
|-----------------|------------------------------|---------|--------------|
| COTAHUMA        | Sopocachi Alto               |     261 |            5 |
| NO IDENTIFICADO | No Identificado              |    1279 |            3 |
| CENTRO          | Miraflores                   |     918 |            3 |
| SUR             | Irpavi                       |     303 |            3 |
| SUR             | Los Pinos                    |     138 |            3 |
| SAN ANTONIO     | Cuarto Centenario            |      69 |            3 |
| COTAHUMA        | San Pedro                    |     457 |            3 |
| PERIFERICA      | Villa Pabón                  |     110 |            2 |
| MALLASA         | Mallasilla                   |      29 |            2 |
| SUR             | Achumani                     |     358 |            2 |
| SAN ANTONIO     | San Antonio                  |     644 |            2 |
| COTAHUMA        | Sopocachi                    |     544 |            2 |
| COTAHUMA        | Villa Nuevo Potosí           |     269 |            2 |
| COTAHUMA        | Tembladerani                 |     269 |            2 |
| MAX PAREDES     | Mariscal Santa Cruz          |     129 |            1 |
| COTAHUMA        | Pasankeri                    |     143 |            1 |
| CENTRO          | Miraflores Sur               |     344 |            1 |
| CENTRO          | Central                      |     218 |            1 |
| CENTRO          | San Sebastián                |     121 |            1 |
| COTAHUMA        | Las Lomas                    |      29 |            1 |
| SUR             | Següencoma Bajo              |      68 |            1 |
| SUR             | Alto Obrajes                 |     258 |            1 |
| SUR             | Bella Vista                  |     143 |            1 |
| SUR             | Obrajes                      |     370 |            1 |
| SUR             | Ventilla                     |      43 |            1 |
| SUR             | Chasquipampa                 |     114 |            1 |
| COTAHUMA        | Cotahuma                     |      63 |            1 |
| SUR             | Alto Irpavi                  |      90 |            1 |
| MAX PAREDES     | Pura Pura                    |     250 |            1 |
| SUR             | Los Rosales                  |      24 |            1 |
| COTAHUMA        | Alto Tacagua                 |      38 |            1 |
| SAN ANTONIO     | Pampahasi                    |     417 |            1 |
| COTAHUMA        | Bello Horizonte              |     140 |            1 |
| SAN ANTONIO     | Villa Copacabana             |     500 |            1 |
| COTAHUMA        | 8 de Diciembre               |      37 |            1 |
| PERIFERICA      | 27 de Mayo                   |      22 |            1 |
| PERIFERICA      | Achachicala                  |     293 |            1 |
| PERIFERICA      | Challapampa                  |     142 |            1 |
| MAX PAREDES     | Alto Pura Pura San Sebastián |       8 |            1 |
| PERIFERICA      | Vino Tinto                   |     282 |            1 |
| MAX PAREDES     | Munaypata                    |     307 |            1 |
| MAX PAREDES     | Villa Victoria               |     255 |            1 |
| MAX PAREDES     | Callampaya                   |     117 |            1 |
| PERIFERICA      | Villa Fátima                 |     342 |            1 |

## Fallecidos en el último día

| Macrodistrito   | Zona            |   Total |   Último Día |
|-----------------|-----------------|---------|--------------|
| MAX PAREDES     | Callampaya      |       8 |            1 |
| PERIFERICA      | Achachicala     |       9 |            1 |
| NO IDENTIFICADO | No Identificado |     157 |            1 |

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