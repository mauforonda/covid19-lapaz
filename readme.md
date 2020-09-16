> Casos de covid-19 por zona en el Municipio de La Paz, Bolivia

Fuente: [Observatorio Covid-19 del Gobierno Autónomo Municipal](http://observatoriocovid19.lapaz.bo/observatorio/index.php/datos-abiertos-covid)

Los datos comenzaron a ser recolectados el 1 de Julio, el primer día de operación del observatorio. Consulto la fuente a cada hora entre las 10am y 6pm para actualizar los datos del día anterior.

Última actualización para el 2020-09-15

## Confirmados en el último día

| Macrodistrito   | Zona                     |   Total |   Último Día |
|-----------------|--------------------------|---------|--------------|
| NO IDENTIFICADO | No Identificado          |    2240 |          165 |
| SAN ANTONIO     | Villa Copacabana         |     637 |            9 |
| CENTRO          | Miraflores               |    1131 |            4 |
| SUR             | Obrajes                  |     485 |            3 |
| SUR             | Los Pinos                |     174 |            2 |
| COTAHUMA        | Sopocachi                |     651 |            2 |
| MAX PAREDES     | Pura Pura                |     304 |            2 |
| SUR             | Bella Vista              |     203 |            2 |
| SAN ANTONIO     | San Antonio              |     824 |            2 |
| CENTRO          | San Jorge                |     278 |            2 |
| PERIFERICA      | Villa El Carmen          |     259 |            2 |
| SUR             | Jardines del Sur         |      38 |            1 |
| SUR             | Santa Rita               |       2 |            1 |
| CENTRO          | San Sebastián            |     149 |            1 |
| SUR             | Alto Achumani            |      28 |            1 |
| CENTRO          | Santa Barbara            |     170 |            1 |
| SUR             | Ventilla                 |      53 |            1 |
| SUR             | Irpavi                   |     374 |            1 |
| SUR             | Bolognia                 |      70 |            1 |
| MALLASA         | Mallasa                  |      40 |            1 |
| SUR             | Ovejuyo                  |      47 |            1 |
| COTAHUMA        | Sopocachi Bajo           |      68 |            1 |
| SUR             | Cota Cota                |     208 |            1 |
| SAN ANTONIO     | Pampahasi                |     537 |            1 |
| PERIFERICA      | San Juan                 |      83 |            1 |
| PERIFERICA      | Limanipata               |       4 |            1 |
| PERIFERICA      | Zona Norte               |     259 |            1 |
| PERIFERICA      | Plan Autopista           |      25 |            1 |
| PERIFERICA      | Vino Tinto               |     381 |            1 |
| MAX PAREDES     | Mariscal Santa Cruz      |     159 |            1 |
| MAX PAREDES     | Sagrado Corazón de Jesús |      24 |            1 |
| MAX PAREDES     | Los Andes                |     101 |            1 |
| COTAHUMA        | San Pedro                |     553 |            1 |
| COTAHUMA        | Belén                    |     134 |            1 |
| COTAHUMA        | Tembladerani             |     342 |            1 |
| COTAHUMA        | Llojeta                  |      97 |            1 |
| COTAHUMA        | Sopocachi Alto           |     340 |            1 |
| SAN ANTONIO     | Villa Salomé             |     199 |            1 |

## Recuperados en el último día

| Macrodistrito   | Zona                  |   Total |   Último Día |
|-----------------|-----------------------|---------|--------------|
| NO IDENTIFICADO | No Identificado       |    1197 |          221 |
| PERIFERICA      | Agua de la Vida Norte |      15 |            2 |
| MAX PAREDES     | Gran Poder            |     162 |            1 |
| PERIFERICA      | Villa 18 de Mayo      |      28 |            1 |
| SAN ANTONIO     | Villa Salomé          |     151 |            1 |
| SAN ANTONIO     | Villa Armonía         |     165 |            1 |

## Fallecidos en el último día

| Macrodistrito   | Zona            |   Total |   Último Día |
|-----------------|-----------------|---------|--------------|
| NO IDENTIFICADO | No Identificado |     171 |           18 |

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