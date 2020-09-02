> Casos de covid-19 por zona en el Municipio de La Paz, Bolivia

Fuente: [Observatorio Covid-19 del Gobierno Autónomo Municipal](http://observatoriocovid19.lapaz.bo/observatorio/index.php/datos-abiertos-covid)

Los datos comenzaron a ser recolectados el 1 de Julio, el primer día de operación del observatorio. Consulto la fuente a cada hora entre las 10am y 6pm para actualizar los datos del día anterior.

Última actualización para el 2020-09-01

## Confirmados en el último día

| Macrodistrito   | Zona                     |   Total |   Último Día |
|-----------------|--------------------------|---------|--------------|
| NO IDENTIFICADO | No Identificado          |    2032 |           23 |
| SAN ANTONIO     | Villa Copacabana         |     564 |           10 |
| PERIFERICA      | Vino Tinto               |     352 |            6 |
| PERIFERICA      | Villa de la Cruz         |     131 |            5 |
| PERIFERICA      | Achachicala              |     351 |            5 |
| SUR             | Alto Obrajes             |     306 |            4 |
| SAN ANTONIO     | Villa Armonía            |     217 |            4 |
| PERIFERICA      | Chuquiaguillo            |      74 |            4 |
| COTAHUMA        | Sopocachi                |     609 |            4 |
| MAX PAREDES     | El Tejar                 |     342 |            4 |
| SUR             | Irpavi                   |     341 |            3 |
| COTAHUMA        | Tacagua                  |     154 |            3 |
| PERIFERICA      | Challapampa              |     164 |            3 |
| MAX PAREDES     | Mariscal Santa Cruz      |     144 |            2 |
| CENTRO          | Miraflores               |    1055 |            2 |
| SUR             | Gramadal                 |      12 |            2 |
| COTAHUMA        | 8 de Diciembre           |      38 |            2 |
| COTAHUMA        | Sopocachi Alto           |     307 |            2 |
| MAX PAREDES     | 14 de Septiembre         |     140 |            2 |
| MAX PAREDES     | Gran Poder               |     209 |            2 |
| COTAHUMA        | San Pedro                |     513 |            2 |
| COTAHUMA        | Bajo Llojeta             |     148 |            2 |
| SUR             | Huantaqui                |      66 |            1 |
| COTAHUMA        | Tembladerani             |     309 |            1 |
| CENTRO          | Miraflores Sur           |     399 |            1 |
| SUR             | Següencoma Bajo          |      79 |            1 |
| COTAHUMA        | Pasankeri                |     167 |            1 |
| SUR             | Alto Següencoma          |     106 |            1 |
| COTAHUMA        | Obispo Bosque            |      60 |            1 |
| SUR             | Kantutani Bajo Llojeta   |      49 |            1 |
| SUR             | Chasquipampa             |     129 |            1 |
| SUR             | Ovejuyo                  |      34 |            1 |
| SUR             | Meseta Achumani          |      33 |            1 |
| SAN ANTONIO     | Kupini                   |     122 |            1 |
| COTAHUMA        | San Juan de Cotahuma     |      23 |            1 |
| MAX PAREDES     | Villa Victoria           |     309 |            1 |
| COTAHUMA        | Alto Tacagua             |      43 |            1 |
| PERIFERICA      | Villa El Carmen          |     248 |            1 |
| PERIFERICA      | Las Delicias             |     110 |            1 |
| PERIFERICA      | Santa Rosa               |      54 |            1 |
| COTAHUMA        | Llojeta                  |      89 |            1 |
| MAX PAREDES     | Chamoco Chico            |      84 |            1 |
| MAX PAREDES     | Sagrado Corazón de Jesús |      20 |            1 |
| MAX PAREDES     | Unión Alianza            |       7 |            1 |
| MAX PAREDES     | La Portada               |     176 |            1 |
| MAX PAREDES     | Callampaya               |     139 |            1 |
| COTAHUMA        | Sopocachi Bajo           |      62 |            1 |

## Recuperados en el último día

| Macrodistrito   | Zona            |   Total |   Último Día |
|-----------------|-----------------|---------|--------------|
| NO IDENTIFICADO | No Identificado |    1724 |          702 |
| PERIFERICA      | Challapampa     |      61 |            1 |
| PERIFERICA      | Zona Norte      |      59 |            1 |

## Fallecidos en el último día

| Macrodistrito   | Zona            |   Total |   Último Día |
|-----------------|-----------------|---------|--------------|
| NO IDENTIFICADO | No Identificado |     134 |           12 |

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