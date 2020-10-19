> Casos de covid-19 por zona en el Municipio de La Paz, Bolivia

Fuente: [Observatorio Covid-19 del Gobierno Autónomo Municipal](http://observatoriocovid19.lapaz.bo/observatorio/index.php/datos-abiertos-covid)

Los datos comenzaron a ser recolectados el 1 de Julio, el primer día de operación del observatorio. Consulto la fuente a cada hora entre las 10am y 6pm para actualizar los datos del día anterior.

Última actualización para el 2020-10-18

## Confirmados en el último día

| Macrodistrito   | Zona               |   Total |   Último Día |
|-----------------|--------------------|---------|--------------|
| NO IDENTIFICADO | No Identificado    |    2247 |            2 |
| COTAHUMA        | Llojeta            |     106 |            1 |
| COTAHUMA        | Villa Nuevo Potosí |     358 |            1 |
| MAX PAREDES     | 14 de Septiembre   |     152 |            1 |
| SAN ANTONIO     | San Antonio        |     846 |            1 |
| SUR             | Alto Obrajes       |     339 |            1 |

## Recuperados en el último día

| Macrodistrito   | Zona                     |   Total |   Último Día |
|-----------------|--------------------------|---------|--------------|
| NO IDENTIFICADO | No Identificado          |    1374 |           14 |
| SAN ANTONIO     | Villa Copacabana         |     537 |            6 |
| CENTRO          | Miraflores               |     965 |            5 |
| COTAHUMA        | San Pedro                |     486 |            5 |
| SUR             | Alto Següencoma          |      94 |            4 |
| SAN ANTONIO     | San Antonio              |     678 |            4 |
| MAX PAREDES     | Pura Pura                |     263 |            4 |
| COTAHUMA        | Villa Nuevo Potosí       |     283 |            3 |
| SUR             | Obrajes                  |     392 |            3 |
| PERIFERICA      | Villa El Carmen          |     204 |            3 |
| SUR             | Alto Obrajes             |     284 |            2 |
| SUR             | Bella Vista              |     155 |            2 |
| SAN ANTONIO     | Villa Salomé             |     171 |            2 |
| PERIFERICA      | Vino Tinto               |     314 |            2 |
| SUR             | Achumani                 |     372 |            2 |
| CENTRO          | San Sebastián            |     125 |            2 |
| SUR             | Chasquipampa             |     123 |            1 |
| SUR             | Ovejuyo                  |      34 |            1 |
| SUR             | Ventilla                 |      46 |            1 |
| SUR             | Bolognia                 |      63 |            1 |
| SUR             | Irpavi                   |     317 |            1 |
| SAN ANTONIO     | Villa Armonía            |     194 |            1 |
| SAN ANTONIO     | San Isidro               |     110 |            1 |
| SUR             | Kantutani Bajo Llojeta   |      41 |            1 |
| SAN ANTONIO     | Pampahasi                |     444 |            1 |
| CENTRO          | Miraflores Sur           |     360 |            1 |
| SUR             | San Miguel               |      49 |            1 |
| COTAHUMA        | Sopocachi                |     570 |            1 |
| PERIFERICA      | Villa Fátima             |     365 |            1 |
| COTAHUMA        | Sopocachi Alto           |     276 |            1 |
| COTAHUMA        | Obispo Bosque            |      54 |            1 |
| COTAHUMA        | Llojeta                  |      81 |            1 |
| COTAHUMA        | Bajo Llojeta             |     131 |            1 |
| COTAHUMA        | Tembladerani             |     285 |            1 |
| COTAHUMA        | San Juan de Cotahuma     |      21 |            1 |
| COTAHUMA        | Tacagua                  |     145 |            1 |
| COTAHUMA        | Alto Tacagua             |      39 |            1 |
| COTAHUMA        | Belén                    |     100 |            1 |
| COTAHUMA        | San Pedro Alto           |     258 |            1 |
| MAX PAREDES     | Sagrado Corazón de Jesús |      21 |            1 |
| MAX PAREDES     | Mariscal Santa Cruz      |     140 |            1 |
| MAX PAREDES     | Callampaya               |     121 |            1 |
| MAX PAREDES     | Villa Victoria           |     268 |            1 |
| MAX PAREDES     | Munaypata                |     317 |            1 |
| PERIFERICA      | Villa de la Cruz         |     112 |            1 |
| PERIFERICA      | Challapampa              |     153 |            1 |
| PERIFERICA      | Achachicala              |     311 |            1 |
| PERIFERICA      | Miraflores Alto          |     204 |            1 |
| PERIFERICA      | Las Delicias             |     109 |            1 |
| PERIFERICA      | Santa Rosa               |      45 |            1 |

## Fallecidos en el último día

| Macrodistrito   | Zona        |   Total |   Último Día |
|-----------------|-------------|---------|--------------|
| MAX PAREDES     | Los Andes   |       4 |            1 |
| PERIFERICA      | Achachicala |      11 |            1 |

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