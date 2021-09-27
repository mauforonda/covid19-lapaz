> Casos de covid-19 por zona en el Municipio de La Paz, Bolivia

Fuente: [Observatorio Covid-19 del Gobierno Autónomo Municipal](http://observatoriocovid19.lapaz.bo/observatorio/index.php/datos-abiertos-covid)

Los datos comenzaron a ser recolectados el 1 de Julio, el primer día de operación del observatorio. Consulto la fuente a cada hora entre las 10am y 6pm para actualizar los datos del día anterior.

Última actualización para el 2021-09-26

## Confirmados en el último día

| Macrodistrito   | Zona             |   Total |   Último Día |
|-----------------|------------------|---------|--------------|
| COTAHUMA        | Sopocachi        |    2323 |            1 |
| COTAHUMA        | Llojeta          |     506 |            1 |
| MAX PAREDES     | El Tejar         |    1031 |            1 |
| PERIFERICA      | Villa de la Cruz |     390 |            1 |
| SUR             | Irpavi           |    1210 |            1 |
| SUR             | Calacoto         |     769 |            1 |
| SUR             | Chasquipampa     |     595 |            1 |
| SUR             | Obrajes          |    1829 |            1 |
| CENTRO          | San Sebastián    |     479 |            1 |
| CENTRO          | Miraflores       |    3427 |            1 |

## Recuperados en el último día

| Macrodistrito   | Zona                      |   Total |   Último Día |
|-----------------|---------------------------|---------|--------------|
| COTAHUMA        | Sopocachi                 |    2112 |            9 |
| CENTRO          | Miraflores                |    3066 |            7 |
| SUR             | Alto Obrajes              |    1201 |            7 |
| SUR             | Obrajes                   |    1575 |            6 |
| SAN ANTONIO     | San Antonio               |    2022 |            5 |
| PERIFERICA      | Villa Fátima              |    1097 |            5 |
| MAX PAREDES     | Pura Pura                 |     857 |            4 |
| SUR             | Alto Irpavi               |     312 |            4 |
| PERIFERICA      | Villa El Carmen           |     657 |            4 |
| PERIFERICA      | Las Delicias              |     299 |            4 |
| PERIFERICA      | Villa Pabón               |     377 |            4 |
| NO IDENTIFICADO | No Identificado           |    4832 |            4 |
| SUR             | Bella Vista               |     673 |            3 |
| COTAHUMA        | Llojeta                   |     446 |            3 |
| COTAHUMA        | Villa Nuevo Potosí        |     873 |            3 |
| PERIFERICA      | Achachicala               |     963 |            3 |
| COTAHUMA        | Pasankeri                 |     374 |            3 |
| CENTRO          | Miraflores Sur            |     974 |            3 |
| SAN ANTONIO     | Villa Copacabana          |    1663 |            3 |
| SUR             | Calacoto                  |     668 |            3 |
| MAX PAREDES     | El Tejar                  |     931 |            3 |
| SAN ANTONIO     | Pampahasi                 |    1557 |            3 |
| CENTRO          | El Rosario                |     363 |            3 |
| CENTRO          | Santa Barbara             |     407 |            3 |
| SUR             | Irpavi                    |    1106 |            3 |
| SUR             | Irpavi II                 |     134 |            2 |
| COTAHUMA        | Cotahuma                  |     156 |            2 |
| COTAHUMA        | Inca Llojeta              |     196 |            2 |
| PERIFERICA      | San Juan                  |     184 |            2 |
| SAN ANTONIO     | Villa Litoral             |      87 |            2 |
| SUR             | Achumani                  |    1318 |            2 |
| COTAHUMA        | San Pedro Alto            |     855 |            2 |
| SUR             | Cota Cota                 |     634 |            2 |
| CENTRO          | San Jorge                 |     721 |            2 |
| PERIFERICA      | Vino Tinto                |     986 |            2 |
| SUR             | Chasquipampa              |     515 |            2 |
| MAX PAREDES     | Munaypata                 |     838 |            2 |
| MAX PAREDES     | Villa Victoria            |     786 |            2 |
| MAX PAREDES     | Mariscal Santa Cruz       |     393 |            2 |
| MAX PAREDES     | Gran Poder                |     506 |            2 |
| COTAHUMA        | San Pedro                 |    1290 |            2 |
| SUR             | San Miguel                |     140 |            1 |
| SUR             | Coqueni                   |      37 |            1 |
| CENTRO          | Central                   |     803 |            1 |
| SUR             | Huantaqui                 |     164 |            1 |
| SUR             | La Florida                |      94 |            1 |
| SUR             | Bolognia                  |     239 |            1 |
| SUR             | Los Rosales Alto Calacoto |      73 |            1 |
| COTAHUMA        | Kantutani                 |      78 |            1 |
| SAN ANTONIO     | Villa Armonía             |     712 |            1 |

## Fallecidos en el último día

| Macrodistrito   | Zona     |   Total |   Último Día |
|-----------------|----------|---------|--------------|
| SUR             | Bolognia |      11 |            1 |

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