> Casos de covid-19 por zona en el Municipio de La Paz, Bolivia

Fuente: [Observatorio Covid-19 del Gobierno Autónomo Municipal](http://observatoriocovid19.lapaz.bo/observatorio/index.php/datos-abiertos-covid)

Los datos comenzaron a ser recolectados el 1 de Julio, el primer día de operación del observatorio. Consulto la fuente a cada hora entre las 10am y 6pm para actualizar los datos del día anterior.

Última actualización para el 2020-08-07

## Confirmados en el último día

| Macrodistrito   | Zona                |   Total |   Último Día |
|-----------------|---------------------|---------|--------------|
| NO IDENTIFICADO | No Identificado     |    1025 |           62 |
| CENTRO          | Miraflores          |     745 |           27 |
| SAN ANTONIO     | San Antonio         |     504 |           23 |
| SAN ANTONIO     | Pampahasi           |     335 |           21 |
| SAN ANTONIO     | Villa Copacabana    |     390 |           21 |
| SUR             | Alto Obrajes        |     197 |           15 |
| SUR             | Obrajes             |     301 |           14 |
| COTAHUMA        | Sopocachi           |     451 |           14 |
| PERIFERICA      | Villa El Carmen     |     165 |           13 |
| CENTRO          | Miraflores Sur      |     295 |           13 |
| PERIFERICA      | Vino Tinto          |     228 |           12 |
| COTAHUMA        | San Pedro Alto      |     198 |           11 |
| PERIFERICA      | La Mercéd           |      90 |            9 |
| MAX PAREDES     | Villa Victoria      |     222 |            9 |
| MAX PAREDES     | El Tejar            |     254 |            9 |
| COTAHUMA        | Sopocachi Alto      |     208 |            9 |
| PERIFERICA      | Achachicala         |     223 |            9 |
| MAX PAREDES     | La Portada          |     129 |            8 |
| MAX PAREDES     | Munaypata           |     258 |            8 |
| SAN ANTONIO     | Villa Armonía       |     132 |            8 |
| SAN ANTONIO     | Kupini              |      72 |            8 |
| SUR             | Irpavi              |     255 |            8 |
| PERIFERICA      | Zona Norte          |     159 |            8 |
| MAX PAREDES     | Pura Pura           |     205 |            8 |
| SAN ANTONIO     | Villa Salomé        |     121 |            7 |
| SAN ANTONIO     | San Isidro          |      87 |            7 |
| COTAHUMA        | Villa Nuevo Potosí  |     206 |            7 |
| COTAHUMA        | Belén               |      84 |            6 |
| COTAHUMA        | Pasankeri           |     114 |            6 |
| PERIFERICA      | Miraflores Alto     |     153 |            6 |
| MAX PAREDES     | Mariscal Santa Cruz |      98 |            5 |
| SUR             | Chasquipampa        |      86 |            5 |
| SUR             | Irpavi II           |      32 |            5 |
| SUR             | Bella Vista         |     112 |            5 |
| COTAHUMA        | Bajo Llojeta        |      98 |            5 |
| COTAHUMA        | Tembladerani        |     202 |            5 |
| SUR             | Achumani            |     253 |            4 |
| SAN ANTONIO     | Valle Hermoso       |      58 |            4 |
| CENTRO          | San Jorge           |     180 |            4 |
| CENTRO          | Central             |     195 |            4 |
| PERIFERICA      | Cupilupaca          |      10 |            4 |
| MAX PAREDES     | Gran Poder          |     139 |            4 |
| MAX PAREDES     | 14 de Septiembre    |     109 |            4 |
| MAX PAREDES     | Obispo Indaburo     |      87 |            4 |
| COTAHUMA        | Tacagua             |     121 |            4 |
| SUR             | Alto Irpavi         |      69 |            3 |
| MAX PAREDES     | Los Andes           |      68 |            3 |
| SAN ANTONIO     | Cuarto Centenario   |      50 |            3 |
| MAX PAREDES     | Callampaya          |      99 |            3 |
| PERIFERICA      | Chuquiaguillo       |      45 |            3 |

## Recuperados en el último día

| Macrodistrito   | Zona            |   Total |   Último Día |
|-----------------|-----------------|---------|--------------|
| NO IDENTIFICADO | No Identificado |      80 |           28 |

## Fallecidos en el último día

| Macrodistrito   | Zona            |   Total |   Último Día |
|-----------------|-----------------|---------|--------------|
| NO IDENTIFICADO | No Identificado |      28 |            2 |

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